# %%
"""
QUA-Config supporting OPX1000 w/ LF-FEM & External Mixers
"""
import numpy as np
from qualang_tools.config.waveform_tools import drag_gaussian_pulse_waveforms
from qualang_tools.units import unit

#######################
# AUXILIARY FUNCTIONS #
#######################
u = unit(coerce_to_integer=True)


# IQ imbalance matrix
def IQ_imbalance(g, phi):
    """
    Creates the correction matrix for the mixer imbalance caused by the gain and phase imbalances, more information can
    be seen here:
    https://docs.qualang.io/libs/examples/mixer-calibration/#non-ideal-mixer
    :param g: relative gain imbalance between the 'I' & 'Q' ports. (unit-less), set to 0 for no gain imbalance.
    :param phi: relative phase imbalance between the 'I' & 'Q' ports (radians), set to 0 for no phase imbalance.
    """
    c = np.cos(phi)
    s = np.sin(phi)
    N = 1 / ((1 - g**2) * (2 * c**2 - 1))
    return [float(N * x) for x in [(1 - g) * c, (1 + g) * s, (1 - g) * s, (1 + g) * c]]


######################
# Network parameters #
######################
qop_ip = "172.16.33.107"  # Write the QM router IP address
cluster_name = "Beta_8"  # Write your cluster_name if version >= QOP220
# qop_ip = "192.168.88.253"  # Write the QM router IP address
# cluster_name = "Cluster_1"  # Write your cluster_name if version >= QOP220
qop_port = 9510  # Write the QOP port if version < QOP220
octave_config = None


#####################
# OPX configuration #
#####################
con1 = "con1"
fem1 = 1  # Should be the LF-FEM index, e.g., 1
fem2 = 2  # Should be the LF-FEM index, e.g., 1
# fem3 = 3  # Should be the LF-FEM index, e.g., 1


#############################################
#              OPX PARAMETERS               #
#############################################
sampling_rate = int(1e9)  # or, int(2e9)


#################
#   CONSTANTS   #
#################

QUBIT_CONSTANTS = {
    "qubit1": {
        "con": "con1",
        "fem": 1,
        "ao_I": 1,
        "ao_Q": 2,
        "do": 1,
        "LO": 16 * u.GHz,
        "IF": 50 * u.GHz,
        "mixer_g": 0,
        "mixer_phi": 0,
        "pi_amp": 0.25,
        "pi_len": 52,
        "pi_sigma": 10,
        "midcircuit_parity_threshold": 0.0,
        "delay": 0,
        "digital_delay": 0,
    },
    "qubit2": {
        "con": "con1",
        "fem": 1,
        "ao_I": 1,
        "ao_Q": 2,
        "do": 1,
        "LO": 16 * u.GHz,
        "IF": 200 * u.GHz,
        "mixer_g": 0,
        "mixer_phi": 0,
        "pi_amp": 0.25,
        "pi_len": 52,
        "pi_sigma": 10,
        "midcircuit_parity_threshold": 0.0,
        "delay": 0,
        "digital_delay": 0,
    },
    "qubit3": {
        "con": "con1",
        "fem": 1,
        "ao_I": 3,
        "ao_Q": 4,
        "do": 2,
        "LO": 16.3 * u.GHz,
        "IF": 50 * u.GHz,
        "mixer_g": 0,
        "mixer_phi": 0,
        "pi_amp": 0.25,
        "pi_len": 52,
        "pi_sigma": 10,
        "midcircuit_parity_threshold": 0.0,
        "delay": 0,
        "digital_delay": 0,
    },
    "qubit4": {
        "con": "con1",
        "fem": 1,
        "ao_I": 3,
        "ao_Q": 4,
        "do": 2,
        "LO": 16.3 * u.GHz,
        "IF": 200 * u.GHz,
        "mixer_g": 0,
        "mixer_phi": 0,
        "pi_amp": 0.25,
        "pi_len": 52,
        "pi_sigma": 10,
        "midcircuit_parity_threshold": 0.0,
        "delay": 0,
        "digital_delay": 0,
    },
    "qubit5": {
        "con": "con1",
        "fem": 1,
        "ao_I": 1,
        "ao_Q": 1,
        "do": 3,
        "LO": 16.6 * u.GHz,
        "IF": 50 * u.GHz,
        "mixer_g": 0,
        "mixer_phi": 0,
        "pi_amp": 0.25,
        "pi_len": 52,
        "pi_sigma": 10,
        "midcircuit_parity_threshold": 0.0,
        "delay": 0,
        "digital_delay": 0,
    },
}

