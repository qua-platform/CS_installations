from dataclasses import dataclass, field
from typing import Dict
import numpy as np
from scipy.optimize import curve_fit
from scipy.signal import find_peaks
import matplotlib.pyplot as plt


STATES = ["0", "1"]
COMPONENTS = ["x", "y", "z"]
PAULI_2Q = ["IX", "IY", "IZ", "ZX", "ZY", "ZZ"]


@dataclass
class PauliMeasurement:
    ts: np.ndarray
    data: Dict[str, Dict[str, np.ndarray]] = field(default_factory=dict)

    def __post_init__(self):
        for state in STATES:
            if state not in self.data:
                raise ValueError(f"Missing data for state {state}.")

            state_data = self.data[state]
            for component in COMPONENTS:
                if component not in state_data:
                    raise ValueError(f"Missing data for component {component} in state {state}.")

                value = state_data[component]
                if not isinstance(value, np.ndarray) or value.ndim != 1:
                    raise ValueError(f"Data for component {component} in state {state} must be a 1D numpy array.")

                if len(value) != len(self.ts):
                    raise ValueError(
                        f"Data for component {component} in state {state} must have the same length as ts."
                    )


class CRHamiltonianTomographyFunctions:
    def __init__(self):
        """Initialize the class."""
        pass

    def _compute_omega_squared(self, d, mx, my):
        """
        Calculate the omega squared based on the parameters.

        :param d: delta.
        :param mx: omega X.
        :param my: omega y.

        :return: omega squared.
        """
        return d**2 + mx**2 + my**2

    def _compute_X(self, ts, d, mx, my):
        """
        Calculate expectation value of target <X> based on the parameters.

        :param ts: durations of CR drive.
        :param d: delta.
        :param mx: omega X.
        :param my: omega y.

        :return: <X>.
        """
        m2 = self._compute_omega_squared(d, mx, my)
        m = np.sqrt(m2)
        return (-d * mx + d * mx * np.cos(m * ts) + m * my * np.sin(m * ts)) / m2

    def _compute_Y(self, ts, d, mx, my):
        """
        Calculate expectation value of target <Y> based on the parameters.

        :param ts: durations of CR drive.
        :param d: delta.
        :param mx: omega X.
        :param my: omega y.

        :return: <Y>.
        """
        m2 = self._compute_omega_squared(d, mx, my)
        m = np.sqrt(m2)
        return (+d * my - d * my * np.cos(m * ts) - m * mx * np.sin(m * ts)) / m2

    def _compute_Z(self, ts, d, mx, my):
        """
        Calculate expectation value of target <Z> based on the parameters.

        :param ts: durations of CR drive.
        :param d: delta.
        :param mx: omega X.
        :param my: omega y.

        :return: <Z>.
        """
        m2 = self._compute_omega_squared(d, mx, my)
        m = np.sqrt(m2)
        return (+(d**2) + (mx**2 + my**2) * np.cos(m * ts)) / m2

    def compute_R(self, xyz0, xyz1):
        """
        Compute the root mean square of the sum of two sets of <X>, <Y>, and <Z> data.
        R = sqrt((X0 + X1) ** 2 + (Y0 + Y1) ** 2 (Z0 + Z1) ** 2)
        , where 0 (1) stands for control state = 0 (1).

        :param xyz0: Dictionary containing 'x', 'y', 'z' data for control state 0.
        :param xyz1: Dictionary containing 'x', 'y', 'z' data for control state 1.

        :return: Computed R value.
        """
        return np.sqrt((xyz0["x"] + xyz1["x"]) ** 2 + (xyz0["y"] + xyz1["y"]) ** 2 + (xyz0["z"] + xyz1["z"]) ** 2) / 2

    def compute_XYZ(self, ts, d, mx, my, noise=0, random_state=0, clip=False):
        """
        Compute the expected values <X>, <Y>, <Z> for a given set of parameters and add noise if specified.

        :param ts: durations of CR drive.
        :param d: delta.
        :param mx: omega X.
        :param my: omega y.
        :param noise: Standard deviation of Gaussian noise to add to the data.
        :param random_state: Seed for the random number generator.
        :param clip: Boolean flag to clip the noisy data between -1 and 1.

        :return: Dictionary with keys 'x', 'y', 'z' containing the computed values.
        """
        xyz = {
            "x": self._compute_X(ts, d, mx, my),
            "y": self._compute_Y(ts, d, mx, my),
            "z": self._compute_Z(ts, d, mx, my),
        }
        if noise > 0:
            np.random.seed(random_state)
            for c in COMPONENTS:
                xyz[c] += np.random.normal(scale=noise, size=xyz[c].shape)
                if clip:
                    xyz[c] = np.clip(xyz[c], -1.0, 1.0)

        return xyz


