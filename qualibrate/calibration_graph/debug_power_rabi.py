
# Single QUA script generated at 2025-04-24 12:23:12.958885
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
    v9 = declare(int, )
    v10 = declare(int, )
    v11 = declare(int, )
    v12 = declare(int, )
    v13 = declare(int, )
    set_dc_offset("q1.z", "single", 0.0)
    set_dc_offset("q2.z", "single", 0.0)
    set_dc_offset("c12.z", "single", 0)
    align("q1.I", "q1.Q", "q1.resonator", "q1.z")
    with for_(v1,0,(v1<10),(v1+1)):
        assign(v8, 0)
        r1 = declare_stream()
        save(v1, r1)
        with for_(v6,0.0,(v6<1.475),(v6+0.05)):
            measure("readout", "q1.resonator", dual_demod.full("iw1", "iw2", v2), dual_demod.full("iw3", "iw1", v4))
            assign(v8, Cast.to_int((v2>0.0)))
            wait(375, "q1.I", "q1.Q", "q1.z", "q1.resonator")
            frame_rotation_2pi(0.25, "q1.Q")
            align("q1.I", "q1.Q")
            play("x180_Cosine"*amp(v6), "q1.I")
            play("x180_Cosine"*amp(v6), "q1.Q")
            reset_frame("q1.Q")
            align("q1.I", "q1.Q", "q1.resonator", "q1.z")
            measure("readout", "q1.resonator", dual_demod.full("iw1", "iw2", v2), dual_demod.full("iw3", "iw1", v4))
            assign(v10, Cast.to_int((v2>0.0)))
            assign(v12, (v8^v10))
            r6 = declare_stream()
            save(v12, r6)
            wait(18750, "q1.I", "q1.Q", "q1.z", "q1.resonator")
    set_dc_offset("q1.z", "single", 0.0)
    set_dc_offset("q2.z", "single", 0.0)
    set_dc_offset("c12.z", "single", 0)
    align("q2.I", "q2.Q", "q2.resonator", "q2.z")
    with for_(v1,0,(v1<10),(v1+1)):
        assign(v9, 0)
        save(v1, r1)
        with for_(v6,0.0,(v6<1.475),(v6+0.05)):
            measure("readout", "q2.resonator", dual_demod.full("iw1", "iw2", v3), dual_demod.full("iw3", "iw1", v5))
            assign(v9, Cast.to_int((v3>0.0)))
            wait(375, "q2.I", "q2.Q", "q2.z", "q2.resonator")
            frame_rotation_2pi(0.25, "q2.Q")
            align("q2.I", "q2.Q")
            play("x180_Cosine"*amp(v6), "q2.I")
            play("x180_Cosine"*amp(v6), "q2.Q")
            reset_frame("q2.Q")
            align("q2.I", "q2.Q", "q2.resonator", "q2.z")
            measure("readout", "q2.resonator", dual_demod.full("iw1", "iw2", v3), dual_demod.full("iw3", "iw1", v5))
            assign(v11, Cast.to_int((v3>0.0)))
            assign(v13, (v9^v11))
            r7 = declare_stream()
            save(v13, r7)
            wait(18750, "q2.I", "q2.Q", "q2.z", "q2.resonator")
    with stream_processing():
        r1.save("n")
        r6.buffer(30).average().save("state1")
        r7.buffer(30).average().save("state2")


