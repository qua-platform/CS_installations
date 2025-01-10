import numpy as np
from scipy.signal.windows import gaussian
from qualang_tools.config.waveform_tools import drag_gaussian_pulse_waveforms, flattop_cosine_waveform
from qualang_tools.units import unit
from qualang_tools.plot import interrupt_on_close
from qualang_tools.results import progress_counter, fetching_tool

#############
# VARIABLES #
#############
u = unit(coerce_to_integer=True)

sampling_rate = int(1e9)  # or, int(2e9)


qop_ip = "172.16.33.107"  # Write the QM router IP address
cluster_name = "Beta_8"  # Write your cluster_name if version >= QOP220
qop_port = 9510  # Write the QOP port if version < QOP220

stimulus_LO = 4.444444444e9
stimulus_IF = 35* u.MHz

#############################################
#                  Qubits                   #
#############################################
qubit_LO = 3.83357 * u.GHz
qubit_IF = 100 * u.MHz
qd_len = 120*u.ns
mixer_qubit_g = 0
mixer_qubit_phi = 0.0

qubit_T1 = int(22.5 * u.us)
thermalization_time = 4 * qubit_T1

# Continuous wave
const_len = 100
const_amp = 0.1
# Saturation_pulse
saturation_len = 10 * u.us
saturation_amp = 0.1
# Square pi pulse
square_pi_len = 120
square_pi_amp = 0.1
# Drag pulses
drag_coef = 0
anharmonicity = -200 * u.MHz
AC_stark_detuning = 0 * u.MHz

x180_len = 120
x180_sigma = x180_len / 5
x180_amp = 0.4355
x180_wf, x180_der_wf = np.array(
    drag_gaussian_pulse_waveforms(x180_amp, x180_len, x180_sigma, drag_coef, anharmonicity, AC_stark_detuning)
)
x180_I_wf = x180_wf
x180_Q_wf = x180_der_wf
# No DRAG when alpha=0, it's just a gaussian.

x90_len = x180_len
x90_sigma = x90_len / 5
x90_amp = x180_amp / 2
x90_wf, x90_der_wf = np.array(
    drag_gaussian_pulse_waveforms(x90_amp, x90_len, x90_sigma, drag_coef, anharmonicity, AC_stark_detuning)
)
x90_I_wf = x90_wf
x90_Q_wf = x90_der_wf
# No DRAG when alpha=0, it's just a gaussian.

minus_x90_len = x180_len
minus_x90_sigma = minus_x90_len / 5
minus_x90_amp = -x90_amp
minus_x90_wf, minus_x90_der_wf = np.array(
    drag_gaussian_pulse_waveforms(
        minus_x90_amp,
        minus_x90_len,
        minus_x90_sigma,
        drag_coef,
        anharmonicity,
        AC_stark_detuning,
    )
)
minus_x90_I_wf = minus_x90_wf
minus_x90_Q_wf = minus_x90_der_wf
# No DRAG when alpha=0, it's just a gaussian.

y180_len = x180_len
y180_sigma = y180_len / 5
y180_amp = x180_amp
y180_wf, y180_der_wf = np.array(
    drag_gaussian_pulse_waveforms(y180_amp, y180_len, y180_sigma, drag_coef, anharmonicity, AC_stark_detuning)
)
y180_I_wf = (-1) * y180_der_wf
y180_Q_wf = y180_wf
# No DRAG when alpha=0, it's just a gaussian.

y90_len = x180_len
y90_sigma = y90_len / 5
y90_amp = y180_amp / 2
y90_wf, y90_der_wf = np.array(
    drag_gaussian_pulse_waveforms(y90_amp, y90_len, y90_sigma, drag_coef, anharmonicity, AC_stark_detuning)
)
y90_I_wf = (-1) * y90_der_wf
y90_Q_wf = y90_wf
# No DRAG when alpha=0, it's just a gaussian.

