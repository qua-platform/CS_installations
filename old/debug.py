# Single QUA script generated at 2024-12-02 07:40:37.015395
# QUA library version: 1.2.1

from qm import CompilerOptionArguments
from qm.qua import *

with program() as prog:
    v1 = declare(int, value=16)
    v2 = declare(fixed, value=0.2)
    v3 = declare(
        int,
    )
    v4 = declare(
        fixed,
    )
    v5 = declare(
        int,
    )
    v6 = declare(
        fixed,
    )
    v7 = declare(
        int,
    )
    with strict_timing_():
        play("initialization", "P1_sticky")
        play("initialization", "P2_sticky")
        play("idle", "P1_sticky", duration=(v1 >> 2))
        play("idle", "P2_sticky", duration=(v1 >> 2))
        play("readout", "P1_sticky")
        play("readout", "P2_sticky")
        assign(v5, ((20480 + Cast.mul_int_by_fixed((v1 << 10), 0.2)) + 51200))
        assign(v4, (0 - Cast.mul_fixed_by_int(4.8828125e-07, v5)))
        play("compensation" * amp(((v4 - 0.1) * 4)), "P1_sticky")
        assign(v7, ((-20480 + Cast.mul_int_by_fixed((v1 << 10), -0.2)) + -51200))
        assign(v6, (0 - Cast.mul_fixed_by_int(4.8828125e-07, v7)))
        play("compensation" * amp(((v6 - -0.1) * 4)), "P2_sticky")
    ramp_to_zero("P1_sticky")
    ramp_to_zero("P2_sticky")


