# %%
import numpy as np
import matplotlib.pyplot as plt


ramp_rate = 3e-4
ramp_duration = 1000 # ramp_rate * ramp_duration will be the voltage applied
ramp_amp = ramp_rate * ramp_duration
flat_duration = 4000


linear_ramp_up = np.linspace(0, ramp_amp, ramp_duration + 1)
linear_flat = ramp_amp * np.ones(flat_duration)
linear_ramp_down = linear_ramp_up[::-1]
linear_ramp_wf = np.concatenate([linear_ramp_up, linear_flat, linear_ramp_down])
# %%