minus_y90_len = y180_len
minus_y90_sigma = minus_y90_len / 5
minus_y90_amp = -y90_amp
minus_y90_wf, minus_y90_der_wf = np.array(
    drag_gaussian_pulse_waveforms(
        minus_y90_amp,
        minus_y90_len,
        minus_y90_sigma,
        drag_coef,
        anharmonicity,
        AC_stark_detuning,
    )
)
minus_y90_I_wf = (-1) * minus_y90_der_wf
minus_y90_Q_wf = minus_y90_wf
# No DRAG when alpha=0, it's just a gaussian.




const_len = 200
const_amp = 0.25
mixer_stimulus_g = 0.1
mixer_stimulus_phi = 3.0


# Resonator
resonator_LO = 7.7 * u.GHz  # Used only for mixer correction and frequency rescaling for plots or computation
resonator_IF = 35 * u.MHz
mixer_resonator_g = 0.0
mixer_resonator_phi = 0.0
readout_len = 5000


time_of_flight = 324

# Flux line
const_flux_len = 16
const_flux_amp = 0.25

ramp_flux_len = 100_000
custom_wf = [0.0]*ramp_flux_len

resonator_LO = 5.5 * u.GHz
resonator_IF = 60 * u.MHz
resonator_power = 1  # power in dBm at waveform amp = 1

qubit_LO = 7.4 * u.GHz
qubit_IF = 110 * u.MHz
qubit_power = 1  # power in dBm at waveform amp = 1 (steps of 3 dB)

max_frequency_point = 0.0



