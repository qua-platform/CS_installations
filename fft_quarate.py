#%%
"""
Load RF signal (time-domain, in mV), compute its FFT, 
and plot both time- and frequency-domain representations.
"""

import numpy as np
import matplotlib.pyplot as plt
import xarray as xr
import numpy as np
import json, os
import base64
import io
from pathlib import Path
from math import ceil
from scipy import signal

# --------------------------------------------------------------------
# Common helper: xarray open_dataset with multiple engine attempts
# --------------------------------------------------------------------
def open_xr_dataset(path, engines=("h5netcdf", "netcdf4", None)):
    """
    Try xarray.open_dataset with multiple engines.
    Return the first successful result, or raise the last exception if all fail.
    """
    last_error = None
    for eng in engines:
        try:
            print(f"  trying engine={eng} ... ", end="")
            ds = xr.open_dataset(path, engine=eng)
            print("✓ success")
            return ds
        except Exception as e:
            print(f"✗ {type(e).__name__}: {e}")
            last_error = e
    raise last_error  # Propagate exception for caller to handle if all fail


# -------------------------------------------------------------------
# 1. Data Loader
# -------------------------------------------------------------------
def load_tof_data(folder_path):
    """Load TOF experiment data"""
    try:
        folder_path = os.path.normpath(folder_path)

        ds_raw_path  = os.path.join(folder_path, "ds_raw.h5")
        ds_fit_path  = os.path.join(folder_path, "ds_fit.h5")
        data_json_path = os.path.join(folder_path, "data.json")
        node_json_path = os.path.join(folder_path, "node.json")

        # Check required file existence
        required = [ds_raw_path, ds_fit_path, data_json_path, node_json_path]
        if not all(os.path.exists(p) for p in required):
            print(f"[load_tof_data] Missing required files in {folder_path}")
            return None

        print(f"[load_tof_data] opening datasets in {folder_path}")
        ds_raw = open_xr_dataset(ds_raw_path)
        ds_fit = open_xr_dataset(ds_fit_path)

        with open(data_json_path, "r", encoding="utf-8") as f:
            data_json = json.load(f)
        with open(node_json_path, "r", encoding="utf-8") as f:
            node_json = json.load(f)

        qubits       = ds_raw["qubit"].values
        n_qubits     = len(qubits)
        success      = ds_fit["success"].values
        delays       = ds_fit["delay"].values
        thresholds   = ds_fit["threshold"].values
        readout_time = ds_raw["readout_time"].values

        print(f"[load_tof_data] loaded OK – {n_qubits} qubits")
        return dict(
            ds_raw=ds_raw,
            ds_fit=ds_fit,
            data_json=data_json,
            node_json=node_json,
            qubits=qubits,
            n_qubits=n_qubits,
            success=success,
            delays=delays,
            thresholds=thresholds,
            readout_time=readout_time,
        )

    except Exception as e:
        print(f"[load_tof_data] ERROR: {e}")
        import traceback
        traceback.print_exc()
        return None

#%%
### If you only have voltage samples:
x = np.loadtxt("my_rf_samples.csv")    # shape (N,)
fs = 1e9                               # e.g. 1 GHz sampling rate
t  = np.arange(len(x)) / fs            # time vector in seconds
###

def generate_rf_signal(fs, duration, freqs, amplitudes, noise_std=0.0):
    """
    Generate a time-domain RF signal.

    Parameters
    ----------
    fs : float
        Sampling frequency in Hz.
    duration : float
        Duration of the signal in seconds.
    freqs : list of float
        Signal component frequencies in Hz.
    amplitudes : list of float
        Corresponding amplitudes (in mV) for each component.
    noise_std : float, optional
        Standard deviation of additive Gaussian noise (in mV).

    Returns
    -------
    t : ndarray
        Time vector (s).
    x : ndarray
        Signal samples (mV).
    """
    t = np.arange(0, duration, 1/fs)
    x = np.zeros_like(t)
    # Sum sine components
    for f, A in zip(freqs, amplitudes):
        x += A * np.sin(2 * np.pi * f * t)
    # Add Gaussian noise
    if noise_std > 0:
        x += np.random.normal(scale=noise_std, size=t.shape)
    return t, x

def compute_fft(x, fs):
    """
    Compute the one-sided FFT of a real-valued signal.

    Parameters
    ----------
    x : ndarray
        Time-domain signal.
    fs : float
        Sampling frequency in Hz.

    Returns
    -------
    freqs : ndarray
        Frequency bins (Hz).
    X_mag : ndarray
        Magnitude spectrum.
    """
    N = len(x)
    # Compute FFT and normalize
    X = np.fft.fft(x)
    X = X[:N//2]  # one-sided
    X_mag = (2.0 / N) * np.abs(X)
    freqs = np.fft.fftfreq(N, d=1/fs)[:N//2]
    return freqs, X_mag

def plot_time_and_freq(t, x, freqs, X_mag):
    """
    Plot time-domain and frequency-domain representations.
    """
    plt.figure(figsize=(12, 5))

    # Time-domain
    plt.subplot(1, 2, 1)
    plt.plot(t * 1e3, x)  # time in ms
    plt.xlabel("Time (ms)")
    plt.ylabel("Amplitude (mV)")
    plt.title("Time-Domain RF Signal")
    plt.grid(True)

    # Frequency-domain
    plt.subplot(1, 2, 2)
    plt.plot(freqs * 1e-3, X_mag)  # freq in kHz
    plt.xlabel("Frequency (kHz)")
    plt.ylabel("Magnitude (mV)")
    plt.title("Frequency Spectrum (FFT)")
    plt.grid(True)

    plt.tight_layout()
    plt.show()

def main():
    # --- PARAMETERS ---
    fs = 1e6            # Sampling rate: 1 MHz
    duration = 1e-3     # Signal duration: 1 ms
    freqs = [100e3, 200e3]   # Two tones: 100 kHz & 200 kHz
    amplitudes = [500.0, 300.0]  # Amplitudes in mV
    noise_std = 50.0    # Noise σ in mV (set to 0 for no noise)

    # Generate signal
    t, x = generate_rf_signal(fs, duration, freqs, amplitudes, noise_std)

    # Compute FFT
    freqs_axis, X_mag = compute_fft(x, fs)

    # Plot results
    plot_time_and_freq(t, x, freqs_axis, X_mag)

if __name__ == "__main__":
    main()