config = {
    "version": 1,
    "controllers": {
        "con1": {
            "type": "opx1000",
            "fems": {
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
                        "8": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                            "sampling_rate": 1000000000,
                            "upsampling_mode": "mw",
                        },
                    },
                    "digital_outputs": {
                        "1": {},
                        "2": {},
                    },
                    "analog_inputs": {
                        "1": {
                            "offset": 0.0,
                            "gain_db": 0,
                            "sampling_rate": 1000000000,
                        },
                        "2": {
                            "offset": 0.0,
                            "gain_db": 0,
                            "sampling_rate": 1000000000,
                        },
                    },
                },
            },
        },
    },
    "elements": {
        "P1": {
            "singleInput": {
                "port": ("con1", 3, 1),
            },
            "operations": {
                "step": "P1_step_pulse",
            },
        },
        "P1_sticky": {
            "singleInput": {
                "port": ("con1", 3, 1),
            },
            "sticky": {
                "analog": True,
                "duration": 4,
            },
            "operations": {
                "step": "step_pulse",
                "initialization": "P1_sticky_initialization_pulse",
                "idle": "P1_sticky_idle_pulse",
                "readout": "P1_sticky_readout_pulse",
                "compensation": "P1_sticky_compensation_pulse",
            },
        },
        "P2": {
            "singleInput": {
                "port": ("con1", 3, 2),
            },
            "operations": {
                "step": "P2_step_pulse",
            },
        },
        "P2_sticky": {
            "singleInput": {
                "port": ("con1", 3, 2),
            },
            "sticky": {
                "analog": True,
                "duration": 4,
            },
            "operations": {
                "step": "step_pulse",
                "initialization": "P2_sticky_initialization_pulse",
                "idle": "P2_sticky_idle_pulse",
                "readout": "P2_sticky_readout_pulse",
                "compensation": "P2_sticky_compensation_pulse",
            },
        },
        "sensor_gate": {
            "singleInput": {
                "port": ("con1", 3, 3),
            },
            "operations": {
                "step": "bias_charge_pulse",
            },
        },
        "sensor_gate_sticky": {
            "singleInput": {
                "port": ("con1", 3, 3),
            },
            "sticky": {
                "analog": True,
                "duration": 4,
            },
            "operations": {
                "step": "bias_charge_pulse",
            },
        },
        "qdac_trigger1": {
            "digitalInputs": {
                "trigger": {
                    "port": ("con1", 3, 1),
                    "delay": 0,
                    "buffer": 0,
                },
            },
            "operations": {
                "trigger": "trigger_pulse",
            },
        },
        "qdac_trigger2": {
            "digitalInputs": {
                "trigger": {
                    "port": ("con1", 3, 2),
                    "delay": 0,
                    "buffer": 0,
                },
            },
            "operations": {
                "trigger": "trigger_pulse",
            },
        },
        "tank_circuit": {
            "singleInput": {
                "port": ("con1", 3, 8),
            },
            "intermediate_frequency": 151000000,
            "operations": {
                "readout": "reflectometry_readout_pulse",
                "long_readout": "reflectometry_readout_long_pulse",
            },
            "outputs": {
                "out1": ("con1", 3, 1),
            },
            "time_of_flight": 24,
            "smearing": 0,
        },
    },
    "pulses": {
        "P1_step_pulse": {
            "operation": "control",
            "length": 16,
            "waveforms": {
                "single": "P1_step_wf",
            },
        },
        "P2_step_pulse": {
            "operation": "control",
            "length": 16,
            "waveforms": {
                "single": "P2_step_wf",
            },
        },
        "bias_charge_pulse": {
            "operation": "control",
            "length": 16,
            "waveforms": {
                "single": "charge_sensor_step_wf",
            },
        },
        "trigger_pulse": {
            "operation": "control",
            "length": 1000,
            "digital_marker": "ON",
        },
        "cw_pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "const_wf",
                "Q": "zero_wf",
            },
        },
        "gaussian_pulse": {
            "operation": "control",
            "length": 20,
            "waveforms": {
                "I": "gaussian_wf",
                "Q": "zero_wf",
            },
        },
        "pi_pulse": {
            "operation": "control",
            "length": 32,
            "waveforms": {
                "I": "pi_wf",
                "Q": "zero_wf",
            },
        },
        "pi_half_pulse": {
            "operation": "control",
            "length": 16,
            "waveforms": {
                "I": "pi_half_wf",
                "Q": "zero_wf",
            },
        },
        "reflectometry_readout_pulse": {
            "operation": "measurement",
            "length": 1000,
            "waveforms": {
                "single": "reflect_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
            },
            "digital_marker": "ON",
        },
        "reflectometry_readout_long_pulse": {
            "operation": "measurement",
            "length": 2000000,
            "waveforms": {
                "single": "reflect_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
            },
            "digital_marker": "ON",
        },
        "step_pulse": {
            "operation": "control",
            "length": 16,
            "waveforms": {
                "single": "step_wf",
            },
        },
        "P1_sticky_initialization_pulse": {
            "operation": "control",
            "length": 200,
            "waveforms": {
                "single": "P1_sticky_initialization_wf",
            },
        },
        "P2_sticky_initialization_pulse": {
            "operation": "control",
            "length": 200,
            "waveforms": {
                "single": "P2_sticky_initialization_wf",
            },
        },
        "P1_sticky_idle_pulse": {
            "operation": "control",
            "length": 16,
            "waveforms": {
                "single": "P1_sticky_idle_wf",
            },
        },
        "P2_sticky_idle_pulse": {
            "operation": "control",
            "length": 16,
            "waveforms": {
                "single": "P2_sticky_idle_wf",
            },
        },
        "P1_sticky_readout_pulse": {
            "operation": "control",
            "length": 500,
            "waveforms": {
                "single": "P1_sticky_readout_wf",
            },
        },
        "P2_sticky_readout_pulse": {
            "operation": "control",
            "length": 500,
            "waveforms": {
                "single": "P2_sticky_readout_wf",
            },
        },
        "P1_sticky_compensation_pulse": {
            "operation": "control",
            "length": 2000,
            "waveforms": {
                "single": "P1_sticky_compensation_wf",
            },
        },
        "P2_sticky_compensation_pulse": {
            "operation": "control",
            "length": 2000,
            "waveforms": {
                "single": "P2_sticky_compensation_wf",
            },
        },
    },
    "waveforms": {
        "P1_step_wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "P2_step_wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "charge_sensor_step_wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "pi_wf": {
            "type": "constant",
            "sample": 0.7,
        },
        "pi_half_wf": {
            "type": "constant",
            "sample": 0.7,
        },
        "gaussian_wf": {
            "type": "arbitrary",
            "samples": [
                0.017876195628595826,
                0.03137370038670043,
                0.05172648716812584,
                0.080115550567903,
                0.11656743825370923,
                0.15932879731060356,
                0.20458222535710444,
                0.24677326871959937,
                0.2796307477078583,
            ]
            + [0.29766538147807303] * 2
            + [
                0.2796307477078583,
                0.24677326871959937,
                0.20458222535710444,
                0.15932879731060356,
                0.11656743825370923,
                0.080115550567903,
                0.05172648716812584,
                0.03137370038670043,
                0.017876195628595826,
            ],
        },
        "reflect_wf": {
            "type": "constant",
            "sample": 0.03,
        },
        "const_wf": {
            "type": "constant",
            "sample": 0.85,
        },
        "zero_wf": {
            "type": "constant",
            "sample": 0.0,
        },
        "step_wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "P1_sticky_initialization_wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "P2_sticky_initialization_wf": {
            "type": "constant",
            "sample": -0.1,
        },
        "P1_sticky_idle_wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "P2_sticky_idle_wf": {
            "type": "constant",
            "sample": -0.1,
        },
        "P1_sticky_readout_wf": {
            "type": "constant",
            "sample": -0.1,
        },
        "P2_sticky_readout_wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "P1_sticky_compensation_wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "P2_sticky_compensation_wf": {
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
        "cosine_weights": {
            "cosine": [(1.0, 1000)],
            "sine": [(0.0, 1000)],
        },
        "sine_weights": {
            "cosine": [(0.0, 1000)],
            "sine": [(1.0, 1000)],
        },
    },
}

loaded_config = None
