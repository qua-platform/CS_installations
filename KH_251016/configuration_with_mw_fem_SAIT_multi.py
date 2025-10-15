"""
QUA-Config supporting OPX1000 w/ MW-FEM
"""
from pathlib import Path
import numpy as np
import plotly.io as pio
from qualang_tools.config.waveform_tools import drag_gaussian_pulse_waveforms
from qualang_tools.units import unit
from test import visualize_opx1000_config

pio.renderers.default = "browser"
u = unit(coerce_to_integer=True)
out1_band = out1_power = out1_up1_LO = out2_band = out2_power = out2_up1_LO \
= out3_band = out3_power = out3_up1_LO = out4_band = out4_power = out4_up1_LO \
= out5_band = out5_power = out5_up1_LO = out6_band = out6_power = out6_up1_LO \
= out7_band = out7_power = out7_up1_LO = out8_band = out8_power = out8_up1_LO \
= in1_band = in1_LO = in2_band = in2_LO = in1_gain_db = in2_gain_db = 1

############################################
# Automatically assign the bands for ports #
############################################
def get_band(freq):
    """Determine the MW fem DAC band corresponding to a given frequency.
    Args:
        freq (float): The frequency in Hz.
    Returns:
        int: The Nyquist band number.
            - 1 if 50 MHz <= freq < 5.5 GHz
            - 2 if 4.5 GHz <= freq < 7.5 GHz
            - 3 if 6.5 GHz <= freq <= 10.5 GHz
    Raises:
        ValueError: If the frequency is outside the MW fem bandwidth [50 MHz, 10.5 GHz].
    """
    if 50e6 <= freq < 5.0e9:
        return 1
    elif 5.0e9 <= freq < 7.0e9:
        return 2
    elif 7.0e9 <= freq <= 10.5e9:
        return 3
    else:
        raise ValueError(f"The specified frequency {freq} Hz is outside of the MW fem bandwidth [50 MHz, 10.5 GHz]")

######################
# Network parameters #
###################### 	
qop_ip = "172.16.33.115"  # Write the QM router IP address
cluster_name = "CS_3"  # Write your cluster_name if version >= QOP220
qop_port = None  # Write the QOP port if version < QOP220
con = "con1"

# MW-FEM slot number (1, 2, 3, ..)
fem_1 = 1 
fem_2 = 2 
fem_3 = 3 
fem_4 = 4 

res1_out_fem = fem_1
res1_in_fem = fem_1
res1_out_port, res1_in_port = 1, 1
res1_in_gain_db = 0 

res2_out_fem = fem_1
res2_in_fem = fem_1
res2_out_port, res2_in_port = 8, 2
res2_in_gain_db = 0 

q1_out_fem = fem_1
q1_out_port = 2

save_dir = Path(__file__).parent.resolve() / "Data"
save_dir.mkdir(exist_ok=True)

#############################################
#                Resonators                 #
#############################################
res1_LO = 5.5 * u.GHz
res1_IF = 60 * u.MHz
res1_power = -11  # power in dBm (steps of 3 dB)
res3_IF = 120 * u.MHz

res2_LO = 6.5 * u.GHz
res2_IF = 60 * u.MHz
res2_power = -11  # power in dBm (steps of 3 dB)

readout_len = 1000
readout_amp = 1.0

time_of_flight = 28
depletion_time = 100 * u.us

#############################################
#                  Qubits                   #
#############################################
q1_LO = 7 * u.GHz
q1_IF = 50 * u.MHz
q1_power = 1  # power in dBm at waveform amp = 1 (steps of 3 dB)
q1_T1 = int(10 * u.us)
q1_thermal_time = 5 * q1_T1

# Continuous wave
const_len = 100
const_amp = 0.03
# Saturation_pulse
saturation_len = 10 * u.us
saturation_amp = 0.03

