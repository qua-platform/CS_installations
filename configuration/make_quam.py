from dataclasses import field
from typing import Dict

import numpy as np
from qualang_tools.units import unit
from scipy import cluster

from quam.components import (
    BasicQuAM,
    Channel,
    InOutIQChannel,
    IQChannel,
    Octave,
    OctaveDownConverter,
    OctaveUpConverter,
    pulses,
)

# Config variables

qop_ip = "172.16.33.101"
cluster_name = "Cluster_81"

u = unit(coerce_to_integer=True)

octave = Octave(
    name="oct1",
    ip="172.16.33.101",
    port=11232,
)

qpu = BasicQuAM(octaves={"oct1": octave})

# Add Octave to the qpu


octave.initialize_frequency_converters()

# Resonator channel

qpu.channels["resonator"] = InOutIQChannel(
    opx_output_I=("con1", 1),
    opx_output_Q=("con1", 2),
    opx_input_I=("con1", 1),
    opx_input_Q=("con1", 2),
    frequency_converter_up=octave.RF_outputs[1].get_reference(),
    frequency_converter_down=octave.RF_inputs[1].get_reference(),
    intermediate_frequency=100e6,
)
octave.RF_outputs[1].channel = qpu.channels["resonator"].get_reference()
octave.RF_inputs[1].channel = qpu.channels["resonator"].get_reference()
octave.RF_outputs[1].LO_frequency = 6 * u.GHz
octave.RF_inputs[1].LO_frequency = 6 * u.GHz

depletion_time = 10 * u.us

# Add Qubit xy drive channel

qpu.channels["qubit_xy"] = IQChannel(
    opx_output_I=("con1", 3),
    opx_output_Q=("con1", 4),
    frequency_converter_up=octave.RF_outputs[2].get_reference(),
    intermediate_frequency=50e6,
)
octave.RF_outputs[2].channel = qpu.channels["qubit_xy"].get_reference()
octave.RF_outputs[2].LO_frequency = 4 * u.GHz


# Add readout pulse

readout_pulse = pulses.SquareReadoutPulse(length=1000, amplitude=0.1)

qpu.channels["resonator"].operations["readout"] = readout_pulse

# Add x180 pulse

pi_pulse = pulses.GaussianPulse(length=20, amplitude=0.1, sigma=8)

qpu.channels["qubit_xy"].operations["x180"] = pi_pulse

# Add square pulse

square = pulses.SquarePulse(length=20, amplitude=0.1)

qpu.channels["qubit_xy"].operations["square"] = square

# Add saturation pulse

saturation_pulse = pulses.SquarePulse(length=5_000, amplitude=0.01)

qpu.channels["qubit_xy"].operations["saturation"] = saturation_pulse


config = qpu.generate_config()
