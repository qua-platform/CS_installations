# %%
import numpy as np
import matplotlib.pyplot as plt
import qutip as qt  # Explicitly import qutip as qt

# -----------------------
# Parameters (GHz → rad/ns)
# -----------------------
Nc, Nt = 3, 3  # Number of energy levels per transmon
omega_c = 5.0 * 2 * np.pi        # Control qubit frequency (rad/ns)
omega_t = 5.1 * 2 * np.pi        # Target qubit frequency (rad/ns)
alpha_c = -0.2 * 2 * np.pi       # Control anharmonicity (rad/ns)
alpha_t = -0.2 * 2 * np.pi       # Target anharmonicity (rad/ns)
J = 0.01 * 2 * np.pi             # Coupling strength (rad/ns)
A_c = 0.005 * 2 * np.pi           # CR drive amplitude (rad/ns)
A_t = 0.002 * 2 * np.pi           # Cancel drive amplitude (rad/ns)
phi = 0.3* np.pi                  # Cancel drive phase (radians)

# -----------------------
# Time Grid
# -----------------------
tlist = np.linspace(0, 200, 1000)  # Time (ns)

# -----------------------
# Operators
# -----------------------
a = qt.tensor(qt.destroy(Nc), qt.qeye(Nt))  # Control
b = qt.tensor(qt.qeye(Nc), qt.destroy(Nt))  # Target

# -----------------------
# Hamiltonian Components
# -----------------------
# Static Hamiltonian: Duffing oscillator + coupling
H0 = (
    omega_c * a.dag() * a + (alpha_c / 2) * a.dag()**2 * a**2 +
    omega_t * b.dag() * b + (alpha_t / 2) * b.dag()**2 * b**2 +
    J * (a.dag() * b + a * b.dag())
)

# Time-dependent drive Hamiltonians
H_drive = [
    [a + a.dag(), lambda t, args: A_c * np.cos(omega_t * t)],                     # CR drive on control
    [b + b.dag(), lambda t, args: A_t * np.cos(omega_t * t + phi)]               # Cancel drive on target
]

H = [H0] + H_drive

# -----------------------
# Initial State: |00⟩
# -----------------------
psi0 = qt.tensor(qt.basis(Nc, 0), qt.basis(Nt, 0))

# -----------------------
# Pauli-like Operators for 3-Level Truncated Qubits
# -----------------------

# Projectors into |0⟩ and |1⟩ subspace
proj_01_c = qt.Qobj(np.eye(2, Nc), dims=[[2], [Nc]])
proj_01_t = qt.Qobj(np.eye(2, Nt), dims=[[2], [Nt]])

# Qubit Pauli matrices
X_qubit = qt.Qobj([[0, 1], [1, 0]], dims=[[2], [2]])
Y_qubit = qt.Qobj([[0, -1j], [1j, 0]], dims=[[2], [2]])
Z_qubit = qt.Qobj([[1, 0], [0, -1]], dims=[[2], [2]])

# Expand into full space via projection
sx_a = proj_01_c.dag() * X_qubit * proj_01_c
sy_a = proj_01_c.dag() * Y_qubit * proj_01_c
sz_a = proj_01_c.dag() * Z_qubit * proj_01_c

sx_b = proj_01_t.dag() * X_qubit * proj_01_t
sy_b = proj_01_t.dag() * Y_qubit * proj_01_t
sz_b = proj_01_t.dag() * Z_qubit * proj_01_t

# Tensor into total Hilbert space
sx_a_full = qt.tensor(sx_a, qt.qeye(Nt))
sy_a_full = qt.tensor(sy_a, qt.qeye(Nt))
sz_a_full = qt.tensor(sz_a, qt.qeye(Nt))

sx_b_full = qt.tensor(qt.qeye(Nc), sx_b)
sy_b_full = qt.tensor(qt.qeye(Nc), sy_b)
sz_b_full = qt.tensor(qt.qeye(Nc), sz_b)

# -----------------------
# Time Evolution
# -----------------------
result = qt.mesolve(H, psi0, tlist, [], [sx_a_full, sy_a_full, sz_a_full,
                                         sx_b_full, sy_b_full, sz_b_full])

# -----------------------
# Extract Expectation Values
# -----------------------
sx_a_vals, sy_a_vals, sz_a_vals = result.expect[0:3]
sx_b_vals, sy_b_vals, sz_b_vals = result.expect[3:6]

# -----------------------
# Plot Results
# -----------------------
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(tlist, sx_a_vals, label='⟨X⟩ control')
plt.plot(tlist, sy_a_vals, label='⟨Y⟩ control')
plt.plot(tlist, sz_a_vals, label='⟨Z⟩ control')
plt.title('Control Qubit Bloch Components')
plt.ylabel('Expectation')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(tlist, sx_b_vals, label='⟨X⟩ target')
plt.plot(tlist, sy_b_vals, label='⟨Y⟩ target')
plt.plot(tlist, sz_b_vals, label='⟨Z⟩ target')
plt.title('Target Qubit Bloch Components')
plt.xlabel('Time [ns]')
plt.ylabel('Expectation')
plt.legend()

plt.tight_layout()
plt.show()

# %%