def create_config(readout_len, dc_flux_reset,readout_amp,const_len,qd_len, x180_amplitude):
    x180_len = 120
    x180_sigma = x180_len / 5
    x180_amp = x180_amplitude
    x180_wf, x180_der_wf = np.array(
        drag_gaussian_pulse_waveforms(x180_amp, x180_len, x180_sigma, drag_coef, anharmonicity, AC_stark_detuning)
    )
    x180_I_wf = x180_wf
    x180_Q_wf = x180_der_wf

    mw_fem = 1
    lf_fem = 5
    
    config1 = {
    "version": 1,
    "controllers": {
        "con1": {
            "type": "opx1000",
            "fems": {
                mw_fem: {
                    # The keyword "band" refers to the following frequency bands:
                    #   1: (50 MHz - 5.5 GHz)
                    #   2: (4.5 GHz - 7.5 GHz)
                    #   3: (6.5 GHz - 10.5 GHz)
                    # Note that the "coupled" ports O1 & I1, O2 & O3, O4 & O5, O6 & O7, O8 & O1
                    # must be in the same band, or in bands 1 & 3.
                    # The keyword "full_scale_power_dbm" is the maximum power of
                    # normalized pulse waveforms in [-1,1]. To convert to voltage,
                    #   power_mw = 10**(full_scale_power_dbm / 10)
                    #   max_voltage_amp = np.sqrt(2 * power_mw * 50 / 1000)
                    #   amp_in_volts = waveform * max_voltage_amp
                    #   ^ equivalent to OPX+ amp
                    # Its range is -41dBm to +10dBm with 3dBm steps.
                    "type": "MW",
                    "analog_outputs": {
                        4: {
                            "full_scale_power_dbm": resonator_power,
                            "band": 2,
                            "upconverter_frequency": resonator_LO,
                        },  # resonator
                        2: {"full_scale_power_dbm": qubit_power, "band": 2, "upconverter_frequency": qubit_LO},  # qubit
                    },
                    "digital_outputs": {},
                    "analog_inputs": {
                        1: {"band": 2, "downconverter_frequency": resonator_LO},  # I from down-conversion
                    },
                },
                lf_fem: {
                    "type": "LF",
                    "analog_outputs": {
                        # Flux line
                        5: {
                            "offset": max_frequency_point,
                            # The "output_mode" can be used to tailor the max voltage and frequency bandwidth, i.e.,
                            #   "direct":    1Vpp (-0.5V to 0.5V), 750MHz bandwidth (default)
                            #   "amplified": 5Vpp (-2.5V to 2.5V), 330MHz bandwidth
                            # Note, 'offset' takes absolute values, e.g., if in amplified mode and want to output 2.0 V, then set "offset": 2.0
                            "output_mode": "amplified",
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
                    },
                    "digital_outputs": {
                        1: {},
                    },
                },
            },
        },
    },
    "elements": {
        "stimulus": {
            "mixInputs": {
                "I": ("con1", 1),
                "Q": ("con1", 2),
                "lo_frequency": stimulus_LO,
                "mixer": "mixer_stimulus",
            },
            "intermediate_frequency": stimulus_IF,
            "operations": {
                "cw": "const_pulse",
            },
            "outputs": {
                "out1": ("con1", 2),
                "out2": ("con1", 2),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },


        # "qdrive": {
            # "mixInputs": {
                # "I": ("con1", 8),
                # "Q": ("con1", 10),
                # "lo_frequency": qubit_LO,
                # "mixer": "mixer_qubit",
            # },
            # "intermediate_frequency": qubit_IF,
            # "operations": {
                # "qdrive": "qd_pulse",
            # },
        # },
        
        "qubit": {
            "mixInputs": {
                "I": ("con1", 10),
                "Q": ("con1", 8),
                "lo_frequency": qubit_LO,
                "mixer": "mixer_qubit",
            },
            "intermediate_frequency": qubit_IF,
            "operations": {
                "cw": "const_pulse",
                "saturation": "saturation_pulse",
                "pi": "square_pi_pulse",
                "pi_half": "square_pi_half_pulse",
                "x90": "x90_pulse",
                "x180": "x180_pulse",
                "-x90": "-x90_pulse",
                "y90": "y90_pulse",
                "y180": "y180_pulse",
                "-y90": "-y90_pulse",
            },
        },

        "resonator": {
            "mixInputs": {
                "I": ("con1", 3),
                "Q": ("con1", 4),
                "lo_frequency": resonator_LO,
                "mixer": "mixer_resonator",
            },
            "intermediate_frequency": resonator_IF,
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse",
            },
            "outputs": {
                "out1": ("con1", 1),
                "out2": ("con1", 1),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },



        "fast_flux_line": {
            "singleInput": {
                "port": ("con1", 5),
            },
            "hold_offset": {"duration": 1},  # in clock cycles (4ns)
            "operations": {
                "const": "const_flux_pulse",
            },

        },


        "wait_element": {
            "singleInput": {
                "port": ("con1", 5),
            },
            "hold_offset": {"duration": 1},  # in clock cycles (4ns)
            "operations": {
                "const": "const_flux_pulse",
            },

        },



        "dc_flux_line": {
            "singleInput": {
                "port": ("con1", 6),
            },
            "hold_offset": {"duration": 1},  # in clock cycles (4ns)
            "operations": {
                "const": "const_dc_flux_pulse",
                "custom": "custom_flux_pulse",
            },
        },



        "dc_flux_line2": {
            "singleInput": {
                "port": ("con1", 7),
            },
            "hold_offset": {"duration": 1},  # in clock cycles (4ns)
            "operations": {
                "const": "const_dc_flux_pulse",
                "custom": "custom_flux_pulse",
            },
        },
    },


    "pulses": {
        "const_flux_pulse": {
            "operation": "control",
            "length": const_flux_len,
            "waveforms": {
                "single": "const_flux_wf",
            },
        },
        "square_pi_pulse": {
            "operation": "control",
            "length": square_pi_len,
            "waveforms": {
                "I": "square_pi_wf",
                "Q": "zero_wf",
            },
        },
        "square_pi_half_pulse": {
            "operation": "control",
            "length": square_pi_len,
            "waveforms": {
                "I": "square_pi_half_wf",
                "Q": "zero_wf",
            },
        },
        "saturation_pulse": {
            "operation": "control",
            "length": saturation_len,
            "waveforms": {"I": "saturation_drive_wf", "Q": "zero_wf"},
        },
        "x90_pulse": {
            "operation": "control",
            "length": x90_len,
            "waveforms": {
                "I": "x90_I_wf",
                "Q": "x90_Q_wf",
            },
        },
        "x180_pulse": {
            "operation": "control",
            "length": x180_len,
            "waveforms": {
                "I": "x180_I_wf",
                "Q": "x180_Q_wf",
            },
        },
        "-x90_pulse": {
            "operation": "control",
            "length": minus_x90_len,
            "waveforms": {
                "I": "minus_x90_I_wf",
                "Q": "minus_x90_Q_wf",
            },
        },
        "y90_pulse": {
            "operation": "control",
            "length": y90_len,
            "waveforms": {
                "I": "y90_I_wf",
                "Q": "y90_Q_wf",
            },
        },
        "y180_pulse": {
            "operation": "control",
            "length": y180_len,
            "waveforms": {
                "I": "y180_I_wf",
                "Q": "y180_Q_wf",
            },
        },
        "-y90_pulse": {
            "operation": "control",
            "length": minus_y90_len,
            "waveforms": {
                "I": "minus_y90_I_wf",
                "Q": "minus_y90_Q_wf",
            },
        },
        "const_dc_flux_pulse": {
            "operation": "control",
            "length": const_flux_len,
            "waveforms": {
                "single": "const_dc_flux_wf",
            },
        },
        "custom_flux_pulse": {
            "operation": "control",
            "length": ramp_flux_len,
            "waveforms": {
                "single": "custom_flux_wf",
            },
        },
        "const_pulse": {
            "operation": "measurement",
            "length": const_len,
            "waveforms": {
                "I": "const_wf",
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

            },


        "qd_pulse": {
            "operation": "control",
            "length": qd_len,
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
                "rotated_cos": "rotated_cosine_weights",
                "rotated_sin": "rotated_sine_weights",
                "rotated_minus_sin": "rotated_minus_sine_weights",
            },
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "const_wf": {"type": "constant", "sample": const_amp},
        "const_flux_wf": {"type": "constant", "sample": const_flux_amp},
        "const_dc_flux_wf": {"type": "constant", "sample": dc_flux_reset},
        "custom_flux_wf": {"type": "arbitrary", "samples": custom_wf},
        "saturation_drive_wf": {"type": "constant", "sample": saturation_amp},
        "square_pi_wf": {"type": "constant", "sample": square_pi_amp},
        "square_pi_half_wf": {"type": "constant", "sample": square_pi_amp / 2},
        "zero_wf": {"type": "constant", "sample": 0.0},
        "x90_I_wf": {"type": "arbitrary", "samples": x90_I_wf.tolist()},
        "x90_Q_wf": {"type": "arbitrary", "samples": x90_Q_wf.tolist()},
        "x180_I_wf": {"type": "arbitrary", "samples": x180_I_wf.tolist()},
        "x180_Q_wf": {"type": "arbitrary", "samples": x180_Q_wf.tolist()},
        "minus_x90_I_wf": {"type": "arbitrary", "samples": minus_x90_I_wf.tolist()},
        "minus_x90_Q_wf": {"type": "arbitrary", "samples": minus_x90_Q_wf.tolist()},
        "y90_Q_wf": {"type": "arbitrary", "samples": y90_Q_wf.tolist()},
        "y90_I_wf": {"type": "arbitrary", "samples": y90_I_wf.tolist()},
        "y180_Q_wf": {"type": "arbitrary", "samples": y180_Q_wf.tolist()},
        "y180_I_wf": {"type": "arbitrary", "samples": y180_I_wf.tolist()},
        "minus_y90_Q_wf": {"type": "arbitrary", "samples": minus_y90_Q_wf.tolist()},
        "minus_y90_I_wf": {"type": "arbitrary", "samples": minus_y90_I_wf.tolist()},
        "readout_wf": {"type": "constant", "sample": readout_amp},
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
    return config1