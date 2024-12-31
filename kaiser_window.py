# %%
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import \
    i0  # Zeroth-order modified Bessel function of the first kind


def kaiser_window(T: int, alpha: float) -> np.ndarray:
    """
    Generate a Kaiser window for digital signal processing.

    :param T: Length of the window (number of points - 1).
    :param alpha: Shape parameter that determines the trade-off between main lobe width and side lobe level.
    :return: A numpy array of the Kaiser window values.
    """
    # Compute the normalized indices
    t = np.arange(T)
    x = (2 * t / (T - 1)) - 1

    # Calculate the Kaiser window using the zeroth-order modified Bessel function
    window = i0(np.pi * alpha * np.sqrt(1 - x**2)) / i0(np.pi * alpha)

    return window


# Parameters
T = 40  # Window length
alpha = 2.0  # Shape parameter

# Generate the Kaiser window
kaiser_win = kaiser_window(T, alpha)

# FFT of the Kaiser window
fft_kaiser = np.fft.fftshift(
    np.fft.fft(kaiser_win, n=1024)
)  # FFT with zero-padding for better resolution
fft_freqs = np.fft.fftshift(
    np.fft.fftfreq(len(fft_kaiser), d=1 / T)
)  # Corresponding frequencies

# Magnitude of FFT
fft_magnitude = 20 * np.log10(
    np.abs(fft_kaiser) / np.max(np.abs(fft_kaiser))
)  # In decibels (normalized)

# Plot the Kaiser window
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(kaiser_win, label=f"Kaiser Window (T={T}, α={alpha})")
plt.title("Kaiser Window")
plt.xlabel("Sample Index")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()

# Plot the FFT magnitude
plt.subplot(1, 2, 2)
plt.plot(fft_freqs, fft_magnitude, label="FFT of Kaiser Window")
plt.title("FFT of Kaiser Window")
plt.xlabel("Frequency (Normalized)")
plt.ylabel("Magnitude (dB)")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
