
import json
from qualang_tools.units import unit
from quam_config import Quam
from quam_builder.builder.superconducting.pulses import add_DragCosine_pulses
from quam.components.pulses import GaussianPulse, SquarePulse  # (+SquarePulse)
import numpy as np
import json
from pprint import pprint
import matplotlib.pyplot as plt
from qualang_tools.wirer.wirer.channel_specs import *

########################################################################################################################
# %%                                 QUAM loading and auxiliary functions
########################################################################################################################
# Loads the QUAM
machine = Quam.load()
# machine.save()
# Class containing tools to help handling units and conversions.
u = unit(coerce_to_integer=True)


def get_octave_gain_and_amplitude(desired_power: float, max_amplitude: float = 0.125) -> tuple[float, float]:
    """Get the Octave gain and IF amplitude for the Octave to output the specified desired power.

    Args:
        desired_power (float): Desired output power in dBm.
        max_amplitude (float, optional): Maximum allowed IF amplitude provided by the OPX to the Octave in V. Default is 0.125V, which is the optimum for driving the Octave up-conversion mixers.

    Returns:
        tuple[float, float]: The Octave gain and IF amplitude realizing the desired power.
    """

    resulting_power = desired_power - u.volts2dBm(max_amplitude)
    if resulting_power < 0:
        octave_gain = round(max(desired_power - u.volts2dBm(max_amplitude) + 0.5, -20) * 2) / 2
    else:
        octave_gain = round(min(desired_power - u.volts2dBm(max_amplitude) + 0.5, 20) * 2) / 2
    amplitude = u.dBm2volts(desired_power - octave_gain)

    if -20 <= octave_gain <= 20 and -0.5 <= amplitude < 0.5:
        return octave_gain, amplitude
    else:
        raise ValueError(
            f"The desired power is outside the specifications ([-20; +20]dBm, [-0.5; +0.5)V), got ({octave_gain}; {amplitude})"
        )


########################################################################################################################
# %%                                    Resonator parameters
########################################################################################################################
# Be mindful that the Octave LO synthesizers are shared between ports:
#    synth1: RF1 and RFin1
#    synth2: RF2 and RF3
#    synth3: RF4 and RF5
# Octave LO frequency [2 : 0.250 : 18] GHz
# Octave gain [-20 : 0.5 : 20] dB
# Please refer to https://docs.quantum-machines.co/latest/docs/Guides/octave/ for more details

# Match "from-scratch" settings: LO = 4.0 GHz, IFs = [3, 4, 5] MHz, gain = -12 dB, readout pulse = 1 us @ 0.2
rr_LO = 4.0 * u.GHz
rr_if = np.array([3.0, 4.0, 5.0]) * u.MHz
rr_freq = rr_LO + rr_if  # RF readout frequencies
assert np.all(np.abs(rr_if) < 400 * u.MHz), "The resonator intermediate frequency must be within [-400; 400] MHz."

rr_gain = -12.0  # dB
rr_amplitude = 0.2  # readout pulse amplitude (dimensionless)

# Update qubit rr freq and power
for k, qubit in enumerate(machine.qubits.values()):
    qubit.resonator.f_01 = rr_freq.tolist()[k]  # Resonator (readout) RF frequency
    qubit.resonator.RF_frequency = qubit.resonator.f_01
    qubit.resonator.frequency_converter_up.LO_frequency = rr_LO
    qubit.resonator.frequency_converter_up.gain = rr_gain
    qubit.resonator.frequency_converter_up.output_mode = "triggered"

########################################################################################################################
# %%                                    Qubit parameters
########################################################################################################################
# Be mindful that the Octave LO synthesizers are shared between ports:
#    synth1: RF1 and RFin1
#    synth2: RF2 and RF3
#    synth3: RF4 and RF5
# Octave LO frequency [2 : 0.250 : 18] GHz
# Octave gain [-20 : 0.5 : 20] dB
# Please refer to https://docs.quantum-machines.co/latest/docs/Guides/octave/ for more details

# Match "from-scratch" settings: LOs = [3.5, 4.5, 5.5] GHz, IFs = [2, 4, 6] MHz, gain = -12 dB
xy_LO = np.array([3.5, 4.5, 5.5]) * u.GHz
xy_if = np.array([2.0, 4.0, 6.0]) * u.MHz
xy_freq = xy_LO + xy_if
assert np.all(np.abs(xy_if) < 400 * u.MHz), "The xy intermediate frequency must be within [-400; 400] MHz."

# Transmon anharmonicity (uniform 200 MHz as in the from-scratch helper)
anharmonicity = np.array([200, 200, 200]) * u.MHz

xy_gain = -12.0  # dB

