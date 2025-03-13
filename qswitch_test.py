# %%

from qswitch_driver import *

# %%

qs = QSwitch(UDPConfig("192.168.8.16"))

# %%
qs.overview()
# %%
qs.close_relay(20, 9)
# %%
qs.open_relay(20, 0)
# %%
qs.ground_and_release(["20"])
# %%
qs.connect_and_unground(["20"])
# %%
qs.close_relay(20, 5)
# %%
qs.ground_and_release_all()
# %%