config = {
    "version": 1,
    "controllers": {
        "con1": {
            "fems": {
                "5": {
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
                "port": ('con1', 5, 5),
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
                "port": ('con1', 5, 1),
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
                "port": ('con1', 5, 1),
            },
        },
        "q1.z": {
            "operations": {
                "const": "q1.z.const.pulse",
            },
            "singleInput": {
                "port": ('con1', 5, 2),
            },
        },
        "q1.resonator": {
            "operations": {
                "readout": "q1.resonator.readout.pulse",
                "const": "q1.resonator.const.pulse",
            },
            "intermediate_frequency": -297307575.0,
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
                "port": ('con1', 5, 3),
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
                "port": ('con1', 5, 3),
            },
        },
        "q2.z": {
            "operations": {
                "const": "q2.z.const.pulse",
            },
            "singleInput": {
                "port": ('con1', 5, 4),
            },
        },
        "q2.resonator": {
            "operations": {
                "readout": "q2.resonator.readout.pulse",
                "const": "q2.resonator.const.pulse",
            },
            "intermediate_frequency": -183964642.0,
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
            "samples": [0.0, 0.00109160670231036, 0.004338154769046212, 0.009655560310612304, 0.016906105316586675, 0.025902004479850603, 0.03641026873740389, 0.04815873956471313, 0.060843137738538694, 0.07413494400898626, 0.08768990757551572, 0.10115696200184861, 0.11418731765226113, 0.12644349515993838, 0.13760806596530523, 0.14739187354898187, 0.1555415224337487, 0.1618459409943038, 0.1661418481014874] + [0.1683179820177597] * 2 + [0.1661418481014874, 0.16184594099430383, 0.15554152243374875, 0.1473918735489819, 0.13760806596530523, 0.12644349515993833, 0.11418731765226117, 0.10115696200184864, 0.08768990757551572, 0.07413494400898632, 0.06084313773853875, 0.04815873956471317, 0.03641026873740392, 0.02590200447985061, 0.016906105316586675, 0.009655560310612295, 0.004338154769046202, 0.00109160670231036, 0.0],
        },
        "q1.I.x90_Cosine.wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.00054580335115518, 0.002169077384523106, 0.004827780155306152, 0.008453052658293337, 0.012951002239925302, 0.018205134368701945, 0.024079369782356565, 0.030421568869269347, 0.03706747200449313, 0.04384495378775786, 0.050578481000924304, 0.057093658826130565, 0.06322174757996919, 0.06880403298265261, 0.07369593677449093, 0.07777076121687435, 0.0809229704971519, 0.0830709240507437] + [0.08415899100887984] * 2 + [0.0830709240507437, 0.08092297049715191, 0.07777076121687437, 0.07369593677449095, 0.06880403298265261, 0.06322174757996916, 0.057093658826130586, 0.05057848100092432, 0.04384495378775786, 0.03706747200449316, 0.030421568869269375, 0.024079369782356586, 0.01820513436870196, 0.012951002239925305, 0.008453052658293337, 0.0048277801553061475, 0.002169077384523101, 0.00054580335115518, 0.0],
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
            "samples": [0.0, 0.0014177035210548446, 0.005634096307709442, 0.012539976001558631, 0.02195648394602339, 0.03363973753160607, 0.04728714662737073, 0.06254525050639118, 0.07901887229291388, 0.0962813538358632, 0.11388560593084099, 0.13137568769567531, 0.14829861519977425, 0.16421609350998628, 0.17871586829914338, 0.19142240301658767, 0.20200660508757287, 0.21019434923808591, 0.21577357719545254, 0.21859978988621054, 0.21859978988621057, 0.21577357719545254, 0.21019434923808591, 0.20200660508757293, 0.19142240301658772, 0.17871586829914338, 0.1642160935099862, 0.1482986151997743, 0.13137568769567537, 0.11388560593084099, 0.0962813538358633, 0.07901887229291395, 0.06254525050639123, 0.04728714662737076, 0.03363973753160608, 0.02195648394602339, 0.012539976001558619, 0.00563409630770943, 0.0014177035210548446, 0.0],
        },
        "q2.I.x90_Cosine.wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.0007088517605274223, 0.002817048153854721, 0.006269988000779316, 0.010978241973011695, 0.016819868765803034, 0.023643573313685363, 0.03127262525319559, 0.03950943614645694, 0.0481406769179316, 0.056942802965420494, 0.06568784384783766, 0.07414930759988712, 0.08210804675499314, 0.08935793414957169, 0.09571120150829383, 0.10100330254378644, 0.10509717461904296, 0.10788678859772627, 0.10929989494310527, 0.10929989494310528, 0.10788678859772627, 0.10509717461904296, 0.10100330254378646, 0.09571120150829386, 0.08935793414957169, 0.0821080467549931, 0.07414930759988715, 0.06568784384783768, 0.056942802965420494, 0.04814067691793165, 0.039509436146456973, 0.031272625253195616, 0.02364357331368538, 0.01681986876580304, 0.010978241973011695, 0.0062699880007793096, 0.002817048153854715, 0.0007088517605274223, 0.0],
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
                "5": {
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
                "port": ('con1', 5, 5),
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
                "port": ('con1', 5, 1),
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
                "port": ('con1', 5, 1),
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
                "port": ('con1', 5, 2),
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
            "intermediate_frequency": -297307575.0,
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
                "port": ('con1', 5, 3),
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
                "port": ('con1', 5, 3),
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
                "port": ('con1', 5, 4),
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
            "intermediate_frequency": -183964642.0,
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
            "samples": [0.0, 0.00109160670231036, 0.004338154769046212, 0.009655560310612304, 0.016906105316586675, 0.025902004479850603, 0.03641026873740389, 0.04815873956471313, 0.060843137738538694, 0.07413494400898626, 0.08768990757551572, 0.10115696200184861, 0.11418731765226113, 0.12644349515993838, 0.13760806596530523, 0.14739187354898187, 0.1555415224337487, 0.1618459409943038, 0.1661418481014874] + [0.1683179820177597] * 2 + [0.1661418481014874, 0.16184594099430383, 0.15554152243374875, 0.1473918735489819, 0.13760806596530523, 0.12644349515993833, 0.11418731765226117, 0.10115696200184864, 0.08768990757551572, 0.07413494400898632, 0.06084313773853875, 0.04815873956471317, 0.03641026873740392, 0.02590200447985061, 0.016906105316586675, 0.009655560310612295, 0.004338154769046202, 0.00109160670231036, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.I.x90_Cosine.wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.00054580335115518, 0.002169077384523106, 0.004827780155306152, 0.008453052658293337, 0.012951002239925302, 0.018205134368701945, 0.024079369782356565, 0.030421568869269347, 0.03706747200449313, 0.04384495378775786, 0.050578481000924304, 0.057093658826130565, 0.06322174757996919, 0.06880403298265261, 0.07369593677449093, 0.07777076121687435, 0.0809229704971519, 0.0830709240507437] + [0.08415899100887984] * 2 + [0.0830709240507437, 0.08092297049715191, 0.07777076121687437, 0.07369593677449095, 0.06880403298265261, 0.06322174757996916, 0.057093658826130586, 0.05057848100092432, 0.04384495378775786, 0.03706747200449316, 0.030421568869269375, 0.024079369782356586, 0.01820513436870196, 0.012951002239925305, 0.008453052658293337, 0.0048277801553061475, 0.002169077384523101, 0.00054580335115518, 0.0],
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
            "samples": [0.0, 0.0014177035210548446, 0.005634096307709442, 0.012539976001558631, 0.02195648394602339, 0.03363973753160607, 0.04728714662737073, 0.06254525050639118, 0.07901887229291388, 0.0962813538358632, 0.11388560593084099, 0.13137568769567531, 0.14829861519977425, 0.16421609350998628, 0.17871586829914338, 0.19142240301658767, 0.20200660508757287, 0.21019434923808591, 0.21577357719545254, 0.21859978988621054, 0.21859978988621057, 0.21577357719545254, 0.21019434923808591, 0.20200660508757293, 0.19142240301658772, 0.17871586829914338, 0.1642160935099862, 0.1482986151997743, 0.13137568769567537, 0.11388560593084099, 0.0962813538358633, 0.07901887229291395, 0.06254525050639123, 0.04728714662737076, 0.03363973753160608, 0.02195648394602339, 0.012539976001558619, 0.00563409630770943, 0.0014177035210548446, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.I.x90_Cosine.wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.0007088517605274223, 0.002817048153854721, 0.006269988000779316, 0.010978241973011695, 0.016819868765803034, 0.023643573313685363, 0.03127262525319559, 0.03950943614645694, 0.0481406769179316, 0.056942802965420494, 0.06568784384783766, 0.07414930759988712, 0.08210804675499314, 0.08935793414957169, 0.09571120150829383, 0.10100330254378644, 0.10509717461904296, 0.10788678859772627, 0.10929989494310527, 0.10929989494310528, 0.10788678859772627, 0.10509717461904296, 0.10100330254378646, 0.09571120150829386, 0.08935793414957169, 0.0821080467549931, 0.07414930759988715, 0.06568784384783768, 0.056942802965420494, 0.04814067691793165, 0.039509436146456973, 0.031272625253195616, 0.02364357331368538, 0.01681986876580304, 0.010978241973011695, 0.0062699880007793096, 0.002817048153854715, 0.0007088517605274223, 0.0],
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


