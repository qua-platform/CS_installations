# %%

import numpy as np
import matplotlib.pyplot as plt

path = "arrays.npz"

data = np.load(path)

I = data["I"]
Q = data["Q"]
R = np.sqrt(I ** 2 + Q ** 2)
ts = np.linspace(0, 1e-3, 5000) * 1000

plt.plot(ts, R)
med = 0.0032896620286946175
plt.ylim(0.999 * med, 1.003 * med)
plt.xlabel("time [ms]")
plt.ylabel(r"$R=\sqrt{I^2 + Q^2}$ [V]")

plt.show()


# %%