#############################################
#                  Config                   #
#############################################
globals()["out{}_band".format(res1_out_port)] = get_band(res1_LO + res1_IF)
globals()["out{}_up1_LO".format(res1_out_port)] = res1_LO
if res1_out_port == 1:
    out1_band = in1_band = get_band(res1_LO + res1_IF)
    out1_up1_LO = in1_LO = res1_LO
elif res1_out_port in [2, 3]:
    out2_band = out3_band = get_band(res1_LO + res1_IF)
    out2_up1_LO = out3_up1_LO = res1_LO
elif res1_out_port in [4,5]:
    out4_band = out5_band = get_band(res1_LO + res1_IF)
    out4_up1_LO = out5_up1_LO = res1_LO
elif res1_out_port in [6,7]:
    out6_band = out7_band = get_band(res1_LO + res1_IF)
    out6_up1_LO = out7_up1_LO = res1_LO
elif res1_out_port == 8:
    out8_band = in2_band = get_band(res1_LO + res1_IF)
    out8_up1_LO = in2_LO = res1_LO
globals()["out{}_power".format(res1_out_port)] = res1_power
globals()["in{}_gain_db".format(res1_in_port)] = res1_in_gain_db
if res1_in_port == 1:
    out1_band = in1_band = globals()["out{}_band".format(res1_out_port)]
    out1_up1_LO = in1_LO = res1_LO
elif res1_in_port == 2:
    out8_band = in2_band = globals()["out{}_band".format(res1_out_port)]
    out8_up1_LO = in2_LO = res1_LO

globals()["out{}_band".format(res2_out_port)] = get_band(res2_LO + res2_IF)
globals()["out{}_up1_LO".format(res2_out_port)] = res2_LO
if res2_out_port == 1:
    out1_band = in1_band = get_band(res2_LO + res2_IF)
    out1_up1_LO = in1_LO = res2_LO
elif res2_out_port in [2, 3]:
    out2_band = out3_band = get_band(res2_LO + res2_IF)
    out2_up1_LO = out3_up1_LO = res2_LO
elif res2_out_port in [4,5]:
    out4_band = out5_band = get_band(res2_LO + res2_IF)
    out4_up1_LO = out5_up1_LO = res2_LO
elif res2_out_port in [6,7]:
    out6_band = out7_band = get_band(res2_LO + res2_IF)
    out6_up1_LO = out7_up1_LO = res2_LO
elif res2_out_port == 8:
    out8_band = in2_band = get_band(res2_LO + res2_IF)
    out8_up1_LO = in2_LO = res2_LO
globals()["out{}_power".format(res2_out_port)] = res2_power
globals()["in{}_gain_db".format(res2_in_port)] = res2_in_gain_db
if res2_in_port == 1:
    out1_band = in1_band = globals()["out{}_band".format(res2_out_port)]
    out1_up1_LO = in1_LO = res2_LO
elif res2_in_port == 2:
    out8_band = in2_band = globals()["out{}_band".format(res2_out_port)]
    out8_up1_LO = in2_LO = res2_LO


globals()["out{}_power".format(q1_out_port)] = q1_power
globals()["out{}_up1_LO".format(q1_out_port)] = q1_LO
if q1_out_port == 1:
    out1_band = in1_band = get_band(q1_LO + q1_IF)
    out1_up1_LO = in1_LO = q1_LO
elif q1_out_port in [2, 3]:
    out2_band = out3_band = get_band(q1_LO + q1_IF)
    out2_up1_LO = out3_up1_LO = q1_LO
elif q1_out_port in [4,5]:
    out4_band = out5_band = get_band(q1_LO + q1_IF)
    out4_up1_LO = out5_up1_LO = q1_LO
elif q1_out_port in [6,7]:
    out6_band = out7_band = get_band(q1_LO + q1_IF)
    out6_up1_LO = out7_up1_LO = q1_LO
elif q1_out_port == 8:
    out8_band = in2_band = get_band(q1_LO + q1_IF)
    out8_up1_LO = in2_LO = q1_LO

