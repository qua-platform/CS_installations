"""Extract charge noise with averages or different DC polarization

Basically: go to a specific DC polarization, take a timetrace with a specific duration,
and sampling rate; repeat for averages or different DC polarizations.

To test:
    - T1: Run the script with a 5s acquisition duration @1kHz.
    - T2: Probe the acquisition duration limit.

Typical dim sizes: (dim_0=5000, dim_1=10) = 5s @1kHz with 10 averages
Typical sampling rate: 1kHz

"""

import numpy as np
from pint import Quantity, get_application_registry

from ..config import get_probe_from_electrode, probe_to_electrode, probe_to_QDAC

# Define the unit registry
ureg = get_application_registry()
Q_ = ureg.Quantity


# --------------------------------------------------------------------------
# 2D STABILITY DIAGRAM
# ---------------------------------------------------------------------------

# -- DC position
# Define the default voltage to apply to each probe, should be 0V by default.
# A collection giving for each electrode, the voltage to apply.
# TODO: here, we apply a voltage to the electrodes of the current device measured
# (e.g. the 12 first probes), but we should apply a 0V voltage to all the 50 probes.
DC_position: dict[str, Quantity] = {electrode: Q_("0V") for electrode in probe_to_electrode.values()}
DC_position = {"gate_1": Q_("100mV"), "gate_17": Q_("1.2V")}

# -- Pre-sequence
# A pre-sequence can be applied before starting the acquisition.
# pre_sequence = [go_there, wait_time, ...]

# -- Run the experiment

# 1 - apply DC position
# ???

# 2 - program the 2D stability diagram
acq_rate = Q_("1kHz")
acq_duration = Q_("5s")
n_averages = 10

# 3 - run the experiment

# go to DC position, run pre-sequence, take timetrace, repeat for averages
# or different DC polarizations/pre-sequences

# 4 - get the data
# ???
