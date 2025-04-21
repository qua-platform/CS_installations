
# Single QUA script generated at 2025-04-21 18:38:05.401603
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
    v7 = declare(int, )
    v8 = declare(int, )
    set_dc_offset("q1.z", "single", 0.4)
    set_dc_offset("q2.z", "single", 0.45)
    set_dc_offset("c12.z", "single", 0.1)
    align("q1.I", "q1.Q", "q1.resonator", "q1.z")
    with for_(v1,0,(v1<50),(v1+1)):
        r1 = declare_stream()
        save(v1, r1)
        with for_(v7,1,(v7<=1),(v7+1)):
            with for_(v6,0.0,(v6<1.475),(v6+0.05)):
                wait(18750, "q1.I", "q1.Q", "q1.z", "q1.resonator")
                with for_(v8,0,(v8<v7),(v8+1)):
                    frame_rotation_2pi(0.25, "q1.Q")
                    align("q1.I", "q1.Q")
                    play("x180_Cosine"*amp(v6), "q1.I")
                    play("x180_Cosine"*amp(v6), "q1.Q")
                    reset_frame("q1.Q")
                align("q1.I", "q1.Q", "q1.resonator", "q1.z")
                measure("readout", "q1.resonator", dual_demod.full("iw1", "iw2", v2), dual_demod.full("iw3", "iw1", v4))
                r2 = declare_stream()
                save(v2, r2)
                r4 = declare_stream()
                save(v4, r4)
    set_dc_offset("q1.z", "single", 0.4)
    set_dc_offset("q2.z", "single", 0.45)
    set_dc_offset("c12.z", "single", 0.1)
    align("q2.I", "q2.Q", "q2.resonator", "q2.z")
    with for_(v1,0,(v1<50),(v1+1)):
        save(v1, r1)
        with for_(v7,1,(v7<=1),(v7+1)):
            with for_(v6,0.0,(v6<1.475),(v6+0.05)):
                wait(18750, "q2.I", "q2.Q", "q2.z", "q2.resonator")
                with for_(v8,0,(v8<v7),(v8+1)):
                    frame_rotation_2pi(0.25, "q2.Q")
                    align("q2.I", "q2.Q")
                    play("x180_Cosine"*amp(v6), "q2.I")
                    play("x180_Cosine"*amp(v6), "q2.Q")
                    reset_frame("q2.Q")
                align("q2.I", "q2.Q", "q2.resonator", "q2.z")
                measure("readout", "q2.resonator", dual_demod.full("iw1", "iw2", v3), dual_demod.full("iw3", "iw1", v5))
                r3 = declare_stream()
                save(v3, r3)
                r5 = declare_stream()
                save(v5, r5)
    with stream_processing():
        r1.save("n")
        r2.buffer(30).buffer(1).average().save("I1")
        r4.buffer(30).buffer(1).average().save("Q1")
        r3.buffer(30).buffer(1).average().save("I2")
        r5.buffer(30).buffer(1).average().save("Q2")