PLUNGER_CONSTANTS = {
    "P1": {
        "con": "con1",
        "fem": 2,
        "ao": 1,
        "step_amp": 0.25,
        "delay": 0,
    },
    "P2": {
        "con": "con1",
        "fem": 2,
        "ao": 2,
        "step_amp": 0.25,
        "delay": 0,
    },
    "P3": {
        "con": "con1",
        "fem": 2,
        "ao": 3,
        "step_amp": 0.25,
        "delay": 0,
    },
    "P4": {
        "con": "con1",
        "fem": 2,
        "ao": 4,
        "step_amp": 0.25,
        "delay": 0,
    },
    "P5": {
        "con": "con1",
        "fem": 2,
        "ao": 5,
        "step_amp": 0.25,
        "delay": 0,
    },
}

BARRIER_CONSTANTS = {
    "B1": {
        "con": "con1",
        "fem": 2,
        "ao": 6,
        "step_amp": 0.25,
        "delay": 0,
    },
    "B2": {
        "con": "con1",
        "fem": 2,
        "ao": 7,
        "step_amp": 0.25,
        "delay": 0,
    },
    "B3": {
        "con": "con1",
        "fem": 2,
        "ao": 8,
        "step_amp": 0.25,
        "delay": 0,
    },
    "B4": {
        "con": "con1",
        "fem": 1,
        "ao": 7,
        "step_amp": 0.25,
        "delay": 0,
    },
}

PLUNGER_SD_CONSTANTS = {
    "Psd1": {
        "con": "con1",
        "fem": 2,
        "ao": 6,
        "step_amp": 0.25,
        "delay": 0,
    },
    "Psd2": {
        "con": "con1",
        "fem": 2,
        "ao": 7,
        "step_amp": 0.25,
        "delay": 0,
    },
}

TANK_CIRCUIT_CONSTANTS = {
    "tank_circuit1": {
        "con": "con1",
        "fem": 1,
        "ao": 8,
        "ai": 2,
        "IF": 150 * u.MHz,
        "readout_amp": 0.1,
        "readout_len": 1_000,
        "time_of_flight": 24,
        "delay": 0,
    },
    "tank_circuit2": {
        "con": "con1",
        "fem": 1,
        "ao": 8,
        "ai": 2,
        "IF": 200 * u.MHz,
        "readout_amp": 0.1,
        "readout_len": 1_000,
        "time_of_flight": 24,
        "delay": 0,
    },
}


########################
#  Pi pulse waveforms  #
########################


