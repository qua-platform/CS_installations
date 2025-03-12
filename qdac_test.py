# %%

from qdac2_driver import *

# %%

qdac = QDACII(communication_type="Ethernet", IP_address="192.168.8.76")

# %%

set_dc_voltage(qdac, channel=1, voltage=0.69, output_range="low", output_filter="dc", slew_rate=2e7)
qdac.query("sour1:dc:volt?")

# %%
