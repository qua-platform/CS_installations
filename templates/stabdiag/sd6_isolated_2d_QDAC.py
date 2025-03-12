""" Run a 3D stability diagram experiment with a sequence loading N electrons.
    The loading sequence is performed before each sweep of the 1st dim = 'fast' axis.
    The number of electrons loaded is stepped on the 3rd dimension.
    The loading sequence is executed on a QDAC.

Pseudo-code:

    define for the 2 first axis: the number of points, the gates to sweep from start to end values
    e.g. dim_0_pts = 100, dim_0_sweeps = {"gate_1": {'start' = -1V, 'end' = 1V}}
         dim_1_pts = 200, dim_1_sweeps = {"gate_2": {'start' = 0V, 'end' = .1V}}

    define the loading sequences used to load different electron numbers N.
    loading_points = [val_1, val_2, val_3, ...] for N=0, 1, 2, ... (= dim_2)
    loading_sequence = [go_to_emptying_point, wait_time, go_to_loading_point(k),
                        wait_time, go_to_isolated_point]

    for k in dim_2: <- change the number of electrons loaded
        for j in dim_1: <- 'slow' axis = can be executed on PC
            run loading_sequence(k) <- must be executed on QDACs right before the fast axis
            for i in dim_0: <- 'fast' axis = must be executed on QDACs
                apply the voltages(i, j)
                measure <- must be stored on QDACs
            get the data from QDACs to PC

To test:
    - T1: Run the script.

Typical dim sizes: (dim_0=1000, dim_1=500, dim_2=10)
Typical number of electrodes swept at the same time: 1 or 2
Typical AWG sequence: a few setpoints and wait times (as long as a few ms)
Typical sampling rate: 1kHz

"""
from qualang_tools import voltage_gates
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

# -- Define the two axes of the stability diagram
dim_0_pts = 100
dim_0_sweeps: dict[str, Quantity] = {
    "gate_1": np.linspace(Q_("-1V"), Q_("1V"), dim_0_pts),
    "gate_2": np.linspace(Q_("-0.1V"), Q_("0.1V"), dim_0_pts),
}

dim_1_pts = 200
dim_1_sweeps: dict[str, Quantity] = {
    "gate_3": np.linspace(Q_("-0.2V"), Q_("0.V"), dim_0_pts),
    "gate_4": np.linspace(Q_("-0.3V"), Q_("0.3V"), dim_0_pts),
}

dim_2_loading_setpoints = [
    {"gate_5": Q_("0.1V")},  # N = 0 electrons
    {"gate_5": Q_("0.12V")},  # N = 1 electron
    {"gate_5": Q_("0.15V")},  # N = 2 electrons
    {"gate_5": Q_("0.2V")},  # N = 3 electrons
]

# -- Pre-sequence
# Each time that the dim_1 (not dim_0, nor dim_2) is stepped, run a specific pre-sequence

# pre_sequence = [go_to_emptying_point, wait_time, go_to_loading_point(i), wait_time, go_to_isolated_point
# for each step i in dim_2, we change the value of the loading_point.
# a setpoint = define the voltages to apply to X electrodes (X = typ. 1 but can be many)

# -- Run the experiment

# 1 - apply DC position
# ???

# 2 - program the 2D stability diagram
# ???

# 3 - run the experiment
# ???

# 4 - get the data
# ???
