# %%
import numpy as np
from itertools import accumulate
from qualang_tools.units import unit
from qualang_tools.config.waveform_tools import drag_gaussian_pulse_waveforms
import matplotlib.pyplot as plt


def generate_gaussian_waveform(
    amplitude: float,
    length: int,
    sigma_ratio: float = 0.2,
    rise_fall: str = "rise",
    subtracted: bool = True,
    sampling_rate: float = 1e9,
) -> np.ndarray:
    """
    Creates Gaussian-based DRAG waveforms that compensate for leakage and AC Stark shift.

    :param amplitude: The amplitude in volts.
    :param length: The pulse length in ns.
    :param sigma: The Gaussian standard deviation in ns.
    :param subtracted: Whether to subtract the final value of the waveform.
    :param sampling_rate: The sampling rate in samples/s. Default is 1G samples/s.
    :param rise_fall_full: Specifies the portion of the Gaussian ('rise', 'fall', or 'full').
    :return: A 1D numpy array representing the Gaussian waveform.
    """
    t = np.arange(length, step=1e9 / sampling_rate)  # Full waveform
    if rise_fall == "rise":
        center = (length - 1e9 / sampling_rate)
    elif rise_fall == "fall":
        center = 0
    else:
        raise ValueError("Invalid value for rise_fall_full. Choose from 'rise', 'fall', or 'full'.")

    gauss_wave = amplitude * np.exp(-((t - center) ** 2) / (2 * (2 * sigma_ratio * length) ** 2))
    if subtracted:
        gauss_wave -= gauss_wave.min()  # Subtract the final value
    gauss_wave /= gauss_wave.max()  # Normalize to the peak value
    gauss_wave *= amplitude

    return gauss_wave


def divide_into_n_parts(m: int, n: int) -> list[int]:
    """
    Divide an integer m into n parts as evenly as possible.

    :param m: Total value to divide.
    :param n: Number of parts.
    :return: A list of cumulative sums of the parts.
    """
    q = m // n  # Base integer value
    r = m % n   # Remainder

    # Create the result list with n - r instances of q and r instances of q + 1
    parts = [q] * (n - r) + [q + 1] * r

    # Return cumulative sums
    return [0] + list(accumulate(parts))


def get_waveform_segments_length_cycle(
    waveform_len_ns: int,
    num_waveform_segments: int,
) -> list[int]:
    """
    Get the lengths of waveform segments in cycles.

    :param waveform_len_ns: Total length of the waveform in ns (multiple of 4).
    :param num_waveform_segments: Number of segments to divide the waveform into.
    :return: A list of cumulative lengths in cycles.
    """
    if waveform_len_ns % 4 != 0 and waveform_len_ns > 16:
        raise ValueError("waveform_len_ns must be a multiple of 4 and longer than or equal to 16")
    
    waveform_len_cycle = waveform_len_ns // 4
    return divide_into_n_parts(waveform_len_cycle, num_waveform_segments)


def generate_waveform_segments(
    wf_array: np.ndarray,
    wf_segments_cycle: int = 5,
) -> tuple[list[np.ndarray], list[np.ndarray]]:
    """
    Generate segments of Gaussian rise/fall waveforms.

    :param amplitude: Amplitude of the Gaussian waveform.
    :param gauss_half_full_len_ns: Length of half of the full Gaussian in ns.
    :param num_segments: Number of segments to divide the waveform into.
    :param sigma_scale: Scaling factor for the standard deviation.
    :return: Tuple of lists containing time arrays and waveform segments.
    """
    ts_segments = []
    wf_segments = []
    num_segments = len(wf_segments_cycle)
    for i in range(num_segments - 1):
        t_cycle_from = wf_segments_cycle[i]
        if i < num_segments - 1:
            t_cycle_to = wf_segments_cycle[i + 1]
        else:
            t_cycle_to = wf_segments_cycle[i + 1] + 1
        
        # print(t_cycle_from, t_cycle_to)
        t_ns_from = 4 * t_cycle_from
        t_ns_to = 4 * t_cycle_to
        
        ts_segments.append(np.arange(t_ns_from, t_ns_to))
        wf_segments.append(wf_array[t_ns_from:t_ns_to])

    return ts_segments, wf_segments


