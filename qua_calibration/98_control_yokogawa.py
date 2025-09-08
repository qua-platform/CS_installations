#%%
import time
from qcodes.instrument_drivers.yokogawa import YokogawaGS200

#%%
gs = YokogawaGS200(
    "gs200", address="USB::0xB21::0x39::91RB18719::INSTR", terminator="\n"
)
#%%
# gs.output('off')
gs.source_mode('CURR')
gs.voltage_limit(5)     
gs.auto_range(True)

gs.output('on')
gs.ramp_current(0.0002, 0.00001, 1)  

#%%
gs.current()