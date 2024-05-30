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
ts = np.arange(0, 20e3, 250)
coeffs_ground = [0.2 * v for v in [d0, mx0, my0]] # [0.04, 0.07, 0.09]
coeffs_excited = [0.2 * v for v in [d1, mx1, my1]] # [0.03, 0.08, 0.06]

# generate traces for <X>, <Y>, <Z> for control state = 0 and 1
np.random.seed(0)
crht_comp = CRHamiltonianTomographyFunctions()
pms0 = crht_comp.compute_XYZ(ts, *coeffs_ground, noise=0.2)
pms1 = crht_comp.compute_XYZ(ts, *coeffs_excited, noise=0.2)

# set the data and perform the analysis for hamiltonian tomography
crht = CRHamiltonianTomographyAnalysis(
    ts=ts,
    crqst_data=np.concatenate(
        [
            np.concatenate([pms0["x"][:, None], pms0["y"][:, None], pms0["z"][:, None]], axis=1)[..., None],
            np.concatenate([pms1["x"][:, None], pms1["y"][:, None], pms1["z"][:, None]], axis=1)[..., None],
        ], axis=2)
)
crht.fit_params(random_state=5)
coefs = {k: 1e6*v for k, v in crht.get_interaction_rates().items()}
fig = crht.plot_fit_result()
                                                                                                                     # %%
# %%