# Update qubit xy freq and power
for k, qubit in enumerate(machine.qubits.values()):
    qubit.f_01 = xy_freq.tolist()[k]  # Qubit |g>->|e> transition frequency (drive RF)
    qubit.xy.RF_frequency = qubit.f_01
    qubit.xy.frequency_converter_up.LO_frequency = xy_LO.tolist()[k]
    qubit.xy.frequency_converter_up.gain = xy_gain
    qubit.xy.frequency_converter_up.output_mode = "triggered"
    qubit.grid_location = f"{k},0"  # Qubit grid location for plotting as "column,row"

########################################################################################################################
# %%                                        Pulse parameters
########################################################################################################################
# How to add new pulses
from quam.components.pulses import (
    SquarePulse,
    DragGaussianPulse,
    DragCosinePulse,
    FlatTopGaussianPulse,
    WaveformPulse,
    SquareReadoutPulse,
)
# e.g., machine.qubits[q].xy.operations["new_pulse"] = FlatTopGaussianPulse(...)

# "From-scratch" pulse set:
# readout: 1 us, 0.2
# saturation: 10 us, 0.5
# XY helper pulses: const (1000 ns, 0.4), gauss (1000 ns, sigma 400, amp 0.4)
# square_pi (1000 ns, 0.4), square_pi_half (1000 ns, 0.2)
# DRAG: x180_len=600 ns, x180_amp=0.35, anharmonicity=200 MHz, alpha=0, detuning=0
x180_len = 600
x180_amp = 0.35

for k, q in enumerate(machine.qubits):
    # readout
    machine.qubits[q].resonator.operations["readout"] = SquareReadoutPulse(length=1*u.us, amplitude=rr_amplitude)

    # Qubit saturation
    machine.qubits[q].xy.operations["saturation"].length = 10 * u.us
    machine.qubits[q].xy.operations["saturation"].amplitude = 0.5

    # XY helper pulses
    machine.qubits[q].xy.operations["const"] = SquarePulse(length=1000, amplitude=0.4)
    machine.qubits[q].xy.operations["gauss"] = GaussianPulse(length=1000, amplitude=0.4, sigma=400)
    machine.qubits[q].xy.operations["square_pi"] = SquarePulse(length=1000, amplitude=0.4)
    machine.qubits[q].xy.operations["square_pi_half"] = SquarePulse(length=1000, amplitude=0.2)

    # Single qubit gates - DragCosine (DRAG family: x/y 90/180 & negatives)
    add_DragCosine_pulses(
        machine.qubits[q],
        amplitude=x180_amp,
        length=x180_len,
        anharmonicity=anharmonicity.tolist()[k],
        alpha=0.0,
        detuning=0,
    )

    # Flux pulse and (optional) mapping (TLS1 -> AO10, TLS2/3 -> AO9) if z exists
    if hasattr(machine.qubits[q], "z") and machine.qubits[q].z != None:
        print(machine.qubits[q].z)
        machine.qubits[q].z.operations["const"] = SquarePulse(length=200, amplitude=0.45)
        # If your QUAM exposes controller/port attributes, set them (ignore if not present)
        try:
            if hasattr(machine.qubits[q].z, "controller"):
                machine.qubits[q].z.controller = "con1"
            if hasattr(machine.qubits[q].z, "port"):
                machine.qubits[q].z.port = 10 if k == 0 else 9
        except Exception:
            pass

########################################################################################################################
# %%                                         Save the updated QUAM
########################################################################################################################
# save into state.json
machine.save()
# Visualize the QUA config and save it


def find_non_jsonables(obj, path="root", out=None):
    if out is None:
        out = []
    # If the whole subtree is fine, stop here
    try:
        json.dumps(obj)
        return out
    except TypeError:
        pass

    if isinstance(obj, dict):
        for k, v in obj.items():
            find_non_jsonables(v, f"{path}.{k}", out)
    elif isinstance(obj, (list, tuple)):
        for i, v in enumerate(obj):
            find_non_jsonables(v, f"{path}[{i}]", out)
    elif isinstance(obj, np.ndarray):
        out.append((path, f"np.ndarray shape={obj.shape}, dtype={obj.dtype}"))
    elif isinstance(obj, (np.floating, np.integer, np.bool_)):
        out.append((path, f"{type(obj).__name__} value={obj!r}"))
    else:
        out.append((path, f"type={type(obj).__name__} value={repr(obj)[:120]}"))
    return out

cfg = machine.generate_config()
bad = find_non_jsonables(cfg)

if bad:
    print("Found non-JSON-serializable values:")
    for p, info in bad:
        print(f" - {p}: {info}")
else:
    print("Config looks JSON-serializable.")

pprint(machine.generate_config())
with open("qua_config.json", "w+") as f:
    json.dump(machine.generate_config(), f, indent=4)

# %%