config = {
    "version": 1,
    "controllers": {
        "con1": {
            "fems": {
                "3": {
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
                            "upsampling_mode": "mw",
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
                    },
                },
                "2": {
                    "type": "MW",
                    "analog_outputs": {
                        "2": {
                            "band": 1,
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 4,
                            "upconverter_frequency": 4200000000,
                        },
                        "1": {
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 4,
                            "upconverter_frequency": 7300000000,
                        },
                    },
                    "analog_inputs": {
                        "1": {
                            "band": 2,
                            "downconverter_frequency": 7300000000,
                            "sampling_rate": 1000000000.0,
                            "shareable": False,
                        },
                    },
                },
            },
        },
    },
    "elements": {
        "c12.xy": {
            "operations": {
                "x180_DragCosine": "c12.xy.x180_DragCosine.pulse",
                "x90_DragCosine": "c12.xy.x90_DragCosine.pulse",
                "-x90_DragCosine": "c12.xy.-x90_DragCosine.pulse",
                "y180_DragCosine": "c12.xy.y180_DragCosine.pulse",
                "y90_DragCosine": "c12.xy.y90_DragCosine.pulse",
                "-y90_DragCosine": "c12.xy.-y90_DragCosine.pulse",
                "x180_Square": "c12.xy.x180_Square.pulse",
                "x90_Square": "c12.xy.x90_Square.pulse",
                "-x90_Square": "c12.xy.-x90_Square.pulse",
                "y180_Square": "c12.xy.y180_Square.pulse",
                "y90_Square": "c12.xy.y90_Square.pulse",
                "-y90_Square": "c12.xy.-y90_Square.pulse",
                "x180": "c12.xy.x180_DragCosine.pulse",
                "x90": "c12.xy.x90_DragCosine.pulse",
                "-x90": "c12.xy.-x90_DragCosine.pulse",
                "y180": "c12.xy.y180_DragCosine.pulse",
                "y90": "c12.xy.y90_DragCosine.pulse",
                "-y90": "c12.xy.-y90_DragCosine.pulse",
                "saturation": "c12.xy.saturation.pulse",
            },
            "intermediate_frequency": -200000000.0,
            "MWInput": {
                "port": ('con1', 2, 2),
                "upconverter": 1,
            },
        },
        "c12.z": {
            "operations": {
                "const": "c12.z.const.pulse",
            },
            "singleInput": {
                "port": ('con1', 3, 5),
            },
        },
        "q1.I": {
            "operations": {
                "x180_Cosine": "q1.I.x180_Cosine.pulse",
                "x90_Cosine": "q1.I.x90_Cosine.pulse",
                "-x90_Cosine": "q1.I.-x90_Cosine.pulse",
                "x180_DragCosine": "q1.I.x180_DragCosine.pulse",
                "x90_DragCosine": "q1.I.x90_DragCosine.pulse",
                "x180_Square": "q1.I.x180_Square.pulse",
                "x90_Square": "q1.I.x90_Square.pulse",
                "saturation": "q1.I.saturation.pulse",
            },
            "intermediate_frequency": 100000000.0,
            "singleInput": {
                "port": ('con1', 3, 1),
            },
        },
        "q1.Q": {
            "operations": {
                "x180_Cosine": "q1.Q.x180_Cosine.pulse",
                "x90_Cosine": "q1.Q.x90_Cosine.pulse",
                "-x90_Cosine": "q1.Q.-x90_Cosine.pulse",
                "x180_DragCosine": "q1.Q.x180_DragCosine.pulse",
                "x90_DragCosine": "q1.Q.x90_DragCosine.pulse",
                "x180_Square": "q1.Q.x180_Square.pulse",
                "x90_Square": "q1.Q.x90_Square.pulse",
                "saturation": "q1.Q.saturation.pulse",
            },
            "intermediate_frequency": 100000000.0,
            "singleInput": {
                "port": ('con1', 3, 1),
            },
        },
        "q1.z": {
            "operations": {
                "const": "q1.z.const.pulse",
            },
            "singleInput": {
                "port": ('con1', 3, 2),
            },
        },
        "q1.resonator": {
            "operations": {
                "readout": "q1.resonator.readout.pulse",
                "const": "q1.resonator.const.pulse",
            },
            "intermediate_frequency": -283814266.0,
            "MWOutput": {
                "port": ('con1', 2, 1),
            },
            "smearing": 0,
            "time_of_flight": 28,
            "MWInput": {
                "port": ('con1', 2, 1),
                "upconverter": 1,
            },
        },
        "q2.I": {
            "operations": {
                "x180_Cosine": "q2.I.x180_Cosine.pulse",
                "x90_Cosine": "q2.I.x90_Cosine.pulse",
                "-x90_Cosine": "q2.I.-x90_Cosine.pulse",
                "x180_DragCosine": "q2.I.x180_DragCosine.pulse",
                "x90_DragCosine": "q2.I.x90_DragCosine.pulse",
                "x180_Square": "q2.I.x180_Square.pulse",
                "x90_Square": "q2.I.x90_Square.pulse",
                "saturation": "q2.I.saturation.pulse",
            },
            "intermediate_frequency": 200000000.0,
            "singleInput": {
                "port": ('con1', 3, 3),
            },
        },
        "q2.Q": {
            "operations": {
                "x180_Cosine": "q2.Q.x180_Cosine.pulse",
                "x90_Cosine": "q2.Q.x90_Cosine.pulse",
                "-x90_Cosine": "q2.Q.-x90_Cosine.pulse",
                "x180_DragCosine": "q2.Q.x180_DragCosine.pulse",
                "x90_DragCosine": "q2.Q.x90_DragCosine.pulse",
                "x180_Square": "q2.Q.x180_Square.pulse",
                "x90_Square": "q2.Q.x90_Square.pulse",
                "saturation": "q2.Q.saturation.pulse",
            },
            "intermediate_frequency": 200000000.0,
            "singleInput": {
                "port": ('con1', 3, 3),
            },
        },
        "q2.z": {
            "operations": {
                "const": "q2.z.const.pulse",
            },
            "singleInput": {
                "port": ('con1', 3, 4),
            },
        },
        "q2.resonator": {
            "operations": {
                "readout": "q2.resonator.readout.pulse",
                "const": "q2.resonator.const.pulse",
            },
            "intermediate_frequency": -216721946.0,
            "MWOutput": {
                "port": ('con1', 2, 1),
            },
            "smearing": 0,
            "time_of_flight": 28,
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
        "c12.xy.x180_DragCosine.pulse": {
            "operation": "control",
            "length": 32,
            "digital_marker": "ON",
            "waveforms": {
                "I": "c12.xy.x180_DragCosine.wf.I",
                "Q": "c12.xy.x180_DragCosine.wf.Q",
            },
        },
        "c12.xy.x90_DragCosine.pulse": {
            "operation": "control",
            "length": 32,
            "digital_marker": "ON",
            "waveforms": {
                "I": "c12.xy.x90_DragCosine.wf.I",
                "Q": "c12.xy.x90_DragCosine.wf.Q",
            },
        },
        "c12.xy.-x90_DragCosine.pulse": {
            "operation": "control",
            "length": 32,
            "digital_marker": "ON",
            "waveforms": {
                "I": "c12.xy.-x90_DragCosine.wf.I",
                "Q": "c12.xy.-x90_DragCosine.wf.Q",
            },
        },
        "c12.xy.y180_DragCosine.pulse": {
            "operation": "control",
            "length": 32,
            "digital_marker": "ON",
            "waveforms": {
                "I": "c12.xy.y180_DragCosine.wf.I",
                "Q": "c12.xy.y180_DragCosine.wf.Q",
            },
        },
        "c12.xy.y90_DragCosine.pulse": {
            "operation": "control",
            "length": 32,
            "digital_marker": "ON",
            "waveforms": {
                "I": "c12.xy.y90_DragCosine.wf.I",
                "Q": "c12.xy.y90_DragCosine.wf.Q",
            },
        },
        "c12.xy.-y90_DragCosine.pulse": {
            "operation": "control",
            "length": 32,
            "digital_marker": "ON",
            "waveforms": {
                "I": "c12.xy.-y90_DragCosine.wf.I",
                "Q": "c12.xy.-y90_DragCosine.wf.Q",
            },
        },
        "c12.xy.x180_Square.pulse": {
            "operation": "control",
            "length": 100,
            "digital_marker": "ON",
            "waveforms": {
                "I": "c12.xy.x180_Square.wf.I",
                "Q": "c12.xy.x180_Square.wf.Q",
            },
        },
        "c12.xy.x90_Square.pulse": {
            "operation": "control",
            "length": 100,
            "digital_marker": "ON",
            "waveforms": {
                "I": "c12.xy.x90_Square.wf.I",
                "Q": "c12.xy.x90_Square.wf.Q",
            },
        },
        "c12.xy.-x90_Square.pulse": {
            "operation": "control",
            "length": 100,
            "digital_marker": "ON",
            "waveforms": {
                "I": "c12.xy.-x90_Square.wf.I",
                "Q": "c12.xy.-x90_Square.wf.Q",
            },
        },
        "c12.xy.y180_Square.pulse": {
            "operation": "control",
            "length": 100,
            "digital_marker": "ON",
            "waveforms": {
                "I": "c12.xy.y180_Square.wf.I",
                "Q": "c12.xy.y180_Square.wf.Q",
            },
        },
        "c12.xy.y90_Square.pulse": {
            "operation": "control",
            "length": 100,
            "digital_marker": "ON",
            "waveforms": {
                "I": "c12.xy.y90_Square.wf.I",
                "Q": "c12.xy.y90_Square.wf.Q",
            },
        },
        "c12.xy.-y90_Square.pulse": {
            "operation": "control",
            "length": 100,
            "digital_marker": "ON",
            "waveforms": {
                "I": "c12.xy.-y90_Square.wf.I",
                "Q": "c12.xy.-y90_Square.wf.Q",
            },
        },
        "c12.xy.saturation.pulse": {
            "operation": "control",
            "length": 20000,
            "digital_marker": "ON",
            "waveforms": {
                "I": "c12.xy.saturation.wf.I",
                "Q": "c12.xy.saturation.wf.Q",
            },
        },
        "c12.z.const.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "single": "c12.z.const.wf",
            },
        },
        "q1.I.x180_Cosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "single": "q1.I.x180_Cosine.wf",
            },
        },
        "q1.I.x90_Cosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "single": "q1.I.x90_Cosine.wf",
            },
        },
        "q1.I.-x90_Cosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "single": "q1.I.-x90_Cosine.wf",
            },
        },
        "q1.I.x180_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "single": "q1.I.x180_DragCosine.wf",
            },
        },
        "q1.I.x90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "single": "q1.I.x90_DragCosine.wf",
            },
        },
        "q1.I.x180_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "single": "q1.I.x180_Square.wf",
            },
        },
        "q1.I.x90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "single": "q1.I.x90_Square.wf",
            },
        },
        "q1.I.saturation.pulse": {
            "operation": "control",
            "length": 20000,
            "digital_marker": "ON",
            "waveforms": {
                "single": "q1.I.saturation.wf",
            },
        },
        "q1.Q.x180_Cosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "single": "q1.Q.x180_Cosine.wf",
            },
        },
        "q1.Q.x90_Cosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "single": "q1.Q.x90_Cosine.wf",
            },
        },
        "q1.Q.-x90_Cosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "single": "q1.Q.-x90_Cosine.wf",
            },
        },
        "q1.Q.x180_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "single": "q1.Q.x180_DragCosine.wf",
            },
        },
        "q1.Q.x90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "single": "q1.Q.x90_DragCosine.wf",
            },
        },
        "q1.Q.x180_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "single": "q1.Q.x180_Square.wf",
            },
        },
        "q1.Q.x90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "single": "q1.Q.x90_Square.wf",
            },
        },
        "q1.Q.saturation.pulse": {
            "operation": "control",
            "length": 20000,
            "digital_marker": "ON",
            "waveforms": {
                "single": "q1.Q.saturation.wf",
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
            "length": 2500,
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
            "length": 2500,
            "waveforms": {
                "I": "q1.resonator.const.wf.I",
                "Q": "q1.resonator.const.wf.Q",
            },
        },
        "q2.I.x180_Cosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "single": "q2.I.x180_Cosine.wf",
            },
        },
        "q2.I.x90_Cosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "single": "q2.I.x90_Cosine.wf",
            },
        },
        "q2.I.-x90_Cosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "single": "q2.I.-x90_Cosine.wf",
            },
        },
        "q2.I.x180_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "single": "q2.I.x180_DragCosine.wf",
            },
        },
        "q2.I.x90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "single": "q2.I.x90_DragCosine.wf",
            },
        },
        "q2.I.x180_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "single": "q2.I.x180_Square.wf",
            },
        },
        "q2.I.x90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "single": "q2.I.x90_Square.wf",
            },
        },
        "q2.I.saturation.pulse": {
            "operation": "control",
            "length": 20000,
            "digital_marker": "ON",
            "waveforms": {
                "single": "q2.I.saturation.wf",
            },
        },
        "q2.Q.x180_Cosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "single": "q2.Q.x180_Cosine.wf",
            },
        },
        "q2.Q.x90_Cosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "single": "q2.Q.x90_Cosine.wf",
            },
        },
        "q2.Q.-x90_Cosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "single": "q2.Q.-x90_Cosine.wf",
            },
        },
        "q2.Q.x180_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "single": "q2.Q.x180_DragCosine.wf",
            },
        },
        "q2.Q.x90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "single": "q2.Q.x90_DragCosine.wf",
            },
        },
        "q2.Q.x180_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "single": "q2.Q.x180_Square.wf",
            },
        },
        "q2.Q.x90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "single": "q2.Q.x90_Square.wf",
            },
        },
        "q2.Q.saturation.pulse": {
            "operation": "control",
            "length": 20000,
            "digital_marker": "ON",
            "waveforms": {
                "single": "q2.Q.saturation.wf",
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
            "length": 2500,
            "waveforms": {
                "I": "q2.resonator.const.wf.I",
                "Q": "q2.resonator.const.wf.Q",
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
        "c12.xy.x180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0010235029373752758, 0.00405210941898847, 0.008961827939636185, 0.015551654046215668, 0.02355179948365188, 0.032634737357758986, 0.04242861112477117, 0.05253245844193564, 0.06253262661293602, 0.07201970757788172, 0.08060529912738312, 0.08793790613463955, 0.0937173308072291, 0.09770696282000245] + [0.09974346616959476] * 2 + [0.09770696282000245, 0.0937173308072291, 0.08793790613463956, 0.08060529912738314, 0.07201970757788172, 0.06253262661293606, 0.05253245844193569, 0.04242861112477117, 0.032634737357758986, 0.02355179948365188, 0.015551654046215675, 0.008961827939636185, 0.00405210941898847, 0.001023502937375287, 0.0],
        },
        "c12.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 32,
        },
        "c12.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0005117514686876379, 0.002026054709494235, 0.004480913969818093, 0.007775827023107834, 0.01177589974182594, 0.016317368678879493, 0.021214305562385585, 0.02626622922096782, 0.03126631330646801, 0.03600985378894086, 0.04030264956369156, 0.04396895306731977, 0.04685866540361455, 0.048853481410001225] + [0.04987173308479738] * 2 + [0.048853481410001225, 0.04685866540361455, 0.04396895306731978, 0.04030264956369157, 0.03600985378894086, 0.03126631330646803, 0.026266229220967843, 0.021214305562385585, 0.016317368678879493, 0.01177589974182594, 0.007775827023107838, 0.004480913969818093, 0.002026054709494235, 0.0005117514686876435, 0.0],
        },
        "c12.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 32,
        },
        "c12.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0005117514686876379, -0.002026054709494235, -0.004480913969818093, -0.007775827023107834, -0.01177589974182594, -0.016317368678879493, -0.021214305562385585, -0.02626622922096782, -0.03126631330646801, -0.03600985378894086, -0.04030264956369156, -0.04396895306731977, -0.04685866540361455, -0.048853481410001225] + [-0.04987173308479738] * 2 + [-0.048853481410001225, -0.04685866540361455, -0.04396895306731978, -0.04030264956369157, -0.03600985378894086, -0.03126631330646803, -0.026266229220967843, -0.021214305562385585, -0.016317368678879493, -0.01177589974182594, -0.007775827023107838, -0.004480913969818093, -0.002026054709494235, -0.0005117514686876435, 0.0],
        },
        "c12.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 6.267147980872727e-20, 2.481201414879535e-19, 5.487536950392387e-19, 9.522641674572502e-19, 1.442131792590728e-18, 1.9983013323097046e-18, 2.59800314031094e-18, 3.2166853541128915e-18, 3.829019051190435e-18, 4.409935218039061e-18, 4.935651078533234e-18, 5.384643763575336e-18, 5.738531459885338e-18, 5.982825963596272e-18] + [6.107525829022826e-18] * 2 + [5.982825963596272e-18, 5.738531459885338e-18, 5.384643763575337e-18, 4.9356510785332354e-18, 4.409935218039061e-18, 3.829019051190437e-18, 3.2166853541128946e-18, 2.59800314031094e-18, 1.9983013323097046e-18, 1.442131792590728e-18, 9.522641674572505e-19, 5.487536950392387e-19, 2.481201414879535e-19, 6.267147980872795e-20, 0.0],
        },
        "c12.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 6.267147980872727e-20, 2.481201414879535e-19, 5.487536950392387e-19, 9.522641674572502e-19, 1.442131792590728e-18, 1.9983013323097046e-18, 2.59800314031094e-18, 3.2166853541128915e-18, 3.829019051190435e-18, 4.409935218039061e-18, 4.935651078533234e-18, 5.384643763575336e-18, 5.738531459885338e-18, 5.982825963596272e-18] + [6.107525829022826e-18] * 2 + [5.982825963596272e-18, 5.738531459885338e-18, 5.384643763575337e-18, 4.9356510785332354e-18, 4.409935218039061e-18, 3.829019051190437e-18, 3.2166853541128946e-18, 2.59800314031094e-18, 1.9983013323097046e-18, 1.442131792590728e-18, 9.522641674572505e-19, 5.487536950392387e-19, 2.481201414879535e-19, 6.267147980872795e-20, 0.0],
        },
        "c12.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0010235029373752758, 0.00405210941898847, 0.008961827939636185, 0.015551654046215668, 0.02355179948365188, 0.032634737357758986, 0.04242861112477117, 0.05253245844193564, 0.06253262661293602, 0.07201970757788172, 0.08060529912738312, 0.08793790613463955, 0.0937173308072291, 0.09770696282000245] + [0.09974346616959476] * 2 + [0.09770696282000245, 0.0937173308072291, 0.08793790613463956, 0.08060529912738314, 0.07201970757788172, 0.06253262661293606, 0.05253245844193569, 0.04242861112477117, 0.032634737357758986, 0.02355179948365188, 0.015551654046215675, 0.008961827939636185, 0.00405210941898847, 0.001023502937375287, 0.0],
        },
        "c12.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 3.1335739904363637e-20, 1.2406007074397676e-19, 2.7437684751961936e-19, 4.761320837286251e-19, 7.21065896295364e-19, 9.991506661548523e-19, 1.29900157015547e-18, 1.6083426770564457e-18, 1.9145095255952173e-18, 2.2049676090195304e-18, 2.467825539266617e-18, 2.692321881787668e-18, 2.869265729942669e-18, 2.991412981798136e-18] + [3.053762914511413e-18] * 2 + [2.991412981798136e-18, 2.869265729942669e-18, 2.6923218817876684e-18, 2.4678255392666177e-18, 2.2049676090195304e-18, 1.9145095255952185e-18, 1.6083426770564473e-18, 1.29900157015547e-18, 9.991506661548523e-19, 7.21065896295364e-19, 4.761320837286253e-19, 2.7437684751961936e-19, 1.2406007074397676e-19, 3.1335739904363974e-20, 0.0],
        },
        "c12.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0005117514686876379, 0.002026054709494235, 0.004480913969818093, 0.007775827023107834, 0.01177589974182594, 0.016317368678879493, 0.021214305562385585, 0.02626622922096782, 0.03126631330646801, 0.03600985378894086, 0.04030264956369156, 0.04396895306731977, 0.04685866540361455, 0.048853481410001225] + [0.04987173308479738] * 2 + [0.048853481410001225, 0.04685866540361455, 0.04396895306731978, 0.04030264956369157, 0.03600985378894086, 0.03126631330646803, 0.026266229220967843, 0.021214305562385585, 0.016317368678879493, 0.01177589974182594, 0.007775827023107838, 0.004480913969818093, 0.002026054709494235, 0.0005117514686876435, 0.0],
        },
        "c12.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 3.1335739904363637e-20, 1.2406007074397676e-19, 2.7437684751961936e-19, 4.761320837286251e-19, 7.21065896295364e-19, 9.991506661548523e-19, 1.29900157015547e-18, 1.6083426770564457e-18, 1.9145095255952173e-18, 2.2049676090195304e-18, 2.467825539266617e-18, 2.692321881787668e-18, 2.869265729942669e-18, 2.991412981798136e-18] + [3.053762914511413e-18] * 2 + [2.991412981798136e-18, 2.869265729942669e-18, 2.6923218817876684e-18, 2.4678255392666177e-18, 2.2049676090195304e-18, 1.9145095255952185e-18, 1.6083426770564473e-18, 1.29900157015547e-18, 9.991506661548523e-19, 7.21065896295364e-19, 4.761320837286253e-19, 2.7437684751961936e-19, 1.2406007074397676e-19, 3.1335739904363974e-20, 0.0],
        },
        "c12.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0005117514686876379, -0.002026054709494235, -0.004480913969818093, -0.007775827023107834, -0.01177589974182594, -0.016317368678879493, -0.021214305562385585, -0.02626622922096782, -0.03126631330646801, -0.03600985378894086, -0.04030264956369156, -0.04396895306731977, -0.04685866540361455, -0.048853481410001225] + [-0.04987173308479738] * 2 + [-0.048853481410001225, -0.04685866540361455, -0.04396895306731978, -0.04030264956369157, -0.03600985378894086, -0.03126631330646803, -0.026266229220967843, -0.021214305562385585, -0.016317368678879493, -0.01177589974182594, -0.007775827023107838, -0.004480913969818093, -0.002026054709494235, -0.0005117514686876435, 0.0],
        },
        "c12.xy.x180_Square.wf.I": {
            "type": "constant",
            "sample": 0.25,
        },
        "c12.xy.x180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "c12.xy.x90_Square.wf.I": {
            "type": "constant",
            "sample": 0.125,
        },
        "c12.xy.x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "c12.xy.-x90_Square.wf.I": {
            "type": "constant",
            "sample": -0.125,
        },
        "c12.xy.-x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "c12.xy.y180_Square.wf.I": {
            "type": "constant",
            "sample": -0.11201840403229253,
        },
        "c12.xy.y180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.22349916590013946,
        },
        "c12.xy.y90_Square.wf.I": {
            "type": "constant",
            "sample": -0.056009202016146266,
        },
        "c12.xy.y90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.11174958295006973,
        },
        "c12.xy.-y90_Square.wf.I": {
            "type": "constant",
            "sample": 0.056009202016146266,
        },
        "c12.xy.-y90_Square.wf.Q": {
            "type": "constant",
            "sample": -0.11174958295006973,
        },
        "c12.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.25,
        },
        "c12.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "c12.z.const.wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "q1.I.x180_Cosine.wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.0008622917500937984, 0.0034268340969887735, 0.0076272067409924385, 0.013354622236979315, 0.020460743532076248, 0.028761525817413945, 0.03804198319200245, 0.04806175668463981, 0.05856133942501153, 0.06926879773531897, 0.07990681406969413, 0.0901998693929696, 0.09988137897896564, 0.10870059681486784, 0.1164291097912483, 0.12286675348161984, 0.1278467962959404, 0.13124025774121517, 0.13295924894851482, 0.13295924894851485, 0.13124025774121517, 0.12784679629594042, 0.12286675348161986, 0.11642910979124833, 0.10870059681486784, 0.0998813789789656, 0.09019986939296964, 0.07990681406969417, 0.06926879773531897, 0.058561339425011585, 0.048061756684639856, 0.03804198319200248, 0.028761525817413966, 0.020460743532076255, 0.013354622236979315, 0.007627206740992431, 0.003426834096988766, 0.0008622917500937984, 0.0],
        },
        "q1.I.x90_Cosine.wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.0004311458750468992, 0.0017134170484943867, 0.0038136033704962193, 0.006677311118489657, 0.010230371766038124, 0.014380762908706973, 0.019020991596001225, 0.024030878342319904, 0.029280669712505765, 0.03463439886765948, 0.039953407034847066, 0.0450999346964848, 0.04994068948948282, 0.05435029840743392, 0.05821455489562415, 0.06143337674080992, 0.0639233981479702, 0.06562012887060759, 0.06647962447425741, 0.06647962447425743, 0.06562012887060759, 0.06392339814797021, 0.06143337674080993, 0.05821455489562417, 0.05435029840743392, 0.0499406894894828, 0.04509993469648482, 0.03995340703484709, 0.03463439886765948, 0.029280669712505793, 0.024030878342319928, 0.01902099159600124, 0.014380762908706983, 0.010230371766038127, 0.006677311118489657, 0.0038136033704962153, 0.001713417048494383, 0.0004311458750468992, 0.0],
        },
        "q1.I.-x90_Cosine.wf": {
            "type": "arbitrary",
            "samples": [0.0, -0.0006474868681043578, -0.002573177902642726, -0.005727198717339505, -0.010027861829824942, -0.015363782324520032, -0.021596762663442206, -0.02856537192984729, -0.03608912680417736, -0.04397316598723385, -0.05201329700547076, -0.060001284688802205, -0.06773024435212678, -0.07500000000000001, -0.08162226877976886, -0.08742553740855505, -0.09225950427718974, -0.09599897218294122, -0.0985470908713026, -0.0998378654067105, -0.09983786540671051, -0.0985470908713026, -0.09599897218294123, -0.09225950427718976, -0.08742553740855508, -0.08162226877976886, -0.07499999999999998, -0.06773024435212681, -0.060001284688802226, -0.05201329700547076, -0.043973165987233886, -0.0360891268041774, -0.028565371929847313, -0.021596762663442223, -0.015363782324520037, -0.010027861829824942, -0.0057271987173395, -0.0025731779026427204, -0.0006474868681043578, 0.0],
        },
        "q1.I.x180_DragCosine.wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.0012949737362087156, 0.005146355805285452, 0.01145439743467901, 0.020055723659649884, 0.030727564649040064, 0.04319352532688441, 0.05713074385969458, 0.07217825360835473, 0.0879463319744677, 0.10402659401094153, 0.12000256937760441, 0.13546048870425356, 0.15000000000000002, 0.16324453755953772, 0.1748510748171101, 0.18451900855437947, 0.19199794436588244, 0.1970941817426052, 0.199675730813421, 0.19967573081342102, 0.1970941817426052, 0.19199794436588247, 0.18451900855437953, 0.17485107481711015, 0.16324453755953772, 0.14999999999999997, 0.13546048870425362, 0.12000256937760445, 0.10402659401094153, 0.08794633197446777, 0.0721782536083548, 0.057130743859694626, 0.04319352532688445, 0.030727564649040074, 0.020055723659649884, 0.011454397434679, 0.005146355805285441, 0.0012949737362087156, 0.0],
        },
        "q1.I.x90_DragCosine.wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.0006474865235251675, 0.0025731765421745604, 0.00572719572252497, 0.010027856668006575, 0.015363774578439817, 0.02159675205631711, 0.028565358344901863, 0.036089110297807266, 0.04397314679519682, 0.05201327554174647, 0.06000126153702194, 0.06773022024973922, 0.07499997581560172, 0.0816222454842792, 0.08742551604114582, 0.09225948590708327, 0.0959989578683585, 0.0985470816169707, 0.09983786212142061, 0.09983786886245094, 0.0985471016654741, 0.09599899070509398, 0.09225953068160411, 0.08742557159382541, 0.08162231037634414, 0.07500004836639468, 0.06773029858024633, 0.060001343618537185, 0.0520133592484133, 0.04397322995906577, 0.036089190764983514, 0.028565434031329072, 0.021596821001752402, 0.015363834997222079, 0.010027906995303338, 0.005727234654859972, 0.0025732030711865103, 0.0006474999620832822, 2.051915953781308e-23],
        },
        "q1.I.x180_Square.wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "q1.I.x90_Square.wf": {
            "type": "constant",
            "sample": 0.05,
        },
        "q1.I.saturation.wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "q1.Q.x180_Cosine.wf": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q1.Q.x90_Cosine.wf": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q1.Q.-x90_Cosine.wf": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q1.Q.x180_DragCosine.wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.002742073177055731, 0.005413128099170471, 0.007943985846902028, 0.010269098533982546, 0.012328246963142131, 0.014068100271686437, 0.015443597172827051, 0.0164191130193397, 0.016969382463214604, 0.01708015381489863, 0.016748558154568684, 0.015983183635648122, 0.014803853056144253, 0.013241110458592388, 0.011335430055398216, 0.009136167967996604, 0.0067002839292320555, 0.004090866056197569, 0.0013754969011406171, -0.001375496901140613, -0.004090866056197572, -0.006700283929232043, -0.009136167967996597, -0.011335430055398207, -0.013241110458592392, -0.014803853056144256, -0.01598318363564812, -0.016748558154568684, -0.01708015381489863, -0.016969382463214604, -0.016419113019339703, -0.015443597172827055, -0.01406810027168644, -0.012328246963142131, -0.010269098533982548, -0.007943985846902027, -0.005413128099170466, -0.002742073177055738, -4.186826663751637e-18],
        },
        "q1.Q.x90_DragCosine.wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.0013710371168688756, 0.0027065660647557863, 0.00397199830085438, 0.005134560717308439, 0.006164144432031172, 0.007034084578733267, 0.007721850900375471, 0.008209631260363719, 0.008484792959128686, 0.0085402099084502, 0.008374447190037784, 0.007991798218483993, 0.007402173546107199, 0.0066208441895274405, 0.005668046125561179, 0.0045684561995969234, 0.0033505530199023133, 0.002045879390062873, 0.0006882253818169591, -0.000687246794114037, -0.0020449134542271726, -0.003349612060124502, -0.00456755189320125, -0.005667189200569045, -0.006620044146807444, -0.007401438413307741, -0.007991134342121528, -0.00837385907112546, -0.008539700085924046, -0.008484361944090534, -0.008209277522843944, -0.007721570908958379, -0.007033872892018857, -0.006163993839564462, -0.005134462426326372, -0.0039719421640136325, -0.0027065408429435014, -0.0013710307702896325, -2.09341389001896e-18],
        },
        "q1.Q.x180_Square.wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "q1.Q.x90_Square.wf": {
            "type": "constant",
            "sample": 0.05,
        },
        "q1.Q.saturation.wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "q1.z.const.wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "q1.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.001,
        },
        "q1.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q1.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.001,
        },
        "q1.resonator.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.I.x180_Cosine.wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.0005892606843622562, 0.0023417811952484336, 0.005212172171983234, 0.009126091996016224, 0.013982172199792415, 0.019654642856815535, 0.025996589956680406, 0.03284376040077201, 0.04001881607124151, 0.04733592679510702, 0.05460558324812178, 0.06163950514672756, 0.06825551760849956, 0.07428226938590929, 0.07956367077362887, 0.08396293624990885, 0.08736612714974136, 0.08968510261643467, 0.09085980240350315, 0.09085980240350316, 0.08968510261643467, 0.08736612714974137, 0.08396293624990886, 0.07956367077362889, 0.07428226938590929, 0.06825551760849953, 0.06163950514672757, 0.0546055832481218, 0.04733592679510702, 0.040018816071241546, 0.03284376040077205, 0.025996589956680426, 0.01965464285681555, 0.01398217219979242, 0.009126091996016224, 0.00521217217198323, 0.0023417811952484288, 0.0005892606843622562, 0.0],
        },
        "q2.I.x90_Cosine.wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.0002946303421811281, 0.0011708905976242168, 0.002606086085991617, 0.004563045998008112, 0.006991086099896207, 0.009827321428407768, 0.012998294978340203, 0.016421880200386006, 0.020009408035620756, 0.02366796339755351, 0.02730279162406089, 0.03081975257336378, 0.03412775880424978, 0.037141134692954644, 0.039781835386814436, 0.04198146812495442, 0.04368306357487068, 0.044842551308217335, 0.045429901201751575, 0.04542990120175158, 0.044842551308217335, 0.04368306357487069, 0.04198146812495443, 0.03978183538681444, 0.037141134692954644, 0.034127758804249765, 0.030819752573363786, 0.0273027916240609, 0.02366796339755351, 0.020009408035620773, 0.016421880200386024, 0.012998294978340213, 0.009827321428407775, 0.00699108609989621, 0.004563045998008112, 0.002606086085991615, 0.0011708905976242144, 0.0002946303421811281, 0.0],
        },
        "q2.I.-x90_Cosine.wf": {
            "type": "arbitrary",
            "samples": [0.0, -0.0006474868681043578, -0.002573177902642726, -0.005727198717339505, -0.010027861829824942, -0.015363782324520032, -0.021596762663442206, -0.02856537192984729, -0.03608912680417736, -0.04397316598723385, -0.05201329700547076, -0.060001284688802205, -0.06773024435212678, -0.07500000000000001, -0.08162226877976886, -0.08742553740855505, -0.09225950427718974, -0.09599897218294122, -0.0985470908713026, -0.0998378654067105, -0.09983786540671051, -0.0985470908713026, -0.09599897218294123, -0.09225950427718976, -0.08742553740855508, -0.08162226877976886, -0.07499999999999998, -0.06773024435212681, -0.060001284688802226, -0.05201329700547076, -0.043973165987233886, -0.0360891268041774, -0.028565371929847313, -0.021596762663442223, -0.015363782324520037, -0.010027861829824942, -0.0057271987173395, -0.0025731779026427204, -0.0006474868681043578, 0.0],
        },
        "q2.I.x180_DragCosine.wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.0012949737362087156, 0.005146355805285452, 0.01145439743467901, 0.020055723659649884, 0.030727564649040064, 0.04319352532688441, 0.05713074385969458, 0.07217825360835473, 0.0879463319744677, 0.10402659401094153, 0.12000256937760441, 0.13546048870425356, 0.15000000000000002, 0.16324453755953772, 0.1748510748171101, 0.18451900855437947, 0.19199794436588244, 0.1970941817426052, 0.199675730813421, 0.19967573081342102, 0.1970941817426052, 0.19199794436588247, 0.18451900855437953, 0.17485107481711015, 0.16324453755953772, 0.14999999999999997, 0.13546048870425362, 0.12000256937760445, 0.10402659401094153, 0.08794633197446777, 0.0721782536083548, 0.057130743859694626, 0.04319352532688445, 0.030727564649040074, 0.020055723659649884, 0.011454397434679, 0.005146355805285441, 0.0012949737362087156, 0.0],
        },
        "q2.I.x90_DragCosine.wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.0006474865235251675, 0.0025731765421745604, 0.00572719572252497, 0.010027856668006575, 0.015363774578439817, 0.02159675205631711, 0.028565358344901863, 0.036089110297807266, 0.04397314679519682, 0.05201327554174647, 0.06000126153702194, 0.06773022024973922, 0.07499997581560172, 0.0816222454842792, 0.08742551604114582, 0.09225948590708327, 0.0959989578683585, 0.0985470816169707, 0.09983786212142061, 0.09983786886245094, 0.0985471016654741, 0.09599899070509398, 0.09225953068160411, 0.08742557159382541, 0.08162231037634414, 0.07500004836639468, 0.06773029858024633, 0.060001343618537185, 0.0520133592484133, 0.04397322995906577, 0.036089190764983514, 0.028565434031329072, 0.021596821001752402, 0.015363834997222079, 0.010027906995303338, 0.005727234654859972, 0.0025732030711865103, 0.0006474999620832822, 2.051915953781308e-23],
        },
        "q2.I.x180_Square.wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "q2.I.x90_Square.wf": {
            "type": "constant",
            "sample": 0.05,
        },
        "q2.I.saturation.wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "q2.Q.x180_Cosine.wf": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q2.Q.x90_Cosine.wf": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q2.Q.-x90_Cosine.wf": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q2.Q.x180_DragCosine.wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.002742073177055731, 0.005413128099170471, 0.007943985846902028, 0.010269098533982546, 0.012328246963142131, 0.014068100271686437, 0.015443597172827051, 0.0164191130193397, 0.016969382463214604, 0.01708015381489863, 0.016748558154568684, 0.015983183635648122, 0.014803853056144253, 0.013241110458592388, 0.011335430055398216, 0.009136167967996604, 0.0067002839292320555, 0.004090866056197569, 0.0013754969011406171, -0.001375496901140613, -0.004090866056197572, -0.006700283929232043, -0.009136167967996597, -0.011335430055398207, -0.013241110458592392, -0.014803853056144256, -0.01598318363564812, -0.016748558154568684, -0.01708015381489863, -0.016969382463214604, -0.016419113019339703, -0.015443597172827055, -0.01406810027168644, -0.012328246963142131, -0.010269098533982548, -0.007943985846902027, -0.005413128099170466, -0.002742073177055738, -4.186826663751637e-18],
        },
        "q2.Q.x90_DragCosine.wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.0013710371168688756, 0.0027065660647557863, 0.00397199830085438, 0.005134560717308439, 0.006164144432031172, 0.007034084578733267, 0.007721850900375471, 0.008209631260363719, 0.008484792959128686, 0.0085402099084502, 0.008374447190037784, 0.007991798218483993, 0.007402173546107199, 0.0066208441895274405, 0.005668046125561179, 0.0045684561995969234, 0.0033505530199023133, 0.002045879390062873, 0.0006882253818169591, -0.000687246794114037, -0.0020449134542271726, -0.003349612060124502, -0.00456755189320125, -0.005667189200569045, -0.006620044146807444, -0.007401438413307741, -0.007991134342121528, -0.00837385907112546, -0.008539700085924046, -0.008484361944090534, -0.008209277522843944, -0.007721570908958379, -0.007033872892018857, -0.006163993839564462, -0.005134462426326372, -0.0039719421640136325, -0.0027065408429435014, -0.0013710307702896325, -2.09341389001896e-18],
        },
        "q2.Q.x180_Square.wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "q2.Q.x90_Square.wf": {
            "type": "constant",
            "sample": 0.05,
        },
        "q2.Q.saturation.wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "q2.z.const.wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "q2.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.001,
        },
        "q2.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.001,
        },
        "q2.resonator.const.wf.Q": {
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
            "cosine": [(1.0, 2500)],
            "sine": [(-0.0, 2500)],
        },
        "q1.resonator.readout.iw2": {
            "cosine": [(0.0, 2500)],
            "sine": [(1.0, 2500)],
        },
        "q1.resonator.readout.iw3": {
            "cosine": [(-0.0, 2500)],
            "sine": [(-1.0, 2500)],
        },
        "q2.resonator.readout.iw1": {
            "cosine": [(1.0, 2500)],
            "sine": [(-0.0, 2500)],
        },
        "q2.resonator.readout.iw2": {
            "cosine": [(0.0, 2500)],
            "sine": [(1.0, 2500)],
        },
        "q2.resonator.readout.iw3": {
            "cosine": [(-0.0, 2500)],
            "sine": [(-1.0, 2500)],
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
                "3": {
                    "type": "LF",
                    "analog_outputs": {
                        "5": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
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
                                "exponential": [],
                                "high_pass": None,
                            },
                            "crosstalk": {},
                            "output_mode": "amplified",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                        },
                        "2": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
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
                                "exponential": [],
                                "high_pass": None,
                            },
                            "crosstalk": {},
                            "output_mode": "amplified",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                        },
                        "4": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
                            },
                            "crosstalk": {},
                            "output_mode": "amplified",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
                        },
                    },
                },
                "2": {
                    "type": "MW",
                    "analog_outputs": {
                        "2": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 4,
                            "band": 1,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 4200000000.0,
                                },
                            },
                        },
                        "1": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 4,
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 7300000000.0,
                                },
                            },
                        },
                    },
                    "analog_inputs": {
                        "1": {
                            "band": 2,
                            "shareable": False,
                            "gain_db": 0,
                            "sampling_rate": 1000000000.0,
                            "downconverter_frequency": 7300000000.0,
                        },
                    },
                },
            },
        },
    },
    "oscillators": {},
    "elements": {
        "c12.xy": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "x180_DragCosine": "c12.xy.x180_DragCosine.pulse",
                "x90_DragCosine": "c12.xy.x90_DragCosine.pulse",
                "-x90_DragCosine": "c12.xy.-x90_DragCosine.pulse",
                "y180_DragCosine": "c12.xy.y180_DragCosine.pulse",
                "y90_DragCosine": "c12.xy.y90_DragCosine.pulse",
                "-y90_DragCosine": "c12.xy.-y90_DragCosine.pulse",
                "x180_Square": "c12.xy.x180_Square.pulse",
                "x90_Square": "c12.xy.x90_Square.pulse",
                "-x90_Square": "c12.xy.-x90_Square.pulse",
                "y180_Square": "c12.xy.y180_Square.pulse",
                "y90_Square": "c12.xy.y90_Square.pulse",
                "-y90_Square": "c12.xy.-y90_Square.pulse",
                "x180": "c12.xy.x180_DragCosine.pulse",
                "x90": "c12.xy.x90_DragCosine.pulse",
                "-x90": "c12.xy.-x90_DragCosine.pulse",
                "y180": "c12.xy.y180_DragCosine.pulse",
                "y90": "c12.xy.y90_DragCosine.pulse",
                "-y90": "c12.xy.-y90_DragCosine.pulse",
                "saturation": "c12.xy.saturation.pulse",
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
            "intermediate_frequency": -200000000.0,
        },
        "c12.z": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "c12.z.const.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 3, 5),
            },
        },
        "q1.I": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "x180_Cosine": "q1.I.x180_Cosine.pulse",
                "x90_Cosine": "q1.I.x90_Cosine.pulse",
                "-x90_Cosine": "q1.I.-x90_Cosine.pulse",
                "x180_DragCosine": "q1.I.x180_DragCosine.pulse",
                "x90_DragCosine": "q1.I.x90_DragCosine.pulse",
                "x180_Square": "q1.I.x180_Square.pulse",
                "x90_Square": "q1.I.x90_Square.pulse",
                "saturation": "q1.I.saturation.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 3, 1),
            },
            "intermediate_frequency": 100000000.0,
        },
        "q1.Q": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "x180_Cosine": "q1.Q.x180_Cosine.pulse",
                "x90_Cosine": "q1.Q.x90_Cosine.pulse",
                "-x90_Cosine": "q1.Q.-x90_Cosine.pulse",
                "x180_DragCosine": "q1.Q.x180_DragCosine.pulse",
                "x90_DragCosine": "q1.Q.x90_DragCosine.pulse",
                "x180_Square": "q1.Q.x180_Square.pulse",
                "x90_Square": "q1.Q.x90_Square.pulse",
                "saturation": "q1.Q.saturation.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 3, 1),
            },
            "intermediate_frequency": 100000000.0,
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
            "singleInput": {
                "port": ('con1', 3, 2),
            },
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
                "port": ('con1', 2, 1),
                "upconverter": 1,
            },
            "MWOutput": {
                "port": ('con1', 2, 1),
            },
            "smearing": 0,
            "time_of_flight": 28,
            "intermediate_frequency": -283814266.0,
        },
        "q2.I": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "x180_Cosine": "q2.I.x180_Cosine.pulse",
                "x90_Cosine": "q2.I.x90_Cosine.pulse",
                "-x90_Cosine": "q2.I.-x90_Cosine.pulse",
                "x180_DragCosine": "q2.I.x180_DragCosine.pulse",
                "x90_DragCosine": "q2.I.x90_DragCosine.pulse",
                "x180_Square": "q2.I.x180_Square.pulse",
                "x90_Square": "q2.I.x90_Square.pulse",
                "saturation": "q2.I.saturation.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 3, 3),
            },
            "intermediate_frequency": 200000000.0,
        },
        "q2.Q": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "x180_Cosine": "q2.Q.x180_Cosine.pulse",
                "x90_Cosine": "q2.Q.x90_Cosine.pulse",
                "-x90_Cosine": "q2.Q.-x90_Cosine.pulse",
                "x180_DragCosine": "q2.Q.x180_DragCosine.pulse",
                "x90_DragCosine": "q2.Q.x90_DragCosine.pulse",
                "x180_Square": "q2.Q.x180_Square.pulse",
                "x90_Square": "q2.Q.x90_Square.pulse",
                "saturation": "q2.Q.saturation.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 3, 3),
            },
            "intermediate_frequency": 200000000.0,
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
            "singleInput": {
                "port": ('con1', 3, 4),
            },
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
                "port": ('con1', 2, 1),
                "upconverter": 1,
            },
            "MWOutput": {
                "port": ('con1', 2, 1),
            },
            "smearing": 0,
            "time_of_flight": 28,
            "intermediate_frequency": -216721946.0,
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
        "c12.xy.x180_DragCosine.pulse": {
            "length": 32,
            "waveforms": {
                "I": "c12.xy.x180_DragCosine.wf.I",
                "Q": "c12.xy.x180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "c12.xy.x90_DragCosine.pulse": {
            "length": 32,
            "waveforms": {
                "I": "c12.xy.x90_DragCosine.wf.I",
                "Q": "c12.xy.x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "c12.xy.-x90_DragCosine.pulse": {
            "length": 32,
            "waveforms": {
                "I": "c12.xy.-x90_DragCosine.wf.I",
                "Q": "c12.xy.-x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "c12.xy.y180_DragCosine.pulse": {
            "length": 32,
            "waveforms": {
                "I": "c12.xy.y180_DragCosine.wf.I",
                "Q": "c12.xy.y180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "c12.xy.y90_DragCosine.pulse": {
            "length": 32,
            "waveforms": {
                "I": "c12.xy.y90_DragCosine.wf.I",
                "Q": "c12.xy.y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "c12.xy.-y90_DragCosine.pulse": {
            "length": 32,
            "waveforms": {
                "I": "c12.xy.-y90_DragCosine.wf.I",
                "Q": "c12.xy.-y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "c12.xy.x180_Square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "c12.xy.x180_Square.wf.I",
                "Q": "c12.xy.x180_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "c12.xy.x90_Square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "c12.xy.x90_Square.wf.I",
                "Q": "c12.xy.x90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "c12.xy.-x90_Square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "c12.xy.-x90_Square.wf.I",
                "Q": "c12.xy.-x90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "c12.xy.y180_Square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "c12.xy.y180_Square.wf.I",
                "Q": "c12.xy.y180_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "c12.xy.y90_Square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "c12.xy.y90_Square.wf.I",
                "Q": "c12.xy.y90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "c12.xy.-y90_Square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "c12.xy.-y90_Square.wf.I",
                "Q": "c12.xy.-y90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "c12.xy.saturation.pulse": {
            "length": 20000,
            "waveforms": {
                "I": "c12.xy.saturation.wf.I",
                "Q": "c12.xy.saturation.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "c12.z.const.pulse": {
            "length": 100,
            "waveforms": {
                "single": "c12.z.const.wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q1.I.x180_Cosine.pulse": {
            "length": 40,
            "waveforms": {
                "single": "q1.I.x180_Cosine.wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.I.x90_Cosine.pulse": {
            "length": 40,
            "waveforms": {
                "single": "q1.I.x90_Cosine.wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.I.-x90_Cosine.pulse": {
            "length": 40,
            "waveforms": {
                "single": "q1.I.-x90_Cosine.wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.I.x180_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "single": "q1.I.x180_DragCosine.wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.I.x90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "single": "q1.I.x90_DragCosine.wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.I.x180_Square.pulse": {
            "length": 40,
            "waveforms": {
                "single": "q1.I.x180_Square.wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.I.x90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "single": "q1.I.x90_Square.wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.I.saturation.pulse": {
            "length": 20000,
            "waveforms": {
                "single": "q1.I.saturation.wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.Q.x180_Cosine.pulse": {
            "length": 40,
            "waveforms": {
                "single": "q1.Q.x180_Cosine.wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.Q.x90_Cosine.pulse": {
            "length": 40,
            "waveforms": {
                "single": "q1.Q.x90_Cosine.wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.Q.-x90_Cosine.pulse": {
            "length": 40,
            "waveforms": {
                "single": "q1.Q.-x90_Cosine.wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.Q.x180_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "single": "q1.Q.x180_DragCosine.wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.Q.x90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "single": "q1.Q.x90_DragCosine.wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.Q.x180_Square.pulse": {
            "length": 40,
            "waveforms": {
                "single": "q1.Q.x180_Square.wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.Q.x90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "single": "q1.Q.x90_Square.wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.Q.saturation.pulse": {
            "length": 20000,
            "waveforms": {
                "single": "q1.Q.saturation.wf",
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
            "length": 2500,
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
            "length": 2500,
            "waveforms": {
                "I": "q1.resonator.const.wf.I",
                "Q": "q1.resonator.const.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q2.I.x180_Cosine.pulse": {
            "length": 40,
            "waveforms": {
                "single": "q2.I.x180_Cosine.wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.I.x90_Cosine.pulse": {
            "length": 40,
            "waveforms": {
                "single": "q2.I.x90_Cosine.wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.I.-x90_Cosine.pulse": {
            "length": 40,
            "waveforms": {
                "single": "q2.I.-x90_Cosine.wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.I.x180_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "single": "q2.I.x180_DragCosine.wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.I.x90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "single": "q2.I.x90_DragCosine.wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.I.x180_Square.pulse": {
            "length": 40,
            "waveforms": {
                "single": "q2.I.x180_Square.wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.I.x90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "single": "q2.I.x90_Square.wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.I.saturation.pulse": {
            "length": 20000,
            "waveforms": {
                "single": "q2.I.saturation.wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.Q.x180_Cosine.pulse": {
            "length": 40,
            "waveforms": {
                "single": "q2.Q.x180_Cosine.wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.Q.x90_Cosine.pulse": {
            "length": 40,
            "waveforms": {
                "single": "q2.Q.x90_Cosine.wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.Q.-x90_Cosine.pulse": {
            "length": 40,
            "waveforms": {
                "single": "q2.Q.-x90_Cosine.wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.Q.x180_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "single": "q2.Q.x180_DragCosine.wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.Q.x90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "single": "q2.Q.x90_DragCosine.wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.Q.x180_Square.pulse": {
            "length": 40,
            "waveforms": {
                "single": "q2.Q.x180_Square.wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.Q.x90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "single": "q2.Q.x90_Square.wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.Q.saturation.pulse": {
            "length": 20000,
            "waveforms": {
                "single": "q2.Q.saturation.wf",
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
            "length": 2500,
            "waveforms": {
                "I": "q2.resonator.const.wf.I",
                "Q": "q2.resonator.const.wf.Q",
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
        "c12.xy.x180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0010235029373752758, 0.00405210941898847, 0.008961827939636185, 0.015551654046215668, 0.02355179948365188, 0.032634737357758986, 0.04242861112477117, 0.05253245844193564, 0.06253262661293602, 0.07201970757788172, 0.08060529912738312, 0.08793790613463955, 0.0937173308072291, 0.09770696282000245] + [0.09974346616959476] * 2 + [0.09770696282000245, 0.0937173308072291, 0.08793790613463956, 0.08060529912738314, 0.07201970757788172, 0.06253262661293606, 0.05253245844193569, 0.04242861112477117, 0.032634737357758986, 0.02355179948365188, 0.015551654046215675, 0.008961827939636185, 0.00405210941898847, 0.001023502937375287, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "c12.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 32,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "c12.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0005117514686876379, 0.002026054709494235, 0.004480913969818093, 0.007775827023107834, 0.01177589974182594, 0.016317368678879493, 0.021214305562385585, 0.02626622922096782, 0.03126631330646801, 0.03600985378894086, 0.04030264956369156, 0.04396895306731977, 0.04685866540361455, 0.048853481410001225] + [0.04987173308479738] * 2 + [0.048853481410001225, 0.04685866540361455, 0.04396895306731978, 0.04030264956369157, 0.03600985378894086, 0.03126631330646803, 0.026266229220967843, 0.021214305562385585, 0.016317368678879493, 0.01177589974182594, 0.007775827023107838, 0.004480913969818093, 0.002026054709494235, 0.0005117514686876435, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "c12.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 32,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "c12.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0005117514686876379, -0.002026054709494235, -0.004480913969818093, -0.007775827023107834, -0.01177589974182594, -0.016317368678879493, -0.021214305562385585, -0.02626622922096782, -0.03126631330646801, -0.03600985378894086, -0.04030264956369156, -0.04396895306731977, -0.04685866540361455, -0.048853481410001225] + [-0.04987173308479738] * 2 + [-0.048853481410001225, -0.04685866540361455, -0.04396895306731978, -0.04030264956369157, -0.03600985378894086, -0.03126631330646803, -0.026266229220967843, -0.021214305562385585, -0.016317368678879493, -0.01177589974182594, -0.007775827023107838, -0.004480913969818093, -0.002026054709494235, -0.0005117514686876435, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "c12.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 6.267147980872727e-20, 2.481201414879535e-19, 5.487536950392387e-19, 9.522641674572502e-19, 1.442131792590728e-18, 1.9983013323097046e-18, 2.59800314031094e-18, 3.2166853541128915e-18, 3.829019051190435e-18, 4.409935218039061e-18, 4.935651078533234e-18, 5.384643763575336e-18, 5.738531459885338e-18, 5.982825963596272e-18] + [6.107525829022826e-18] * 2 + [5.982825963596272e-18, 5.738531459885338e-18, 5.384643763575337e-18, 4.9356510785332354e-18, 4.409935218039061e-18, 3.829019051190437e-18, 3.2166853541128946e-18, 2.59800314031094e-18, 1.9983013323097046e-18, 1.442131792590728e-18, 9.522641674572505e-19, 5.487536950392387e-19, 2.481201414879535e-19, 6.267147980872795e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "c12.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 6.267147980872727e-20, 2.481201414879535e-19, 5.487536950392387e-19, 9.522641674572502e-19, 1.442131792590728e-18, 1.9983013323097046e-18, 2.59800314031094e-18, 3.2166853541128915e-18, 3.829019051190435e-18, 4.409935218039061e-18, 4.935651078533234e-18, 5.384643763575336e-18, 5.738531459885338e-18, 5.982825963596272e-18] + [6.107525829022826e-18] * 2 + [5.982825963596272e-18, 5.738531459885338e-18, 5.384643763575337e-18, 4.9356510785332354e-18, 4.409935218039061e-18, 3.829019051190437e-18, 3.2166853541128946e-18, 2.59800314031094e-18, 1.9983013323097046e-18, 1.442131792590728e-18, 9.522641674572505e-19, 5.487536950392387e-19, 2.481201414879535e-19, 6.267147980872795e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "c12.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0010235029373752758, 0.00405210941898847, 0.008961827939636185, 0.015551654046215668, 0.02355179948365188, 0.032634737357758986, 0.04242861112477117, 0.05253245844193564, 0.06253262661293602, 0.07201970757788172, 0.08060529912738312, 0.08793790613463955, 0.0937173308072291, 0.09770696282000245] + [0.09974346616959476] * 2 + [0.09770696282000245, 0.0937173308072291, 0.08793790613463956, 0.08060529912738314, 0.07201970757788172, 0.06253262661293606, 0.05253245844193569, 0.04242861112477117, 0.032634737357758986, 0.02355179948365188, 0.015551654046215675, 0.008961827939636185, 0.00405210941898847, 0.001023502937375287, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "c12.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 3.1335739904363637e-20, 1.2406007074397676e-19, 2.7437684751961936e-19, 4.761320837286251e-19, 7.21065896295364e-19, 9.991506661548523e-19, 1.29900157015547e-18, 1.6083426770564457e-18, 1.9145095255952173e-18, 2.2049676090195304e-18, 2.467825539266617e-18, 2.692321881787668e-18, 2.869265729942669e-18, 2.991412981798136e-18] + [3.053762914511413e-18] * 2 + [2.991412981798136e-18, 2.869265729942669e-18, 2.6923218817876684e-18, 2.4678255392666177e-18, 2.2049676090195304e-18, 1.9145095255952185e-18, 1.6083426770564473e-18, 1.29900157015547e-18, 9.991506661548523e-19, 7.21065896295364e-19, 4.761320837286253e-19, 2.7437684751961936e-19, 1.2406007074397676e-19, 3.1335739904363974e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "c12.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0005117514686876379, 0.002026054709494235, 0.004480913969818093, 0.007775827023107834, 0.01177589974182594, 0.016317368678879493, 0.021214305562385585, 0.02626622922096782, 0.03126631330646801, 0.03600985378894086, 0.04030264956369156, 0.04396895306731977, 0.04685866540361455, 0.048853481410001225] + [0.04987173308479738] * 2 + [0.048853481410001225, 0.04685866540361455, 0.04396895306731978, 0.04030264956369157, 0.03600985378894086, 0.03126631330646803, 0.026266229220967843, 0.021214305562385585, 0.016317368678879493, 0.01177589974182594, 0.007775827023107838, 0.004480913969818093, 0.002026054709494235, 0.0005117514686876435, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "c12.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 3.1335739904363637e-20, 1.2406007074397676e-19, 2.7437684751961936e-19, 4.761320837286251e-19, 7.21065896295364e-19, 9.991506661548523e-19, 1.29900157015547e-18, 1.6083426770564457e-18, 1.9145095255952173e-18, 2.2049676090195304e-18, 2.467825539266617e-18, 2.692321881787668e-18, 2.869265729942669e-18, 2.991412981798136e-18] + [3.053762914511413e-18] * 2 + [2.991412981798136e-18, 2.869265729942669e-18, 2.6923218817876684e-18, 2.4678255392666177e-18, 2.2049676090195304e-18, 1.9145095255952185e-18, 1.6083426770564473e-18, 1.29900157015547e-18, 9.991506661548523e-19, 7.21065896295364e-19, 4.761320837286253e-19, 2.7437684751961936e-19, 1.2406007074397676e-19, 3.1335739904363974e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "c12.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0005117514686876379, -0.002026054709494235, -0.004480913969818093, -0.007775827023107834, -0.01177589974182594, -0.016317368678879493, -0.021214305562385585, -0.02626622922096782, -0.03126631330646801, -0.03600985378894086, -0.04030264956369156, -0.04396895306731977, -0.04685866540361455, -0.048853481410001225] + [-0.04987173308479738] * 2 + [-0.048853481410001225, -0.04685866540361455, -0.04396895306731978, -0.04030264956369157, -0.03600985378894086, -0.03126631330646803, -0.026266229220967843, -0.021214305562385585, -0.016317368678879493, -0.01177589974182594, -0.007775827023107838, -0.004480913969818093, -0.002026054709494235, -0.0005117514686876435, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "c12.xy.x180_Square.wf.I": {
            "type": "constant",
            "sample": 0.25,
        },
        "c12.xy.x180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "c12.xy.x90_Square.wf.I": {
            "type": "constant",
            "sample": 0.125,
        },
        "c12.xy.x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "c12.xy.-x90_Square.wf.I": {
            "type": "constant",
            "sample": -0.125,
        },
        "c12.xy.-x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "c12.xy.y180_Square.wf.I": {
            "type": "constant",
            "sample": -0.11201840403229253,
        },
        "c12.xy.y180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.22349916590013946,
        },
        "c12.xy.y90_Square.wf.I": {
            "type": "constant",
            "sample": -0.056009202016146266,
        },
        "c12.xy.y90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.11174958295006973,
        },
        "c12.xy.-y90_Square.wf.I": {
            "type": "constant",
            "sample": 0.056009202016146266,
        },
        "c12.xy.-y90_Square.wf.Q": {
            "type": "constant",
            "sample": -0.11174958295006973,
        },
        "c12.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.25,
        },
        "c12.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "c12.z.const.wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "q1.I.x180_Cosine.wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.0008622917500937984, 0.0034268340969887735, 0.0076272067409924385, 0.013354622236979315, 0.020460743532076248, 0.028761525817413945, 0.03804198319200245, 0.04806175668463981, 0.05856133942501153, 0.06926879773531897, 0.07990681406969413, 0.0901998693929696, 0.09988137897896564, 0.10870059681486784, 0.1164291097912483, 0.12286675348161984, 0.1278467962959404, 0.13124025774121517, 0.13295924894851482, 0.13295924894851485, 0.13124025774121517, 0.12784679629594042, 0.12286675348161986, 0.11642910979124833, 0.10870059681486784, 0.0998813789789656, 0.09019986939296964, 0.07990681406969417, 0.06926879773531897, 0.058561339425011585, 0.048061756684639856, 0.03804198319200248, 0.028761525817413966, 0.020460743532076255, 0.013354622236979315, 0.007627206740992431, 0.003426834096988766, 0.0008622917500937984, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.I.x90_Cosine.wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.0004311458750468992, 0.0017134170484943867, 0.0038136033704962193, 0.006677311118489657, 0.010230371766038124, 0.014380762908706973, 0.019020991596001225, 0.024030878342319904, 0.029280669712505765, 0.03463439886765948, 0.039953407034847066, 0.0450999346964848, 0.04994068948948282, 0.05435029840743392, 0.05821455489562415, 0.06143337674080992, 0.0639233981479702, 0.06562012887060759, 0.06647962447425741, 0.06647962447425743, 0.06562012887060759, 0.06392339814797021, 0.06143337674080993, 0.05821455489562417, 0.05435029840743392, 0.0499406894894828, 0.04509993469648482, 0.03995340703484709, 0.03463439886765948, 0.029280669712505793, 0.024030878342319928, 0.01902099159600124, 0.014380762908706983, 0.010230371766038127, 0.006677311118489657, 0.0038136033704962153, 0.001713417048494383, 0.0004311458750468992, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.I.-x90_Cosine.wf": {
            "type": "arbitrary",
            "samples": [0.0, -0.0006474868681043578, -0.002573177902642726, -0.005727198717339505, -0.010027861829824942, -0.015363782324520032, -0.021596762663442206, -0.02856537192984729, -0.03608912680417736, -0.04397316598723385, -0.05201329700547076, -0.060001284688802205, -0.06773024435212678, -0.07500000000000001, -0.08162226877976886, -0.08742553740855505, -0.09225950427718974, -0.09599897218294122, -0.0985470908713026, -0.0998378654067105, -0.09983786540671051, -0.0985470908713026, -0.09599897218294123, -0.09225950427718976, -0.08742553740855508, -0.08162226877976886, -0.07499999999999998, -0.06773024435212681, -0.060001284688802226, -0.05201329700547076, -0.043973165987233886, -0.0360891268041774, -0.028565371929847313, -0.021596762663442223, -0.015363782324520037, -0.010027861829824942, -0.0057271987173395, -0.0025731779026427204, -0.0006474868681043578, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.I.x180_DragCosine.wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.0012949737362087156, 0.005146355805285452, 0.01145439743467901, 0.020055723659649884, 0.030727564649040064, 0.04319352532688441, 0.05713074385969458, 0.07217825360835473, 0.0879463319744677, 0.10402659401094153, 0.12000256937760441, 0.13546048870425356, 0.15000000000000002, 0.16324453755953772, 0.1748510748171101, 0.18451900855437947, 0.19199794436588244, 0.1970941817426052, 0.199675730813421, 0.19967573081342102, 0.1970941817426052, 0.19199794436588247, 0.18451900855437953, 0.17485107481711015, 0.16324453755953772, 0.14999999999999997, 0.13546048870425362, 0.12000256937760445, 0.10402659401094153, 0.08794633197446777, 0.0721782536083548, 0.057130743859694626, 0.04319352532688445, 0.030727564649040074, 0.020055723659649884, 0.011454397434679, 0.005146355805285441, 0.0012949737362087156, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.I.x90_DragCosine.wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.0006474865235251675, 0.0025731765421745604, 0.00572719572252497, 0.010027856668006575, 0.015363774578439817, 0.02159675205631711, 0.028565358344901863, 0.036089110297807266, 0.04397314679519682, 0.05201327554174647, 0.06000126153702194, 0.06773022024973922, 0.07499997581560172, 0.0816222454842792, 0.08742551604114582, 0.09225948590708327, 0.0959989578683585, 0.0985470816169707, 0.09983786212142061, 0.09983786886245094, 0.0985471016654741, 0.09599899070509398, 0.09225953068160411, 0.08742557159382541, 0.08162231037634414, 0.07500004836639468, 0.06773029858024633, 0.060001343618537185, 0.0520133592484133, 0.04397322995906577, 0.036089190764983514, 0.028565434031329072, 0.021596821001752402, 0.015363834997222079, 0.010027906995303338, 0.005727234654859972, 0.0025732030711865103, 0.0006474999620832822, 2.051915953781308e-23],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.I.x180_Square.wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "q1.I.x90_Square.wf": {
            "type": "constant",
            "sample": 0.05,
        },
        "q1.I.saturation.wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "q1.Q.x180_Cosine.wf": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.Q.x90_Cosine.wf": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.Q.-x90_Cosine.wf": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.Q.x180_DragCosine.wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.002742073177055731, 0.005413128099170471, 0.007943985846902028, 0.010269098533982546, 0.012328246963142131, 0.014068100271686437, 0.015443597172827051, 0.0164191130193397, 0.016969382463214604, 0.01708015381489863, 0.016748558154568684, 0.015983183635648122, 0.014803853056144253, 0.013241110458592388, 0.011335430055398216, 0.009136167967996604, 0.0067002839292320555, 0.004090866056197569, 0.0013754969011406171, -0.001375496901140613, -0.004090866056197572, -0.006700283929232043, -0.009136167967996597, -0.011335430055398207, -0.013241110458592392, -0.014803853056144256, -0.01598318363564812, -0.016748558154568684, -0.01708015381489863, -0.016969382463214604, -0.016419113019339703, -0.015443597172827055, -0.01406810027168644, -0.012328246963142131, -0.010269098533982548, -0.007943985846902027, -0.005413128099170466, -0.002742073177055738, -4.186826663751637e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.Q.x90_DragCosine.wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.0013710371168688756, 0.0027065660647557863, 0.00397199830085438, 0.005134560717308439, 0.006164144432031172, 0.007034084578733267, 0.007721850900375471, 0.008209631260363719, 0.008484792959128686, 0.0085402099084502, 0.008374447190037784, 0.007991798218483993, 0.007402173546107199, 0.0066208441895274405, 0.005668046125561179, 0.0045684561995969234, 0.0033505530199023133, 0.002045879390062873, 0.0006882253818169591, -0.000687246794114037, -0.0020449134542271726, -0.003349612060124502, -0.00456755189320125, -0.005667189200569045, -0.006620044146807444, -0.007401438413307741, -0.007991134342121528, -0.00837385907112546, -0.008539700085924046, -0.008484361944090534, -0.008209277522843944, -0.007721570908958379, -0.007033872892018857, -0.006163993839564462, -0.005134462426326372, -0.0039719421640136325, -0.0027065408429435014, -0.0013710307702896325, -2.09341389001896e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.Q.x180_Square.wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "q1.Q.x90_Square.wf": {
            "type": "constant",
            "sample": 0.05,
        },
        "q1.Q.saturation.wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "q1.z.const.wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "q1.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.001,
        },
        "q1.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q1.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.001,
        },
        "q1.resonator.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.I.x180_Cosine.wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.0005892606843622562, 0.0023417811952484336, 0.005212172171983234, 0.009126091996016224, 0.013982172199792415, 0.019654642856815535, 0.025996589956680406, 0.03284376040077201, 0.04001881607124151, 0.04733592679510702, 0.05460558324812178, 0.06163950514672756, 0.06825551760849956, 0.07428226938590929, 0.07956367077362887, 0.08396293624990885, 0.08736612714974136, 0.08968510261643467, 0.09085980240350315, 0.09085980240350316, 0.08968510261643467, 0.08736612714974137, 0.08396293624990886, 0.07956367077362889, 0.07428226938590929, 0.06825551760849953, 0.06163950514672757, 0.0546055832481218, 0.04733592679510702, 0.040018816071241546, 0.03284376040077205, 0.025996589956680426, 0.01965464285681555, 0.01398217219979242, 0.009126091996016224, 0.00521217217198323, 0.0023417811952484288, 0.0005892606843622562, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.I.x90_Cosine.wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.0002946303421811281, 0.0011708905976242168, 0.002606086085991617, 0.004563045998008112, 0.006991086099896207, 0.009827321428407768, 0.012998294978340203, 0.016421880200386006, 0.020009408035620756, 0.02366796339755351, 0.02730279162406089, 0.03081975257336378, 0.03412775880424978, 0.037141134692954644, 0.039781835386814436, 0.04198146812495442, 0.04368306357487068, 0.044842551308217335, 0.045429901201751575, 0.04542990120175158, 0.044842551308217335, 0.04368306357487069, 0.04198146812495443, 0.03978183538681444, 0.037141134692954644, 0.034127758804249765, 0.030819752573363786, 0.0273027916240609, 0.02366796339755351, 0.020009408035620773, 0.016421880200386024, 0.012998294978340213, 0.009827321428407775, 0.00699108609989621, 0.004563045998008112, 0.002606086085991615, 0.0011708905976242144, 0.0002946303421811281, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.I.-x90_Cosine.wf": {
            "type": "arbitrary",
            "samples": [0.0, -0.0006474868681043578, -0.002573177902642726, -0.005727198717339505, -0.010027861829824942, -0.015363782324520032, -0.021596762663442206, -0.02856537192984729, -0.03608912680417736, -0.04397316598723385, -0.05201329700547076, -0.060001284688802205, -0.06773024435212678, -0.07500000000000001, -0.08162226877976886, -0.08742553740855505, -0.09225950427718974, -0.09599897218294122, -0.0985470908713026, -0.0998378654067105, -0.09983786540671051, -0.0985470908713026, -0.09599897218294123, -0.09225950427718976, -0.08742553740855508, -0.08162226877976886, -0.07499999999999998, -0.06773024435212681, -0.060001284688802226, -0.05201329700547076, -0.043973165987233886, -0.0360891268041774, -0.028565371929847313, -0.021596762663442223, -0.015363782324520037, -0.010027861829824942, -0.0057271987173395, -0.0025731779026427204, -0.0006474868681043578, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.I.x180_DragCosine.wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.0012949737362087156, 0.005146355805285452, 0.01145439743467901, 0.020055723659649884, 0.030727564649040064, 0.04319352532688441, 0.05713074385969458, 0.07217825360835473, 0.0879463319744677, 0.10402659401094153, 0.12000256937760441, 0.13546048870425356, 0.15000000000000002, 0.16324453755953772, 0.1748510748171101, 0.18451900855437947, 0.19199794436588244, 0.1970941817426052, 0.199675730813421, 0.19967573081342102, 0.1970941817426052, 0.19199794436588247, 0.18451900855437953, 0.17485107481711015, 0.16324453755953772, 0.14999999999999997, 0.13546048870425362, 0.12000256937760445, 0.10402659401094153, 0.08794633197446777, 0.0721782536083548, 0.057130743859694626, 0.04319352532688445, 0.030727564649040074, 0.020055723659649884, 0.011454397434679, 0.005146355805285441, 0.0012949737362087156, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.I.x90_DragCosine.wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.0006474865235251675, 0.0025731765421745604, 0.00572719572252497, 0.010027856668006575, 0.015363774578439817, 0.02159675205631711, 0.028565358344901863, 0.036089110297807266, 0.04397314679519682, 0.05201327554174647, 0.06000126153702194, 0.06773022024973922, 0.07499997581560172, 0.0816222454842792, 0.08742551604114582, 0.09225948590708327, 0.0959989578683585, 0.0985470816169707, 0.09983786212142061, 0.09983786886245094, 0.0985471016654741, 0.09599899070509398, 0.09225953068160411, 0.08742557159382541, 0.08162231037634414, 0.07500004836639468, 0.06773029858024633, 0.060001343618537185, 0.0520133592484133, 0.04397322995906577, 0.036089190764983514, 0.028565434031329072, 0.021596821001752402, 0.015363834997222079, 0.010027906995303338, 0.005727234654859972, 0.0025732030711865103, 0.0006474999620832822, 2.051915953781308e-23],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.I.x180_Square.wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "q2.I.x90_Square.wf": {
            "type": "constant",
            "sample": 0.05,
        },
        "q2.I.saturation.wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "q2.Q.x180_Cosine.wf": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.Q.x90_Cosine.wf": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.Q.-x90_Cosine.wf": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.Q.x180_DragCosine.wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.002742073177055731, 0.005413128099170471, 0.007943985846902028, 0.010269098533982546, 0.012328246963142131, 0.014068100271686437, 0.015443597172827051, 0.0164191130193397, 0.016969382463214604, 0.01708015381489863, 0.016748558154568684, 0.015983183635648122, 0.014803853056144253, 0.013241110458592388, 0.011335430055398216, 0.009136167967996604, 0.0067002839292320555, 0.004090866056197569, 0.0013754969011406171, -0.001375496901140613, -0.004090866056197572, -0.006700283929232043, -0.009136167967996597, -0.011335430055398207, -0.013241110458592392, -0.014803853056144256, -0.01598318363564812, -0.016748558154568684, -0.01708015381489863, -0.016969382463214604, -0.016419113019339703, -0.015443597172827055, -0.01406810027168644, -0.012328246963142131, -0.010269098533982548, -0.007943985846902027, -0.005413128099170466, -0.002742073177055738, -4.186826663751637e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.Q.x90_DragCosine.wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.0013710371168688756, 0.0027065660647557863, 0.00397199830085438, 0.005134560717308439, 0.006164144432031172, 0.007034084578733267, 0.007721850900375471, 0.008209631260363719, 0.008484792959128686, 0.0085402099084502, 0.008374447190037784, 0.007991798218483993, 0.007402173546107199, 0.0066208441895274405, 0.005668046125561179, 0.0045684561995969234, 0.0033505530199023133, 0.002045879390062873, 0.0006882253818169591, -0.000687246794114037, -0.0020449134542271726, -0.003349612060124502, -0.00456755189320125, -0.005667189200569045, -0.006620044146807444, -0.007401438413307741, -0.007991134342121528, -0.00837385907112546, -0.008539700085924046, -0.008484361944090534, -0.008209277522843944, -0.007721570908958379, -0.007033872892018857, -0.006163993839564462, -0.005134462426326372, -0.0039719421640136325, -0.0027065408429435014, -0.0013710307702896325, -2.09341389001896e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.Q.x180_Square.wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "q2.Q.x90_Square.wf": {
            "type": "constant",
            "sample": 0.05,
        },
        "q2.Q.saturation.wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "q2.z.const.wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "q2.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.001,
        },
        "q2.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.001,
        },
        "q2.resonator.const.wf.Q": {
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
            "cosine": [(1.0, 2500)],
            "sine": [(-0.0, 2500)],
        },
        "q1.resonator.readout.iw2": {
            "cosine": [(0.0, 2500)],
            "sine": [(1.0, 2500)],
        },
        "q1.resonator.readout.iw3": {
            "cosine": [(-0.0, 2500)],
            "sine": [(-1.0, 2500)],
        },
        "q2.resonator.readout.iw1": {
            "cosine": [(1.0, 2500)],
            "sine": [(-0.0, 2500)],
        },
        "q2.resonator.readout.iw2": {
            "cosine": [(0.0, 2500)],
            "sine": [(1.0, 2500)],
        },
        "q2.resonator.readout.iw3": {
            "cosine": [(-0.0, 2500)],
            "sine": [(-1.0, 2500)],
        },
    },
    "mixers": {},
}