config = {
    "version": 1,
    "controllers": {
        con: {
            "type": "opx1000",
            "fems": {                
                fem_1: {
                    "type": "MW",
                    "analog_outputs": {
                        1: {
                            "band": out1_band,
                            "full_scale_power_dbm": out1_power,
                            "upconverters": {1: {"frequency": out1_up1_LO}},
                        },  
                        2: {
                            "band": out2_band,
                            "full_scale_power_dbm": out2_power,
                            "upconverters": {1: {"frequency": out2_up1_LO}},
                        },  
                        3: {
                            "band": out3_band,
                            "full_scale_power_dbm": out3_power,
                            "upconverters": {1: {"frequency": out3_up1_LO}},
                        },  
                        4: {
                            "band": out4_band,
                            "full_scale_power_dbm": out4_power,
                            "upconverters": {1: {"frequency": out4_up1_LO}},
                        },  
                        5: {
                            "band": out5_band,
                            "full_scale_power_dbm": out5_power,
                            "upconverters": {1: {"frequency": out5_up1_LO}},
                        },  
                        6: {
                            "band": out6_band,
                            "full_scale_power_dbm": out6_power,
                            "upconverters": {1: {"frequency": out6_up1_LO}},
                        },  
                        7: {
                            "band": out7_band,
                            "full_scale_power_dbm": out7_power,
                            "upconverters": {1: {"frequency": out7_up1_LO}},
                        },  
                        8: {
                            "band": out8_band,
                            "full_scale_power_dbm": out8_power,
                            "upconverters": {1: {"frequency": out8_up1_LO}},
                        },  
                    },
                    "digital_outputs": {},
                    "analog_inputs": {
                            1: {
                            "band": in1_band, 
                            "downconverter_frequency": in1_LO,
                            "gain_db": in1_gain_db},  
                            2: {
                            "band": in2_band, 
                            "downconverter_frequency": in2_LO,
                            "gain_db": in2_gain_db},  
                    },
                },
            },
        },
    },
    "elements": {
        "resonator_1": {
            "MWInput": {
                "port": (con, res1_out_fem, res1_out_port),
                "upconverter": 1,
            },
            "intermediate_frequency": res1_IF,
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse",
            },
            "MWOutput": {
                "port": (con, res1_in_fem, res1_in_port),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
        "resonator_2": {
            "MWInput": {
                "port": (con, res2_out_fem, res2_out_port),
                "upconverter": 1,
            },
            "intermediate_frequency": res2_IF,
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse",
            },
            "MWOutput": {
                "port": (con, res2_in_fem, res2_in_port),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
        "resonator_3": {
            "MWInput": {
                "port": (con, res1_out_fem, res1_out_port),
                "upconverter": 1,
            },
            "intermediate_frequency": res3_IF,
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse",
            },
            "MWOutput": {
                "port": (con, res1_in_fem, res1_in_port),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
        "qubit": {
            "MWInput": {
                "port": (con, q1_out_fem, q1_out_port),
                "upconverter": 1,
            },
            "intermediate_frequency": q1_IF,
            "operations": {
                "cw": "const_pulse",
                "saturation": "saturation_pulse",
            },
        },
    },
    "pulses": {
        "const_pulse": {
            "operation": "control",
            "length": const_len,
            "waveforms": {
                "I": "const_wf",
                "Q": "zero_wf",
            },
        },
        "readout_pulse": {
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
        "saturation_pulse": {
            "operation": "control",
            "length": saturation_len,
            "waveforms": {"I": "saturation_drive_wf", "Q": "zero_wf"},
        }
    },
    "waveforms": {
        "const_wf": {"type": "constant", "sample": const_amp},
        "zero_wf": {"type": "constant", "sample": 0.0},
        "readout_wf": {"type": "constant", "sample": readout_amp},
        "saturation_drive_wf": {"type": "constant", "sample": saturation_amp},
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
        }
    },
}

if __name__ == "__main__":
    visualize_opx1000_config(config)