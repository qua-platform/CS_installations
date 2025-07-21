# %%
from qdac2_driver import QDACII, load_voltage_list, set_qdac_voltage

import numpy as np

##########################################################################################
## QDAC2 section
# Create the qdac instrument
# qdac = QDACII("Ethernet", IP_address="224.0.0.22", port=5025)  # Using Ethernet protocol
qdac = QDACII("USB", USB_device=8)  # Using USB protocol

###########################
# Voltage scan triggering #
###########################
# Voltages in Volt
n_points_fast = 10
voltage_values_fast = np.linspace(-1.5, 1.5, n_points_fast)
load_voltage_list(
    qdac,
    channel=1,
    dwell=2e-6,
    slew_rate=2e7,
    trigger_port="ext1",
    output_range="low",
    output_filter="med",
    voltage_list=voltage_values_fast,
)

###############
# Set voltage #
###############
set_qdac_voltage(qdac, channel=2, voltage=1)

## QDAC2 section
##########################################################################################