# TODO: Implement Kaiser
def generate_waveforms(rotation_keys):
    """Generate all necessary waveforms for a set of rotation types across all qubits."""

    if not isinstance(rotation_keys, list):
        raise ValueError("rotation_keys must be a list")

    waveforms = {}

    for qb, constants in QUBIT_CONSTANTS.items():
        pi_amp = constants["pi_amp"]
        pi_len = constants["pi_len"]
        pi_sigma = constants["pi_sigma"]

        for rotation_key in rotation_keys:
            if rotation_key in ["x180", "y180"]:
                wf_amp = pi_amp
            elif rotation_key in ["x90", "y90"]:
                wf_amp = pi_amp / 2
            elif rotation_key in ["minus_x90", "minus_y90"]:
                wf_amp = -pi_amp / 2
            else:
                continue

            wf, der_wf = np.array(
                drag_gaussian_pulse_waveforms(
                    wf_amp, pi_len, pi_sigma, alpha=0, anharmonicity=0
                )
            )

            if rotation_key in ["x180", "x90", "minus_x90"]:
                I_wf = wf
                Q_wf = der_wf
            elif rotation_key in ["y180", "y90", "minus_y90"]:
                I_wf = (-1) * der_wf
                Q_wf = wf
            else:
                raise ValueError(
                    f'{rotation_key} is passed. rotation_key must be one of ["x180", "x90", "minus_x90", "y180", "y90", "minus_y90"]'
                )

            waveforms[f"{qb}_{rotation_key}_I"] = I_wf
            waveforms[f"{qb}_{rotation_key}_Q"] = Q_wf

    return waveforms


qubit_rotation_keys = ["x180", "x90", "minus_x90", "y180", "y90", "minus_y90"]
waveforms = generate_waveforms(qubit_rotation_keys)


######################
#      DC GATES      #
######################

## Section defining the points from the charge stability map - can be done in the config
# Relevant points in the charge stability map as ["P1", "P2"] in V
level_init = [0.1, -0.1]
level_manip = [0.2, -0.2]
level_readout = [0.12, -0.12]

# Duration of each step in ns
duration_init = 2500
duration_manip = 1000
duration_readout = 1200  # reflectometry_readout_length + 100
duration_compensation_pulse = 4 * u.us

# Step parameters
step_length = 16  # in ns

# Time to ramp down to zero for sticky elements in ns
hold_offset_duration = 4  # in ns
bias_tee_cut_off_frequency = 10 * u.kHz

######################
#    QUBIT PULSES    #
######################
qubit_LO = 4 * u.GHz
qubit_IF = 100 * u.MHz
qubit_g = 0.0
qubit_phi = 0.0

