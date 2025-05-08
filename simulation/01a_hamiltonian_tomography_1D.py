# %%
import numpy as np
import matplotlib.pyplot as plt
from simulation.helper_cr_simulation import *
from quam_libs.cr_hamiltonian_tomography import (
    CRHamiltonianTomographyAnalysis,
    plot_crqst_result_2D,
    plot_crqst_result_3D,
    PAULI_2Q,
)


# -----------------------
# Parameters (GHz → rad/ns)
# -----------------------
ts = np.arange(0, 30, 0.25)

r = 0.4
s = -0.03
A_c = 1.28 * two_pi * r        # CR drive amplitude (rad/ns)
A_t = 0.3 * two_pi * r        # Cancel drive amplitude (rad/ns)
phi_c = (0.368 - s) * two_pi         # CR drive phase (rad)
phi_t = (0.668 - s) * two_pi        # Cancel drive phase (rad)



# -----------------------
# Derived Parameters
# -----------------------
hcr = CRHamiltonian(A_c, A_t, phi_c, phi_t)
hcr.print_params()

# For Qc = |g>
cr_rabi_g = CRRabiOscillations(hcr, qc_g=True)
X0, Y0, Z0 = cr_rabi_g.compute_components(ts)

# For Qc = |e>
cr_rabi_e = CRRabiOscillations(hcr, qc_g=False)
X1, Y1, Z1 = cr_rabi_e.compute_components(ts)


# -----------------------
# Plotting
# -----------------------

fig = plot_raw_data(ts, X0, Y0, Z0, X1, Y1, Z1)
plt.show()


# -----------------------
# Fitting
# -----------------------
data = np.stack(
    [
        np.stack([X0, X1], axis=-1),
        np.stack([Y0, Y1], axis=-1),
        np.stack([Z0, Z1], axis=-1),
    ],
    axis=1
) # target data: len(ts) x 3 x 2
# data += np.random.normal(size=data.shape, loc=0, scale=0.03)

crht = CRHamiltonianTomographyAnalysis(ts=ts, data=data)

try:
    crht.fit_params()
    fig_analysis = crht.plot_fit_result(do_show=True)
except:
    pass

fig_3d = plot_crqst_result_3D(ts, data)

plt.show()



# %%
