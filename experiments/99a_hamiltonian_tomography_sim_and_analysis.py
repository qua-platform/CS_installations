# %%

import numpy as np
import matplotlib.pyplot as plt
from hamiltonian_tomography import (
    CRHamiltonianTomography,
    CRHamiltonianTomographyFunctions,
)

# for simulation
ts = np.arange(0, 2e2, 4)
coeffs_ground = [0.04, 0.07, 0.09]
coeffs_excited = [0.03, 0.08, 0.06]

# generate traces for <X>, <Y>, <Z> for control state = 0 and 1
np.random.seed(0)
crht_comp = CRHamiltonianTomographyFunctions()
pms0 = crht_comp.compute_XYZ(ts, *coeffs_ground, noise=0.15)
pms1 = crht_comp.compute_XYZ(ts, *coeffs_excited, noise=0.15)

# set the data and perform the analysis for hamiltonian tomography
crht = CRHamiltonianTomography(
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
