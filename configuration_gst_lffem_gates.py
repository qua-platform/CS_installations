# %%
import numpy as np
from qualang_tools.units import unit
from scipy.signal.windows import gaussian

#######################
# AUXILIARY FUNCTIONS #
#######################
u = unit(coerce_to_integer=True)


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
con = "con1"
lf_fem = 5  # Should be the LF-FEM index, e.g., 1
sampling_rate = 1e9

step_length = 16
P1_step_amp = 0.25
P2_step_amp = 0.25
hold_offset_duration = 4

######################
#       READOUT      #
######################
# Reflectometry
resonator_IF = 150 * u.MHz
reflectometry_readout_len = 1 * u.us
reflectometry_readout_amp = 30 * u.mV

# Time of flight
time_of_flight = 28


######################
#    QUBIT PULSES    #
######################
qubit_IF = 0 * u.MHz

# CW pulse
const_len = 48  # in ns
const_amp = 0.3  # in V
x90_amp = 0.2
y90_amp = 0.1

#############################################
#                  Config                   #
#############################################
config = {
    "version": 1,
    "controllers": {
        con: {
            "type": "opx1000",
            "fems": {
                # mw_fem: {
                #     # The keyword "band" refers to the following frequency bands:
                #     #   1: (50 MHz - 5.5 GHz)
                #     #   2: (4.5 GHz - 7.5 GHz)
                #     #   3: (6.5 GHz - 10.5 GHz)
                #     # Note that the "coupled" ports O1 & I1, O2 & O3, O4 & O5, O6 & O7, O8 & O1
                #     # must be in the same band, or in bands 1 & 3.
                #     # The keyword "full_scale_power_dbm" is the maximum power of
                #     # normalized pulse waveforms in [-1,1]. To convert to voltage,
                #     #   power_mw = 10**(full_scale_power_dbm / 10)
                #     #   max_voltage_amp = np.sqrt(2 * power_mw * 50 / 1000)
                #     #   amp_in_volts = waveform * max_voltage_amp
                #     #   ^ equivalent to OPX+ amp
                #     # Its range is -41dBm to +10dBm with 3dBm steps.
                #     "type": "MW",
                #     "analog_outputs": {
                #         1: {"band": 1, "full_scale_power_dbm": qubit_power},  # qubit
                #     },
                #     "digital_outputs": {},
                # },
                lf_fem: {
                    "type": "LF",
                    "analog_outputs": {
                        # P1
                        1: {
                            # DC Offset applied to the analog output at the beginning of a program.
                            "offset": 0.0,
                            # The "output_mode" can be used to tailor the max voltage and frequency bandwidth, i.e.,
                            #   "direct":    1Vpp (-0.5V to 0.5V), 750MHz bandwidth (default)
                            #   "amplified": 5Vpp (-2.5V to 2.5V), 330MHz bandwidth
                            # Note, 'offset' takes absolute values, e.g., if in amplified mode and want to output 2.0 V, then set "offset": 2.0
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
                            "upsampling_mode": "pulse",
                        },
                        # qubit
                        4: {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": sampling_rate,
                            "upsampling_mode": "mw",
                        },
                        # P1
                        5: {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": sampling_rate,
                            "upsampling_mode": "pulse",
                        },
                        # P2
                        6: {
                            "offset": 0.0,
                            "output_mode": "direct",
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
                    "digital_outputs": {},
                    "analog_inputs": {
                        1: {
                            "offset": 0.0,
                            "gain_db": 0,
                            "sampling_rate": sampling_rate,
                        },  # RF reflectometry input
                        2: {
                            "offset": 0.0,
                            "gain_db": 0,
                            "sampling_rate": sampling_rate,
                        },  # RF reflectometry input
                    },
                },
            },
        },
    },
    "elements": {
        "qubit": {
            "singleInput": {
                "port": (con, lf_fem, 4),
            },
            "intermediate_frequency": qubit_IF,
            "operations": {
                "const": "const_pulse",
                "x90": "x90_pulse",
                "y90": "y90_pulse",
            },
            "thread": "a",
        },
        "qubit_twin": {
            "singleInput": {
                "port": (con, lf_fem, 4),
            },
            "intermediate_frequency": qubit_IF,
            "operations": {
                "const": "const_pulse",
                "x90": "minus_x90_pulse",
                "y90": "minus_y90_pulse",
            },
            "thread": "b",
        },
        "P1": {
            "singleInput": {
                "port": (con, lf_fem, 5),
            },
            "operations": {
                "step": "P1_step_pulse",
            },
        },
        "P1_sticky": {
            "singleInput": {
                "port": (con, lf_fem, 5),
            },
            "sticky": {"analog": True, "duration": hold_offset_duration},
            "operations": {
                "step": "P1_step_pulse",
            },
        },
        "P2": {
            "singleInput": {
                "port": (con, lf_fem, 6),
            },
            "operations": {
                "step": "P2_step_pulse",
            },
        },
        "P2_sticky": {
            "singleInput": {
                "port": (con, lf_fem, 6),
            },
            "sticky": {"analog": True, "duration": hold_offset_duration},
            "operations": {
                "step": "P1_step_pulse",
            },
        },
        "tank_circuit": {
            "singleInput": {
                "port": (con, lf_fem, 8),
            },
            "intermediate_frequency": resonator_IF,
            "operations": {
                "readout": "reflectometry_readout_pulse",
            },
            "outputs": {
                "out1": (con, lf_fem, 1),
                "out2": (con, lf_fem, 2),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
    },
    "pulses": {
        "const_pulse": {
            "operation": "control",
            "length": const_len,
            "waveforms": {
                "single": "const_wf",
            },
        },
        "x90_pulse": {
            "operation": "control",
            "length": const_len,
            "waveforms": {
                "single": "x90_wf",
            },
        },
        "y90_pulse": {
            "operation": "control",
            "length": const_len,
            "waveforms": {
                "single": "y90_wf",
            },
        },
        "minus_x90_pulse": {
            "operation": "control",
            "length": const_len,
            "waveforms": {
                "single": "minus_x90_wf",
            },
        },
        "minus_y90_pulse": {
            "operation": "control",
            "length": const_len,
            "waveforms": {
                "single": "minus_y90_wf",
            },
        },
        "P1_step_pulse": {
            "operation": "control",
            "length": step_length,
            "waveforms": {
                "single": "P1_step_wf",
            },
        },
        "P2_step_pulse": {
            "operation": "control",
            "length": step_length,
            "waveforms": {
                "single": "P2_step_wf",
            },
        },
        "reflectometry_readout_pulse": {
            "operation": "measurement",
            "length": reflectometry_readout_len,
            "waveforms": {
                "single": "readout_pulse_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
            },
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "zero_wf": {"type": "constant", "sample": 0.0},
        "const_wf": {"type": "constant", "sample": const_amp},
        "P1_step_wf": {"type": "constant", "sample": P1_step_amp},
        "P2_step_wf": {"type": "constant", "sample": P2_step_amp},
        "x90_wf": {"type": "constant", "sample": x90_amp},
        "y90_wf": {"type": "constant", "sample": y90_amp},
        "minus_x90_wf": {"type": "constant", "sample": -x90_amp},
        "minus_y90_wf": {"type": "constant", "sample": -y90_amp},
        "readout_pulse_wf": {"type": "constant", "sample": reflectometry_readout_amp},
    },
    "digital_waveforms": {
        "ON": {"samples": [(1, 0)]},
    },
    "integration_weights": {
        "constant_weights": {
            "cosine": [(1, reflectometry_readout_len)],
            "sine": [(0.0, reflectometry_readout_len)],
        },
        "cosine_weights": {
            "cosine": [(1.0, reflectometry_readout_len)],
            "sine": [(0.0, reflectometry_readout_len)],
        },
        "sine_weights": {
            "cosine": [(0.0, reflectometry_readout_len)],
            "sine": [(1.0, reflectometry_readout_len)],
        },
    },
}

# %%
