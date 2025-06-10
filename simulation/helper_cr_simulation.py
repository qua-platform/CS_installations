import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass


# -----------------------
# Base Parameters (GHz → rad/ns)
# -----------------------

two_pi = 2 * np.pi

@dataclass
class BaseParameters:
    omega_c: float = 5.0 * two_pi       # Control qubit frequency (rad/ns)
    omega_t: float = 5.1 * two_pi       # Target qubit frequency (rad/ns)
    alpha_c: float = -0.2 * two_pi      # Control anharmonicity (rad/ns)
    alpha_t: float = -0.2 * two_pi      # Target anharmonicity (rad/ns)
    J: float = 0.01 * two_pi            # Coupling strength (rad/ns)

    C_tc: float = 0.2                   # Capacitive coupling (abs)
    phi_tc: float = 0.2 * two_pi        # Capacitive coupling phase (rad)
    theta_c: float = 0.1 * two_pi       # Path phase difference (rad)


bp = BaseParameters()


class CRHamiltonian:
    def __init__(self,
        A_c, A_t, phi_c, phi_t,
        omega_c=bp.omega_c,
        omega_t=bp.omega_t,
        J=bp.J,
        alpha_c=bp.alpha_c,
        alpha_t=bp.alpha_t,
        C_tc=bp.C_tc,
        theta_c=bp.theta_c,
        phi_tc=bp.phi_tc,
        ):

        self.omega_c = omega_c
        self.omega_t = omega_t
        self.J = J
        self.alpha_c = alpha_c
        self.alpha_t = alpha_t
        self.C_tc = C_tc
        self.phi_tc = phi_tc
        self.phi_ct = -phi_tc
        self.theta_c = theta_c

        self.A_c = A_c
        self.A_t = A_t
        self.phi_c = phi_c
        self.phi_t = phi_t

        self.eps_c = self._compute_eps_c()
        self.eps_t = self._compute_eps_t()

        self.Delta = self._compute_Delta()
        self.nu = self._compute_nu()
        self.mu = self._compute_mu()
        self.b_i = self._compute_bi()
        
        self.ax = self._compute_ax()
        self.ay = self._compute_ay()
        self.az = self._compute_az()
        self.bx = self._compute_bx()
        self.by = self._compute_by()
        self.bz = self._compute_bz()
        self.bi = self._compute_bi()
    
    def _compute_eps_c(self):
        C = self.C_tc * np.exp(1j * self.phi_tc)
        Ac = self.A_c * np.exp(-1j * self.phi_c)
        At = self.A_t * np.exp(-1j * self.phi_t)
        return np.exp(1j * self.theta_c) * Ac + C * At

    def _compute_eps_t(self):
        C = self.C_tc * np.exp(1j * self.phi_tc)
        Ac = self.A_c * np.exp(-1j * self.phi_c)
        At = self.A_t * np.exp(-1j * self.phi_t)
        return C * Ac + At

    def _compute_Delta(self):
        return self.omega_c - self.omega_t

    def _compute_nu(self):
        return -self.eps_c * self.J / (self.Delta + self.alpha_c)

    def _compute_mu(self):
        return -self.eps_c * (self.J / self.Delta) * (self.alpha_c / (self.Delta + self.alpha_c))

    def _compute_ax(self):
        return np.abs(self.nu) * np.cos(self.theta_c - self.phi_c) + np.abs(self.eps_t) * np.cos(self.phi_tc)

    def _compute_ay(self):
        return np.abs(self.nu) * np.sin(self.theta_c - self.phi_c) + np.abs(self.eps_t) * np.sin(self.phi_tc)

    def _compute_az(self):
        return np.abs(self.nu + self.eps_t)**2 / self.alpha_t

    def _compute_bx(self):
        return np.abs(self.mu) * np.cos(self.theta_c - self.phi_c)

    def _compute_by(self):
        return np.abs(self.mu) * np.sin(self.theta_c - self.phi_c)

    def _compute_bz(self):
        zt = self.Delta - self.alpha_t
        zc = self.Delta + self.alpha_c
        return 2 * self.J * self.J * (1 / zt - 1 / zc)

    def _compute_bi(self):
        denom = 2 * self.Delta * (self.Delta + self.alpha_c)
        return np.abs(self.eps_c)**2 * self.alpha_c / denom
    
    def print_params(self):
        print("-" * 100)
        print(f"Delta: {1000 * self.Delta:4.3f} MHz")
        print(f"nu: {1000 * self.nu:4.3f} MHz")
        print(f"mu: {1000 * self.mu:4.3f} MHz")
        print(f"ax: {1000 * self.ax:4.3f} MHz")
        print(f"ay: {1000 * self.ay:4.3f} MHz")
        print(f"az: {1000 * self.az:4.3f} MHz")
        print(f"bx: {1000 * self.bx:4.3f} MHz")
        print(f"by: {1000 * self.by:4.3f} MHz")
        print(f"bz: {1000 * self.bz:4.3f} MHz")
        print(f"bi: {1000 * self.bi:4.3f} MHz")


class CRRabiOscillations:
    def __init__(self, hamiltonian: CRHamiltonian, qc_g: bool): 
        self.h = hamiltonian
        self.qc_g = qc_g
        self.OmegaX, self.OmegaY, self.OmegaZ = self._compute_Omega_components()
        self.Omega = self._compute_Omega()

    def _compute_Omega_components(self):
        sign = 1 if self.qc_g else -1
        OmegaX = self.h.ax + sign * self.h.bx
        OmegaY = self.h.ay + sign * self.h.by
        OmegaZ = self.h.az + sign * self.h.bz
        return OmegaX, OmegaY, OmegaZ

    def _compute_Omega(self):
        return np.sqrt(self.OmegaX**2 + self.OmegaY**2 + self.OmegaZ**2)

    def compute_components(self, ts):
        denom = self.Omega**2
        cos = np.cos(self.Omega * ts)
        sin = np.sin(self.Omega * ts)
        X = self.OmegaX
        Y = self.OmegaY
        Z = self.OmegaZ
        R = self.Omega

        ExpX = (Z * X * (1 - cos) + R * Y * sin) / denom
        ExpY = (Z * Y * (1 - cos) - R * X * sin) / denom
        ExpZ = (Z * Z + (X * X + Y * Y) * cos) / denom
        return ExpX, ExpY, ExpZ


def plot_raw_data(ts, X0, Y0, Z0, X1, Y1, Z1):
    fig, axs = plt.subplots(3, 1, figsize=(5, 6))
    axs[0].plot(ts, X0, color='b', label='Qc=g')
    axs[1].plot(ts, Y0, color='b')
    axs[2].plot(ts, Z0, color='b')
    axs[0].plot(ts, X1, color='c', label='Qc=e')
    axs[1].plot(ts, Y1, color='c')
    axs[2].plot(ts, Z1, color='c')

    for ax in axs:
        ax.set_ylim([-1.05, 1.05])
        ax.set_xlim([0, ts[-1]])

    axs[0].set_ylabel(r'$\langle X \rangle$')
    axs[1].set_ylabel(r'$\langle Y \rangle$')
    axs[2].set_ylabel(r'$\langle Z \rangle$')
    axs[2].set_xlabel('Time (ns)')
    axs[0].legend()
    return fig