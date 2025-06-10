# %%
import numpy as np
import matplotlib.pyplot as plt
from helper_cr_simulation import *
from cr_hamiltonian_tomography import (
    CRHamiltonianTomographyAnalysis,
    plot_cr_duration_vs_scan_param,
    plot_interaction_coeffs,
    plot_crqst_result_2D,
    plot_crqst_result_3D,
    PAULI_2Q,
)


# -----------------------
# Parameters (GHz → rad/ns)
# -----------------------
ts = np.arange(0, 40, 1)

r = 0.8
A_c = 1.28 * two_pi * r      # CR drive amplitude (rad/ns)
A_t = 0.3 * two_pi * r       # Cancel drive amplitude (rad/ns)
phi_c = 0.365 * two_pi         # CR drive phase (rad)
phi_t = 0.669 * two_pi         # Cancel drive phase (rad)

amp_scalings = np.arange(0.0, 2.0, 0.05)


# -----------------------
# Derived Parameters
# -----------------------
control_data = np.ones((len(amp_scalings), len(ts), 3, 2))
control_data[..., 1] = -1
target_data = np.zeros((len(amp_scalings), len(ts), 3, 2))


for idx, amp in enumerate(amp_scalings):
    hcr = CRHamiltonian(amp * A_c, A_t, phi_c, phi_t)
    hcr.print_params()

    # For Qc = |g>
    cr_rabi_g = CRRabiOscillations(hcr, qc_g=True)
    X0, Y0, Z0 = cr_rabi_g.compute_components(ts)

    # For Qc = |e>
    cr_rabi_e = CRRabiOscillations(hcr, qc_g=False)
    X1, Y1, Z1 = cr_rabi_e.compute_components(ts)

    # Plot
    fig = plot_raw_data(ts, X0, Y0, Z0, X1, Y1, Z1)
    plt.suptitle(f"amp = {amp:5.4f}")
    plt.tight_layout()
    plt.show()

    # Organize data in np.array
    data_t = np.stack(
        [
            np.stack([X0, X1], axis=-1),
            np.stack([Y0, Y1], axis=-1),
            np.stack([Z0, Z1], axis=-1),
        ],
        axis=1
    ) # target data: len(cr_drive_phases) x len(t_vec_cycle) x 3 x 2
    target_data[idx, ...] = data_t


# -----------------------
# Fitting
# -----------------------

# Perform CR Hamiltonian tomography
coeffs = []
for idx, a in enumerate(amp_scalings):
    print("-" * 40)
    print(f"fitting for amp = {a:5.4f}")
    try:
        crht = CRHamiltonianTomographyAnalysis(
            ts=ts,
            data=target_data[idx, ...],  # target data: len(amp_scalings) x len(t_vec_cycle) x 3 x 2
        )
        crht.fit_params()
        coeffs.append(crht.interaction_coeffs_MHz)
        fig_analysis = crht.plot_fit_result(do_show=True)
    except:
        print(f"-> failed")
        crht.interaction_coeffs_MHz = {k: None for k, v in crht.interaction_coeffs_MHz.items()}
        coeffs.append({p: None for p in PAULI_2Q})


# -----------------------
# Plotting
# -----------------------

# Prepare the figure for live plotting
fig, axss = plt.subplots(3, 4, figsize=(12, 9), sharex=True, sharey=True)
# plotting data
plot_cr_duration_vs_scan_param(
    control_data,
    target_data,
    ts,
    amp_scalings,
    "cr drive amplitude scaling",
    axss,
)

# Plot the estimated interaction coefficients
fig_summary = plot_interaction_coeffs(coeffs, amp_scalings, xlabel="cr drive amplitude scaling")
plt.show()

# %%
