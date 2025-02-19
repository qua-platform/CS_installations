"""
QUA-Config supporting OPX1000 w/ LF-FEM & External Mixers
"""

from pathlib import Path
import numpy as np
from qualang_tools.config.waveform_tools import drag_gaussian_pulse_waveforms
from qualang_tools.units import unit

######################
# Network parameters #
######################
# qop_ip = "172.17.2.121"  # Write the QM router IP address
qop_ip = "172.16.33.107"  # Write the QM router IP address
# cluster_name = 'Beta_17'  # Write your cluster_name if version >= QOP220
cluster_name = 'Cluster_1'  # Write your cluster_name if version >= QOP220
qop_port = None  # Write the QOP port if version < QOP220

#####################
# OPX configuration #
#####################
con = "con1"
lf_fem = 3  # Should be the LF-FEM index
mw_fem = 1  # Should be the MW-FEM index

#############################################
#                  Qubits                   #
#############################################
u = unit(coerce_to_integer=True)

sampling_rate = int(1e9)  # or, int(2e9)


#############################################
#                Resonators                 #
#############################################
resonator_LO = 4.8 * u.GHz
resonator_IF = 10 * u.MHz
resonator_power = 1

readout_len = 1_000
readout_amp = 0.1

time_of_flight = 24
depletion_time = 2 * u.us

#############################################
#                  Config                   #
#############################################

config = {
    "version": 1,
    "controllers": {
        'con1': {
            "type": "opx1000",
            "fems": {
                mw_fem: {
                    # The keyword "band" refers to the following frequency bands:
                    #   1: (50 MHz - 5.5 GHz)
                    #   2: (4.5 GHz - 7.5 GHz)
                    #   3: (6.5 GHz - 10.5 GHz)
                    # Note that the "coupled" ports O1 & I1, O2 & O3, O4 & O5, O6 & O7, and O8 & I2
                    # must be in the same band, or in bands 1 & 3 (that is, if you assign band 2 to one of the coupled ports, the other must use the same band).
                    # The keyword "full_scale_power_dbm" is the maximum power of
                    # normalized pulse waveforms in [-1,1]. To convert to voltage,
                    #   power_mw = 10**(full_scale_power_dbm / 10)
                    #   max_voltage_amp = np.sqrt(2 * power_mw * 50 / 1000)
                    #   amp_in_volts = waveform * max_voltage_amp
                    #   ^ equivalent to OPX+ amp
                    # Its range is -41dBm to +10dBm with 3dBm steps.
                    "type": "MW",
                    "analog_outputs": {
                        8: {
                            "band": 2,
                            "full_scale_power_dbm": resonator_power,
                            "upconverters": {1: {"frequency": resonator_LO}},
                        },  # resonator
                    },
                    "digital_outputs": {},
                    "analog_inputs": {
                        2: {"band": 2, "downconverter_frequency": resonator_LO},  # for down-conversion
                    },
                },
                lf_fem: {
                    "type": "LF",
                    "analog_outputs": {
                        # I qubit
                        7: {
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
                            "upsampling_mode": "mw",
                        },
                        # Q qubit
                        8: {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": sampling_rate,
                            "upsampling_mode": "mw",
                        },
                    },
                    "digital_outputs": {},
                    "analog_inputs": {
                        # I from down-conversion
                        1: {"offset": -0.0028453466796875, "gain_db": 0, "sampling_rate": sampling_rate},
                        # Q from down-conversion
                        2: {"offset": -0.0045774462890625, "gain_db": 0, "sampling_rate": sampling_rate},
                    },
                }
            },
        }
    },
    "elements": {
        "mw_el": {
            "MWInput": {
                "port": (con, mw_fem, 8),
                "upconverter": 1,
            },
            "intermediate_frequency": resonator_IF,
            "operations": {
                "zero": "mw_zero_pulse",
                "readout": "mw_readout_pulse",
            },
            "MWOutput": {
                "port": (con, mw_fem, 2),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
        "mw_el_twin": {
            "MWInput": {
                "port": (con, mw_fem, 8),
                "upconverter": 1,
            },
            "intermediate_frequency": resonator_IF,
            "operations": {
                "zero": "mw_zero_pulse",
                "readout": "mw_readout_pulse",
            },
            "MWOutput": {
                "port": (con, mw_fem, 2),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
        "rr1": {
            "singleInput": {
                "port": (con, lf_fem, 7),
            },
            "intermediate_frequency": resonator_IF,
            "operations": {
                "readout": "readout_pulse",
                "zero": "zero_pulse",
            },
            "outputs": {
                "out1": (con, lf_fem, 1),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
        "rr1_twin": {
            "singleInput": {
                "port": (con, lf_fem, 7),
            },
            "intermediate_frequency": resonator_IF,
            "operations": {
                "readout": "readout_pulse",
                "zero": "zero_pulse",
            },
            "outputs": {
                "out1": (con, lf_fem, 1),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
        "rr2": {
            "singleInput": {
                "port": (con, lf_fem, 8),
            },
            "intermediate_frequency": resonator_IF,
            "operations": {
                "readout": "readout_pulse",
                "zero": "zero_pulse",
            },
            "outputs": {
                "out2": (con, lf_fem, 2),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
        "rr2_twin": {
            "singleInput": {
                "port": (con, lf_fem, 8),
            },
            "intermediate_frequency": resonator_IF,
            "operations": {
                "readout": "readout_pulse",
                "zero": "zero_pulse",
            },
            "outputs": {
                "out2": (con, lf_fem, 2),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
    },
    "pulses": {
        "zero_pulse": {
            "operation": "measurement",
            "length": readout_len,
            "waveforms": {
                "single": "zero_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
                "minus_sin": "minus_sine_weights",
            },
            "digital_marker": "ON",
        },
        "mw_zero_pulse": {
            "operation": "measurement",
            "length": readout_len,
            "waveforms": {
                "I": "zero_wf",
                "Q": "zero_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
                "minus_sin": "minus_sine_weights",
            },
            "digital_marker": "ON",
        },
        "readout_pulse": {
            "operation": "measurement",
            "length": readout_len,
            "waveforms": {
                "single": "readout_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
                "minus_sin": "minus_sine_weights",
            },
            "digital_marker": "ON",
        },
        "mw_readout_pulse": {
            "operation": "measurement",
            "length": readout_len,
            "waveforms": {
                "I": "readout_wf",
                "Q": "zero_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
                "minus_sin": "minus_sine_weights",
            },
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "readout_wf": {"type": "constant", "sample": readout_amp},
        "zero_wf": {"type": "constant", "sample": 0.0},
    },
    "digital_waveforms": {
        "ON": {"samples": [(1, 0)]},
    },
    "integration_weights": {
        "cosine_weights": {
            "cosine": [(1.0, readout_len)],
            "sine": [(0.0, readout_len)],
        },
        "sine_weights": {
            "cosine": [(0.0, readout_len)],
            "sine": [(1.0, readout_len)],
        },
        "minus_sine_weights": {
            "cosine": [(0.0, readout_len)],
            "sine": [(-1.0, readout_len)],
        },
    },
}