#############
# VARIABLES #
#############
u = unit(coerce_to_integer=True)
qop_ip = "172.16.33.101"  # QOP IP address
qop_port = None  # Write the QOP port if version < QOP220
cluster_name = "Cluster_83"  # Name of the cluster

# Frequencies
cooling_fm_freq = 0 * u.MHz # in units of Hz
cooling_fm_len = 1000  # in ns
cooling_fm_amp = 0.2  # in units of volts

gauss_amp = 0.1
gauss_rise_fall_len_ns = 1000 // 4 * 4 # ensure it's multiple of 4ns 
num_gauss_rise_fall_wf_segments = 6

gauss_wf = generate_gaussian_waveform(
    amplitude=gauss_amp,
    length=gauss_rise_fall_len_ns,
    sigma_ratio=0.2,
    rise_fall="rise", # rise or fall
)
wf_segments_cycle = get_waveform_segments_length_cycle(
    waveform_len_ns=gauss_rise_fall_len_ns,
    num_waveform_segments=num_gauss_rise_fall_wf_segments,
)
gauss_rise_ts_segments, gauss_rise_wf_segments = generate_waveform_segments(
    wf_array=gauss_wf,
    wf_segments_cycle=wf_segments_cycle,
)

config = {
    "version": 1,
    "controllers": {
        "con1": {
            "analog_outputs": {
                1: {"offset": 0.0, "delay": 0.0},
                2: {"offset": 0.0, "delay": 0.0},
                3: {"offset": 0.0, "delay": 0.0}, 
                4: {"offset": 0.0, "delay": 0.0},
            },
            "digital_outputs": {
                1: {}, 
                2: {},
                3: {},
                4: {},
                5: {},
                6: {},
                7: {},
                8: {}, 
                9: {},
                10: {},
            },
            "analog_inputs": {},
        }
    },
    "elements": {
        "cooling_fm": {
            "singleInput": {
                "port": ("con1", 1)
            },
            "intermediate_frequency": cooling_fm_freq,
            "operations": {
                "const": "const_pulse",
                "const_1us": "const_pulse_1us",
                "const_1ms": "const_pulse_1ms",
                "const_1s": "const_pulse_1s",
            },
        },
        "cooling_fm_even_segment": {
            "singleInput": {
                "port": ("con1", 1)
            },
            "intermediate_frequency": cooling_fm_freq,
            "operations": {
                "const": "const_pulse",
                **{
                    f"gauss_rise_{s:02d}": f"gauss_rise_pulse_{s:02d}"
                    for s in range(num_gauss_rise_fall_wf_segments) if s % 2 == 0
                }
            },
        },
        "cooling_fm_odd_segment": {
            "singleInput": {
                "port": ("con1", 1)
            },
            "intermediate_frequency": cooling_fm_freq,
            "operations": {
                "const": "const_pulse",
                **{
                    f"gauss_rise_{s:02d}": f"gauss_rise_pulse_{s:02d}"
                    for s in range(num_gauss_rise_fall_wf_segments) if s % 2 == 1
                }
            },
        },
    },
    "pulses": {
        "const_pulse": {
            "operation": "control",
            "length": cooling_fm_len,
            "waveforms": {"single": "const_wf"},
        },
        "const_pulse_1us": {
            "operation": "control",
            "length": 1 * u.us,
            "waveforms": {"single": "const_wf"},
        },
        "const_pulse_1ms": {
            "operation": "control",
            "length": 1 * u.ms,
            "waveforms": {"single": "const_wf"},
        },
        "const_pulse_1s": {
            "operation": "control",
            "length": 1 * u.s,
            "waveforms": {"single": "const_wf"},
        },
        **{
            f"gauss_rise_pulse_{s:02d}": {
                "operation": "control",
                "length": len(_ts) * u.ns,
                "waveforms": {"single": f"gauss_rise_wf_{s:02d}"},
            }
            for s, _ts in enumerate(gauss_rise_ts_segments)
        }
    },
    "waveforms": {
        "const_wf": {"type": "constant", "sample": cooling_fm_amp},
        "zero_wf": {"type": "constant", "sample": 0.0},
        **{
            f"gauss_rise_wf_{s:02d}": {
                "type": "arbitrary",
                "samples": _wf,
            }
            for s, _wf in enumerate(gauss_rise_wf_segments)
        }
    },
    "digital_waveforms": {
        "ON": {"samples": [(1, 0)]},  # [(on/off, ns)]
    },
}

# %%

