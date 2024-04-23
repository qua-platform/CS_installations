# %%

import numpy as np
import matplotlib.pyplot as plt
from cr_hamiltonian_tomography import (
    CRHamiltonianTomographyAnalysis,
    CRHamiltonianTomographyFunctions,
)


IX = +0.889 * 1e-3 
IY = -1.530 * 1e-3
IZ = -0.147 * 1e-3
ZX = -2.627 * 1e-3
ZY = +4.616 * 1e-3
ZZ = +0.422 * 1e-3

mx0 = IX + ZX
mx1 = IX - ZX
my0 = IY + ZY
my1 = IY - ZY
d0 = IZ + ZZ
d1 = IZ - ZZ

# p00 = [0.0002, 0.0002, 0.0005]
# p01 = [0.0002, 0.001, 0.001]

# for simulation
ts = np.arange(0, 8.5e3, 50)
coeffs_ground = [0.2 * v for v in [d0, mx0, my0]] # [0.04, 0.07, 0.09]
coeffs_excited = [0.2 * v for v in [d1, mx1, my1]] # [0.03, 0.08, 0.06]

# generate traces for <X>, <Y>, <Z> for control state = 0 and 1
np.random.seed(0)
crht_comp = CRHamiltonianTomographyFunctions()
pms0 = crht_comp.compute_XYZ(ts, *coeffs_ground, noise=0.05)
pms1 = crht_comp.compute_XYZ(ts, *coeffs_excited, noise=0.05)

# set the data and perform the analysis for hamiltonian tomography
crht = CRHamiltonianTomographyAnalysis(
    ts=ts,
    xyz={
        "0": {
            "x": pms0["x"],
            "y": pms0["y"],
            "z": pms0["z"],
        },
        "1": {
            "x": pms1["x"],
            "y": pms1["y"],
            "z": pms1["z"],
        },
    },
)
crht.fit_params(random_state=5)
coefs = {k: 1e6*v for k, v in crht.get_interaction_rates().items()}
fig = crht.plot_fit_result()
                                                                                                                     # %%
# %%
