"""Run a 2D stability diagram experiment using the QDACs for the control
   but the OPX for readout.

   As seen in QM webpage:
    - Fig 4-5, https://www.quantum-machines.co/solutions/quantum-dots/

Pseudo-code:

    define for each axis: the number of points, the gates to sweep from start to end values
    e.g. dim_0_pts = 100, dim_0_sweeps = {"gate_1": {'start' = -1V, 'end' = 1V}}
         dim_1_pts = 200, dim_1_sweeps = {"gate_2": {'start' = 0V, 'end' = .1V}}
    
    for j in dim_1: <- 'slow' axis = can be executed on PC
        for i in dim_0: <- 'fast' axis = must be executed on QDACs
            apply the voltages(i, j) <- QDACs only
            measure <- OPX only, must be stored on the OPX
        get the data from OPX to PC

Typical dim sizes: (dim_0=1000, dim_1=500)
Typical number of electrodes swept at the same time: 1 or 2

!!! IMPORTANT !!!
Typical sampling rate: 1-100kHz -> does the OPX works for 'slow' 1kHz readout ??

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
DC_position: dict[str, Quantity] = {
    electrode: Q_("0V") for electrode in probe_to_electrode.values()
}
DC_position = {"gate_1": Q_("100mV"), "gate_17": Q_("1.2V")}

# -- Define the two axes of the simple stability diagram
# dim_0 = QDACs
dim_0_pts = 100
dim_0_sweeps: dict[str, Quantity] = {
    "gate_1": np.linspace(Q_("-1V"), Q_("1V"), dim_0_pts),
    "gate_2": np.linspace(Q_("-0.1V"), Q_("0.1V"), dim_0_pts),
}

# dim_1 = QDACs
dim_1_pts = 200
dim_1_sweeps: dict[str, Quantity] = {
    "gate_3": np.linspace(Q_("-0.2V"), Q_("0.V"), dim_0_pts),
    "gate_4": np.linspace(Q_("-0.3V"), Q_("0.3V"), dim_0_pts),
}

# -- Run the experiment

# 1 - apply DC position
# ???

# 2 - program the 2D stability diagram
# ???

# 3 - run the experiment
# ???

# 4 - get the data
# ???