class CRHamiltonianTomography(CRHamiltonianTomographyFunctions):
    def __init__(self, ts, xyz):
        """
        CR Hamiltonian Tomography class.

        :param ts: durations of CR drive.
        :param xyz: Dictionary containing measurement data for 'x', 'y', and 'z' components.
        """
        self.ts = ts
        self.pauli_meas = PauliMeasurement(ts=ts, data=xyz)
        self.params_fitted = {s: [] for s in STATES}
        self.interaction_coeffs = {p: None for p in PAULI_2Q}

    def _bloch_vec_evolution(self, ts, d, mx, my):
        """
        Calculate the expected evolution of the Bloch vector components over time.

        :param ts: durations of CR drive.
        :param d, mx, my: Hamiltonian parameters.
        :return: Array of expected 'x', 'y', and 'z' components concatenated.
        """
        ts_len = len(ts) // len(COMPONENTS)
        xyz = self.compute_XYZ(ts[:ts_len], *[d, mx, my])
        return np.hstack([xyz[c] for c in COMPONENTS])

    def _fit_bloch_vec_evolution(self, xyz, p0):
        """
        Fit the model to the data using non-linear least squares.

        :param xyz: Measured data for the Bloch vector components.
        :param p0: Initial guess for the parameters.
        :return: Fitted parameters and the covariance of the parameters.
        """
        return curve_fit(
            f=self._bloch_vec_evolution,
            xdata=np.tile(self.ts, len(COMPONENTS)),
            ydata=np.hstack([xyz[c] for c in COMPONENTS]),
            p0=p0,
            method="trf",
        )

    def _find_dominant_frequency(self, data):
        """
        Identify the dominant frequency in the provided data using Fourier transform.

        :param data: Time-series data from which to extract the frequency.
        :return: Dominant frequency value.
        """
        N = len(self.ts)
        dt = self.ts[1] - self.ts[0]
        freq = np.fft.fftfreq(N, dt)
        spectrum = np.abs(np.fft.fft(data - data.mean()))

        # Find peaks in the frequency spectrum (DC removed alraedy)
        peaks, _ = find_peaks(spectrum, prominence=0.1 * N)
        if len(peaks) == 0:
            print("the data should have more than 1 period")
        highest_peak_idx = np.argmax(spectrum[peaks])

        # Identify dominant frequency (peak frequency)
        return freq[peaks[highest_peak_idx]]

    def _pick_params_init(self, xyz):
        """
        Choose initial parameter estimates for the fitting process based on frequency analysis.

        :param xyz: Measured Bloch vector components.
        :return: Array of initial parameter guesses.
        """
        freq_inits = [self._find_dominant_frequency(data=xyz[c]) for c in COMPONENTS]

        # pick the initial omega as median of estimated omega from x, y, z
        freq_init = np.median(np.array(freq_inits))

        # omega_init = initial value for sqrt(delta ** 2 + omega_x ** 2 + omega_y ** 2)
        # we pick the initial value for each parameter only from all positives
        theta, phi = 0.5 * np.pi * np.random.rand(2)
        return (
            2
            * np.pi
            * freq_init
            * np.array(
                [
                    np.cos(theta),  # delta
                    np.sin(theta) * np.cos(phi),  # omega_x
                    np.sin(theta) * np.sin(phi),  # omega_y
                ]
            )
        )

    def fit_params(self, params_init=None, random_state=0, do_print=True):
        """
        Fit the Hamiltonian parameters for each state and compute interaction rates.

        :param params_init: Initial parameter estimates (optional).
        :param random_state: Seed for the random number generator.
        :param _print: Boolean flag to control the printing of fitting results.
        :return: Self.
        """
        np.random.seed(random_state)
        for st in STATES:
            if params_init is None:
                p0 = self._pick_params_init(xyz=self.pauli_meas.data[st])
            else:
                p0 = params_init[st]

            self.params_fitted[st], _ = self._fit_bloch_vec_evolution(
                xyz=self.pauli_meas.data[st],
                p0=p0,
            )

        # compute interaction rates based on the fitted params
        self.compute_interaction_rates()

        # print the fitted parameters and interaction coefficents
        if do_print:
            for st in STATES:
                ps = self.params_fitted[st]
                print(f"state = {st}: delta = {ps[0]:.3f}, omega_x = {ps[1]:.3f}, omega_y = {ps[2]:.3f}")
            for op in PAULI_2Q:
                print(f"{op}: {1e3 * self.interaction_coeffs[op]:.3f} MHz")

        return self

    def compute_interaction_rates(self):
        """
        Compute the interaction coefficients from fitted Hamiltonian parameters.
        """
        # get the fitted params
        d0, mx0, my0 = self.params_fitted["0"]
        d1, mx1, my1 = self.params_fitted["1"]
        # compute the coefficients for each interaction terms
        self.interaction_coeffs["IX"] = (mx0 + mx1) / 2
        self.interaction_coeffs["IY"] = (my0 + my1) / 2
        self.interaction_coeffs["IZ"] = (d0 + d1) / 2
        self.interaction_coeffs["ZX"] = (mx0 - mx1) / 2
        self.interaction_coeffs["ZY"] = (my0 - my1) / 2
        self.interaction_coeffs["ZZ"] = (d0 - d1) / 2

    def get_interaction_rates(self):
        """
        Get the computed interaction rates after fitting.

        :raises RuntimeError: If any interaction coefficient has not been computed yet.
        :return: Dictionary of interaction coefficients.
        """
        if any(value is None for value in self.interaction_coeffs.values()):
            raise RuntimeError("some of the interaction coefficients have not been computed yet.")
        return self.interaction_coeffs

    def plot_fit_result(self):
        """
        Plot the original measurement data along with the fitted data and interaction rates.

        :return: The matplotlib figure object containing the plots.
        """
        fig, axs = plt.subplots(4, 1, figsize=(10, 10), sharex=True, sharey=True)

        if self.params_fitted["0"] is None or self.params_fitted["1"] is None:
            raise RuntimeError("fitting has not been done yet")

        if any(value is None for value in self.interaction_coeffs.values()):
            raise RuntimeError("some of the interaction coefficients have not been computed yet.")

        for ax, cmp in zip(axs, COMPONENTS):
            v0 = self.pauli_meas.data["0"][cmp]
            v1 = self.pauli_meas.data["1"][cmp]
            if cmp == "x":
                eV0 = self._compute_X(self.ts, *self.params_fitted["0"])
                eV1 = self._compute_X(self.ts, *self.params_fitted["1"])
            elif cmp == "y":
                eV0 = self._compute_Y(self.ts, *self.params_fitted["0"])
                eV1 = self._compute_Y(self.ts, *self.params_fitted["1"])
            elif cmp == "z":
                eV0 = self._compute_Z(self.ts, *self.params_fitted["0"])
                eV1 = self._compute_Z(self.ts, *self.params_fitted["1"])

            ax.scatter(self.ts, v0, s=20, color="b", label="ctrl in |0>")
            ax.scatter(self.ts, v1, s=20, color="r", label="ctrl in |1>")
            ax.plot(self.ts, eV0, lw=4.0, color="b", alpha=0.5)
            ax.plot(self.ts, eV1, lw=4.0, color="r", alpha=0.5)
            ax.set_ylabel(f"<{cmp}(t)>", fontsize=16)

            if cmp == "x":
                ax.set_title("Pauli Expectation Value", fontsize=16)
                ax.legend(["0 meas", "1 meas", "0 fit", "1 fit"], fontsize=10)
            elif cmp == "y":
                ax.set_title(
                    "IX = %.2f MHz, IY = %.2f MHz, IZ = %.2f MHz"
                    % (
                        self.interaction_coeffs["IX"] * 1e3,
                        self.interaction_coeffs["IY"] * 1e3,
                        self.interaction_coeffs["IZ"] * 1e3,
                    ),
                    fontsize=16,
                )
            elif cmp == "z":
                ax.set_title(
                    "ZX = %.2f MHz, ZY = %.2f MHz, ZZ = %.2f MHz"
                    % (
                        self.interaction_coeffs["ZX"] * 1e3,
                        self.interaction_coeffs["ZY"] * 1e3,
                        self.interaction_coeffs["ZZ"] * 1e3,
                    ),
                    fontsize=16,
                )

        for ax in axs:
            ax.hlines(y=0, xmin=self.ts[0], xmax=self.ts[-1], lw=1.0, color="k", alpha=0.2)
            ax.set_xlim((self.ts[0], self.ts[-1]))

        # plot "R"
        R = self.compute_R(self.pauli_meas.data["0"], self.pauli_meas.data["1"])
        axs[3].plot(self.ts, R, "k")
        axs[3].set_xlabel("time")
        axs[3].set_ylabel("R", fontsize=16)
        plt.tight_layout()
        plt.show()

        return fig