# Pi pulse
pi_amp = 0.25  # in V
pi_length = 32  # in ns
# Pi half
pi_half_amp = 0.25  # in V
pi_half_length = 16  # in ns
# Gaussian pulse
gaussian_amp = 0.1  # in V
gaussian_length = 20 * int(sampling_rate // 1e9)  # in units of [1/sampling_rate]
# CW pulse
CONST_AMP = 0.3  # in V
CONST_LEN = 100  # in ns

#############################################
#                  Config                   #
#############################################
config = {
    "version": 1,
    "controllers": {
        con1: {
            "type": "opx1000",
            "fems": {
                fem1: {
                    "type": "LF",
                    "analog_outputs": {
                        # EDSR I1 (q1, q2)
                        1: {
                            # DC Offset applied to the analog output at the beginning of a program.
                            "offset": 0.0,
                            # The "output_mode" can be used to tailor the max voltage and frequency bandwidth, i.e.,
                            #   "direct":    1Vpp (-0.5V to 0.5V), 750MHz bandwidth (default)
                            #   "amplified": 5Vpp (-2.5V to 2.5V), 330MHz bandwidth
                            "output_mode": "direct",
                            # The "sampling_rate" can be adjusted by using more FEM cores, i.e.,
                            #   1 GS/s: uses one core per output (default)
                            #   2 GS/s: uses two cores per output
                            # NOTE: duration parameterization of arb. waveforms, sticky elements and chirping
                            #       aren't yet supported in 2 GS/s.
                            "sampling_rate": sampling_rate,
                            # At 1 GS/s, use the "upsampling_mode" to optimize output for
                            #   modulated pulses (optimized for modulated pulses):      "mw"    (default)
                            #   unmodulated pulses (optimized for clean step response): "pulse"
                            "upsampling_mode": "mw",
                        },
                        # EDSR Q1 (q1, q2)
                        2: {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": sampling_rate,
                            "upsampling_mode": "mw",
                        },
                        # EDSR I2 (q3, q4)
                        3: {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": sampling_rate,
                            "upsampling_mode": "mw",
                        },
                        # EDSR Q2 (q3, q4)
                        4: {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": sampling_rate,
                            "upsampling_mode": "mw",
                        },
                        # EDSR I3 (q5)
                        5: {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": sampling_rate,
                            "upsampling_mode": "mw",
                        },
                        # EDSR Q3 (q5)
                        6: {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": sampling_rate,
                            "upsampling_mode": "mw",
                        },
                        # B4
                        7: {
                            "offset": 0.0,
                            "output_mode": "amplified",
                            "sampling_rate": sampling_rate,
                            "upsampling_mode": "pulse",
                        },
                        # RF Reflectometry
                        8: {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": sampling_rate,
                            "upsampling_mode": "mw",
                        },
                    },
                    "digital_outputs": {
                        1: {},  # TTL for RF1
                        2: {},  # TTL for RF2
                        3: {},  # TTL for RF3
                    },
                    "analog_inputs": {
                        # 1: {"offset": 0.0, "gain_db": 0, "sampling_rate": sampling_rate},  # RF reflectometry input
                        2: {
                            "offset": 0.0,
                            "gain_db": 0,
                            "sampling_rate": sampling_rate,
                        },  # DC readout input
                    },
                },
                fem2: {
                    "type": "LF",
                    "analog_outputs": {
                        # P1
                        1: {
                            "offset": 0.0,
                            "output_mode": "amplified",
                            "sampling_rate": sampling_rate,
                            "upsampling_mode": "pulse",
                        },
                        # P2
                        2: {
                            "offset": 0.0,
                            "output_mode": "amplified",
                            "sampling_rate": sampling_rate,
                            "upsampling_mode": "pulse",
                        },
                        # P3
                        3: {
                            "offset": 0.0,
                            "output_mode": "amplified",
                            "sampling_rate": sampling_rate,
                            "upsampling_mode": "pulse",
                        },
                        # P4
                        4: {
                            "offset": 0.0,
                            "output_mode": "amplified",
                            "sampling_rate": sampling_rate,
                            "upsampling_mode": "pulse",
                        },
                        # P5
                        5: {
                            "offset": 0.0,
                            "output_mode": "amplified",
                            "sampling_rate": sampling_rate,
                            "upsampling_mode": "pulse",
                        },
                        # B1
                        6: {
                            "offset": 0.0,
                            "output_mode": "amplified",
                            "sampling_rate": sampling_rate,
                            "upsampling_mode": "pulse",
                        },
                        # B2
                        7: {
                            "offset": 0.0,
                            "output_mode": "amplified",
                            "sampling_rate": sampling_rate,
                            "upsampling_mode": "pulse",
                        },
                        # B3
                        8: {
                            "offset": 0.0,
                            "output_mode": "amplified",
                            "sampling_rate": sampling_rate,
                            "upsampling_mode": "pulse",
                        },
                    },
                    "digital_outputs": {},
                    "analog_inputs": {},
                },
                # fem3: {
                #     "type": "LF",
                #     "analog_outputs": {
                #         # B4
                #         1: {
                #             "offset": 0.0,
                #             "output_mode": "amplified",
                #             "sampling_rate": sampling_rate,
                #             "upsampling_mode": "pulse",
                #         },
                #         # Psd1
                #         2: {
                #             "offset": 0.0,
                #             "output_mode": "amplified",
                #             "sampling_rate": sampling_rate,
                #             "upsampling_mode": "pulse",
                #         },
                #         # Psd2
                #         3: {
                #             "offset": 0.0,
                #             "output_mode":"amplified",
                #             "sampling_rate": sampling_rate,
                #             "upsampling_mode": "pulse",
                #         },
                #     },
                #     "digital_outputs": {
                #     },
                #     "analog_inputs": {
                #     },
                # },
            },
        }
    },
    "elements": {
        # pluger (P1, P2, ...)
        **{
            pg: {
                "singleInput": {
                    "port": (val["con"], val["fem"], val["ao"]),
                },
                "operations": {
                    "step": f"{pg}_step_pulse",
                },
            }
            for pg, val in PLUNGER_CONSTANTS.items()
        },
        # pluger sticky (P1_sticky, P2_sticky, ...)
        **{
            f"{pg}_sticky": {
                "singleInput": {
                    "port": (val["con"], val["fem"], val["ao"]),
                },
                "sticky": {"analog": True, "duration": hold_offset_duration},
                "operations": {
                    "step": f"{pg}_step_pulse",
                },
            }
            for pg, val in PLUNGER_CONSTANTS.items()
        },
        # barrier (B1, B2, ...)
        **{
            br: {
                "singleInput": {
                    "port": (val["con"], val["fem"], val["ao"]),
                },
                "operations": {
                    "step": f"{br}_step_pulse",
                },
            }
            for br, val in BARRIER_CONSTANTS.items()
        },
        # barrier sticky (B1_sticky, B2_sticky, ...)
        **{
            f"{br}_sticky": {
                "singleInput": {
                    "port": (val["con"], val["fem"], val["ao"]),
                },
                "sticky": {"analog": True, "duration": hold_offset_duration},
                "operations": {
                    "step": f"{br}_step_pulse",
                },
            }
            for br, val in BARRIER_CONSTANTS.items()
        },
        # qubits (qubit1, ...)
        **{
            qb: {
                "mixInputs": {
                    "I": (val["con"], val["fem"], val["ao_I"]),
                    "Q": (val["con"], val["fem"], val["ao_Q"]),
                    "lo_frequency": val["LO"],
                    "mixer": f"mixer_{qb}",
                },
                "intermediate_frequency": val["IF"],
                "operations": {
                    "const": "const_pulse",
                    "x180": f"x180_gaussian_pulse_{qb}",
                    "x90": f"x90_gaussian_pulse_{qb}",
                    "y180": f"y180_gaussian_pulse_{qb}",
                    "y90": f"y90_gaussian_pulse_{qb}",
                },
            }
            for qb, val in QUBIT_CONSTANTS.items()
        },
        # qubit_triggers (qubit1_trigger, ...)
        **{
            f"{qb}_trigger": {
                "digitalInputs": {
                    "trigger": {
                        "port": (val["con"], val["fem"], val["do"]),
                        "delay": 0,
                        "buffer": 0,
                    }
                },
                "operations": {
                    "trigger": "trigger_pulse",
                },
            }
            for qb, val in QUBIT_CONSTANTS.items()
        },
        # reflectometry (qubit1, ...)
        **{
            tc: {
                "singleInput": {
                    "port": (val["con"], val["fem"], val["ao"]),
                },
                "intermediate_frequency": val["IF"],
                "operations": {
                    "readout": "reflectometry_readout_pulse",
                },
                "outputs": {
                    "out1": (val["con"], val["fem"], val["ai"]),
                },
                "time_of_flight": val["time_of_flight"],
                "smearing": 0,
            }
            for tc, val in TANK_CIRCUIT_CONSTANTS.items()
        },
    },
    "pulses": {
        # pluger (P1, P2, ...)
        **{
            f"{pg}_step_pulse": {
                "operation": "control",
                "length": step_length,
                "waveforms": {
                    "single": f"{pg}_step_wf",
                },
            }
            for pg, val in PLUNGER_CONSTANTS.items()
        },
        **{
            f"{br}_step_pulse": {
                "operation": "control",
                "length": step_length,
                "waveforms": {
                    "single": f"{br}_step_wf",
                },
            }
            for br, val in BARRIER_CONSTANTS.items()
        },
        **{
            f"{pg}_step_pulse": {
                "operation": "control",
                "length": step_length,
                "waveforms": {
                    "single": f"{pg}_step_wf",
                },
            }
            for pg, val in PLUNGER_SD_CONSTANTS.items()
        },
        **{
            f"x180_gaussian_pulse_{qb}": {
                "operation": "control",
                "length": val["pi_len"],
                "waveforms": {
                    "I": f"x180_gaussian_I_wf_{qb}",
                    "Q": f"x180_gaussian_Q_wf_{qb}",
                },
            }
            for qb, val in QUBIT_CONSTANTS.items()
        },
        **{
            f"x90_gaussian_pulse_{qb}": {
                "operation": "control",
                "length": val["pi_len"],
                "waveforms": {
                    "I": f"x90_gaussian_I_wf_{qb}",
                    "Q": f"x90_gaussian_Q_wf_{qb}",
                },
            }
            for qb, val in QUBIT_CONSTANTS.items()
        },
        **{
            f"minus_x90_gaussian_pulse_{qb}": {
                "operation": "control",
                "length": val["pi_len"],
                "waveforms": {
                    "I": f"minus_x90_gaussian_I_wf_{qb}",
                    "Q": f"minus_x90_gaussian_Q_wf_{qb}",
                },
            }
            for qb, val in QUBIT_CONSTANTS.items()
        },
        **{
            f"y180_gaussian_pulse_{qb}": {
                "operation": "control",
                "length": val["pi_len"],
                "waveforms": {
                    "I": f"y180_gaussian_I_wf_{qb}",
                    "Q": f"y180_gaussian_Q_wf_{qb}",
                },
            }
            for qb, val in QUBIT_CONSTANTS.items()
        },
        **{
            f"y90_gaussian_pulse_{qb}": {
                "operation": "control",
                "length": val["pi_len"],
                "waveforms": {
                    "I": f"y90_gaussian_I_wf_{qb}",
                    "Q": f"y90_gaussian_Q_wf_{qb}",
                },
            }
            for qb, val in QUBIT_CONSTANTS.items()
        },
        **{
            f"minus_y90_gaussian_pulse_{qb}": {
                "operation": "control",
                "length": val["pi_len"],
                "waveforms": {
                    "I": f"minus_y90_gaussian_I_wf_{qb}",
                    "Q": f"minus_y90_gaussian_Q_wf_{qb}",
                },
            }
            for qb, val in QUBIT_CONSTANTS.items()
        },
        **{
            f"reflectometry_readout_pulse_{tc}": {
                "operation": "measurement",
                "length": val["readout_len"],
                "waveforms": {
                    "single": f"reflectometry_readout_wf_{tc}",
                },
                "integration_weights": {
                    "cos": f"cosine_weights_{tc}",
                    "sin": f"sine_weights_{tc}",
                },
                "digital_marker": "ON",
            }
            for tc, val in TANK_CIRCUIT_CONSTANTS.items()
        },
        "const_pulse": {
            "operation": "control",
            "length": CONST_LEN,
            "waveforms": {
                "I": "const_wf",
                "Q": "zero_wf",
            },
        },
        "trigger_pulse": {
            "operation": "control",
            "length": 1000,
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "const_wf": {"type": "constant", "sample": CONST_AMP},
        "zero_wf": {"type": "constant", "sample": 0.0},
        **{
            f"reflectometry_readout_wf_{key}": {
                "type": "constant",
                "sample": val["readout_amp"],
            }
            for key, val in TANK_CIRCUIT_CONSTANTS.items()
        },
        **{
            f"{key}_step_wf": {"type": "constant", "sample": val["step_amp"]}
            for key, val in PLUNGER_CONSTANTS.items()
        },
        **{
            f"{key}_step_wf": {"type": "constant", "sample": val["step_amp"]}
            for key, val in BARRIER_CONSTANTS.items()
        },
        **{
            f"{key}_step_wf": {"type": "constant", "sample": val["step_amp"]}
            for key, val in PLUNGER_SD_CONSTANTS.items()
        },
        **{
            f"x90_I_wf_{key}": {
                "type": "arbitrary",
                "samples": waveforms[key + "_x90_I"].tolist(),
            }
            for key in QUBIT_CONSTANTS.keys()
        },
        **{
            f"x90_Q_wf_{key}": {
                "type": "arbitrary",
                "samples": waveforms[key + "_x90_Q"].tolist(),
            }
            for key in QUBIT_CONSTANTS.keys()
        },
        **{
            f"x180_I_wf_{key}": {
                "type": "arbitrary",
                "samples": waveforms[key + "_x180_I"].tolist(),
            }
            for key in QUBIT_CONSTANTS.keys()
        },
        **{
            f"x180_Q_wf_{key}": {
                "type": "arbitrary",
                "samples": waveforms[key + "_x180_Q"].tolist(),
            }
            for key in QUBIT_CONSTANTS.keys()
        },
        **{
            f"minus_x90_I_wf_{key}": {
                "type": "arbitrary",
                "samples": waveforms[key + "_minus_x90_I"].tolist(),
            }
            for key in QUBIT_CONSTANTS.keys()
        },
        **{
            f"minus_x90_Q_wf_{key}": {
                "type": "arbitrary",
                "samples": waveforms[key + "_minus_x90_Q"].tolist(),
            }
            for key in QUBIT_CONSTANTS.keys()
        },
        **{
            f"y90_I_wf_{key}": {
                "type": "arbitrary",
                "samples": waveforms[key + "_y90_I"].tolist(),
            }
            for key in QUBIT_CONSTANTS.keys()
        },
        **{
            f"y90_Q_wf_{key}": {
                "type": "arbitrary",
                "samples": waveforms[key + "_y90_Q"].tolist(),
            }
            for key in QUBIT_CONSTANTS.keys()
        },
        **{
            f"y180_I_wf_{key}": {
                "type": "arbitrary",
                "samples": waveforms[key + "_y180_I"].tolist(),
            }
            for key in QUBIT_CONSTANTS.keys()
        },
        **{
            f"y180_Q_wf_{key}": {
                "type": "arbitrary",
                "samples": waveforms[key + "_y180_Q"].tolist(),
            }
            for key in QUBIT_CONSTANTS.keys()
        },
        **{
            f"minus_y90_I_wf_{key}": {
                "type": "arbitrary",
                "samples": waveforms[key + "_minus_y90_I"].tolist(),
            }
            for key in QUBIT_CONSTANTS.keys()
        },
        **{
            f"minus_y90_Q_wf_{key}": {
                "type": "arbitrary",
                "samples": waveforms[key + "_minus_y90_Q"].tolist(),
            }
            for key in QUBIT_CONSTANTS.keys()
        },
    },
    "digital_waveforms": {
        "ON": {"samples": [(1, 0)]},
    },
    "integration_weights": {
        **{
            f"cosine_weights_{tc}": {
                "cosine": [(1.0, val["readout_len"])],
                "sine": [(0.0, val["readout_len"])],
            }
            for tc, val in TANK_CIRCUIT_CONSTANTS.items()
        },
        **{
            f"sine_weights_{tc}": {
                "cosine": [(0.0, val["readout_len"])],
                "sine": [(1.0, val["readout_len"])],
            }
            for tc, val in TANK_CIRCUIT_CONSTANTS.items()
        },
    },
    "mixers": {
        **{
            f"mixer_{qb}": [
                {
                    "intermediate_frequency": val["IF"],
                    "lo_frequency": val["LO"],
                    "correction": IQ_imbalance(val["mixer_g"], val["mixer_phi"]),
                },
            ]
            for qb, val in QUBIT_CONSTANTS.items()
        },
    },
}

# %%
