#%%
import time
from qcodes.instrument_drivers.yokogawa import YokogawaGS200

#%%
gs = YokogawaGS200(
    "gs200", address='USB0::0x0B21::0x0039::901B35283::0::INSTR', terminator="\n"
)
#%%
# gs.output('off')
# gs.source_mode('CURR')
gs.voltage_limit(10)     
gs.auto_range(True)
#%%
# gs.output('on')
gs.ramp_current(0e-3, 1e-5, 0.01)  

#%%
# gs.current()
# gs.output('off')
# %%
