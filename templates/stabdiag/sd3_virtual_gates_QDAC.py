"""Run a 2D stability diagram experiment with virtual gates using one or multiple QDACs.

Pseudo-code:
    define transformation matrix to get virtual gates from the real gates

    define for each axis: the number of points, the gates to sweep from start to end values
    e.g. dim_0_pts = 100, dim_0_sweeps = {"eps": {'start' = -1V, 'end' = 1V}}
         dim_1_pts = 200, dim_1_sweeps = {"gate_2": {'start' = 0V, 'end' = .1V}}

    compute the actual voltages to apply to the QDACs from the virtual gates

    for j in dim_1: <- 'slow' axis = can be executed on PC
        for i in dim_0: <- 'fast' axis = must be executed on QDACs
            apply the voltages(i, j)
            measure <- must be stored on QDACs
        get the data from QDACs to PC

To test:
    - T1: Run the script to compensate a SET cross-capacitive coupling.

Typical dim sizes: (dim_0=1000, dim_1=500)
Typical number of electrodes swept at the same time: >1 (up to 8)
Typical sampling rate: 1kHz

"""

import numpy as np
from pint import Quantity, get_application_registry

from ..config import get_probe_from_electrode, probe_to_electrode, probe_to_QDAC

# Define the unit registry
ureg = get_application_registry()
Q_ = ureg.Quantity


# --------------------------------------------------------------------------
# VIRUTAL GATES STABILITY DIAGRAM
# ---------------------------------------------------------------------------

# -- Virtual gate definition
# Define the virtual gates from the real gates

# transformation matrix (not necessarily square)
# (delta) = (1     1) (gate_1)
# (eps  )   (1    -1) (gate_2)

# gives the virtual gates :
# delta = gate_1 + gate_2
# eps = gate_1 - gate_2

t_matrix = ((1, 1), (1, -1))

# -- DC position
# Define the default voltage to apply to each probe, should be 0V by default.
# A collection giving for each electrode, the voltage to apply.
# TODO: here, we apply a voltage to the electrodes of the current device measured
# (e.g. the 12 first probes), but we should apply a 0V voltage to all the 50 probes.
DC_position: dict[str, Quantity] = {
    electrode: Q_("0V") for electrode in probe_to_electrode.values()
}
DC_position = {"gate_1": Q_("100mV"), "gate_17": Q_("1.2V")}

# -- Define the two axes of the stability diagram using the virtual gates
dim_0_pts = 100
dim_0_sweeps: dict[str, Quantity] = {
    "eps": np.linspace(Q_("-1V"), Q_("1V"), dim_0_pts),
}

dim_1_pts = 200
dim_1_sweeps: dict[str, Quantity] = {
    "delta": np.linspace(Q_("-0.2V"), Q_("0.V"), dim_0_pts),
}

# -- Run the experiment

# 1 - apply DC position
# ???

# 2 - program the stability diagram using the virtual gates
# ???

# How do we program the QDACs to sweep the virtual gates?
# either use QM smart tools (?) or simply translate the two virtual gate sweeps as a
# 2D map of the real gates.

# 3 - run the experiment
# ???

# 4 - get the data
# ??? with both virtual and physical axes
