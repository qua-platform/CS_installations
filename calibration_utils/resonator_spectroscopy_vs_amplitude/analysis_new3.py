# %%
import glob
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from scipy.stats import gaussian_kde
from itertools import groupby
from operator import itemgetter
# === Functions ===

def prepare_data(ds, qubit):
    """Assigns freq_MHz and selects a qubit slice."""
    return ds.assign_coords(freq_MHz=ds.freq / 1e6).loc[{'qubit': qubit}]

def moving_average(x, window_size=5):
    pad_width = window_size // 2
    padded = np.pad(x, pad_width, mode='edge')  # replicate edge values
    kernel = np.ones(window_size) / window_size
    return np.convolve(padded, kernel, mode='valid')

def find_two_main_peaks(data_2d, axis=1):
    """Finds the two highest peaks in mean-over-axis data (e.g., averaged over power)."""
    avg_data = data_2d.mean(axis=axis)
    avg_data = moving_average(avg_data)
    flipped_data = avg_data.max() - avg_data  # convert dips to peaks
    peaks, _ = find_peaks(flipped_data)
    top_two = peaks[np.argsort(flipped_data[peaks])[-2:]]
    return np.sort(top_two), flipped_data

def find_most_deviant_power(data_2d, freq_idx):
    """Finds the power index with the largest deviation from a freq-averaged subset."""
    avg_all = data_2d.mean(axis=0)
    avg_cut = data_2d[slice(freq_idx-2,freq_idx+2), :].mean(axis=0)
    deviation = avg_all - avg_cut
    peaks, _ = find_peaks(deviation)
    top_peak = peaks[np.argmax(deviation[peaks])]
    return top_peak, deviation, avg_cut, avg_all

def detect_peak_regions_with_kde(data, freq, power, delta_x=0.01, bandwidth=None, x1=None, delta=0.01):
    """
    Applies KDE along freq axis for each power strip, detects peaks, and finds the contiguous
    region along power where peaks stay close to x1 (within delta).

    Parameters:
    - data: 2D array (freq × power)
    - freq: 1D array of frequency values
    - power: 1D array of power values
    - delta_x: resolution of KDE sampling grid
    - bandwidth: optional float or 'scott'/'silverman' for KDE
    - x1: reference peak position (if None, auto-detect top 1 or 2 modes)
    - delta: closeness threshold for determining x1-like region

    Returns:
    - x1: the most common peak position
    - peak_freqs: detected peak freq per power strip
    - (start_power, end_power): bounds of contiguous x1-like region
    """
    num_power = data.shape[1]
    peak_freqs = []

    freq_grid = np.arange(freq.min(), freq.max(), delta_x)

    for i in range(num_power):
        strip = data[:, i]
        weights = strip - strip.min()  # subtract background
        if np.sum(weights) == 0:
            peak_freqs.append(np.nan)
            continue
        kde = gaussian_kde(freq, weights=weights, bw_method=bandwidth)
        density = kde(freq_grid)
        peak_idx = np.argmax(density)
        peak_freqs.append(freq_grid[peak_idx])

    peak_freqs = np.array(peak_freqs)

    # Automatically find the two most common peaks via histogram if x1 not given
    if x1 is None:
        hist, bin_edges = np.histogram(peak_freqs[~np.isnan(peak_freqs)], bins=100)
        bin_centers = 0.5 * (bin_edges[1:] + bin_edges[:-1])
        sorted_peaks = bin_centers[np.argsort(hist)[::-1]]
        x1 = sorted_peaks[0]  # most common peak

    # Find region where peak_freq is close to x1
    mask = np.abs(peak_freqs - x1) < delta
    idx_true = np.where(mask)[0]

    groups = []
    for k, g in groupby(enumerate(idx_true), lambda i_x: i_x[0] - i_x[1]):
        group = list(map(itemgetter(1), g))
        groups.append(group)

    if not groups:
        return x1, peak_freqs, None

    largest_region = max(groups, key=len)
    start_idx = largest_region[0]
    end_idx = largest_region[-1]
    pick_idx = int(0.8 * end_idx + 0.2 * start_idx)

    return x1, peak_freqs, (power[start_idx], power[end_idx]), pick_idx

# === Pipeline Execution ===

paths = glob.glob("/workspaces/data/QPU_project/2025-04-29/*Resonator_Spectroscopy_vs_amplitude**/ds.h5")
paths.sort()

for path in paths:
    ds = xr.open_dataset(path, engine="netcdf4")
    for qubit in ds.qubit.values.tolist():

        ds_sliced = prepare_data(ds, qubit=qubit)
        freq = ds_sliced.freq_MHz
        power = ds_sliced.power_dbm
        data = ds_sliced.IQ_abs.values
        data = data / data.mean(axis=0, keepdims=True)
        data = data.max() - data

        x1, peak_freqs, region, pick_idx = detect_peak_regions_with_kde(data, freq, power, delta=0.1)


        import matplotlib.pyplot as plt

        # Plot the 2D charge map
        plt.figure(figsize=(8, 6))
        plt.pcolormesh(power, freq, data, shading='auto', cmap='viridis')
        plt.colorbar(label='Signal')

        # Overlay the detected peak positions
        plt.plot(power, peak_freqs, color='red', label='Detected peak')

        # Mark x1-like region with vertical lines
        if region:
            plt.axhline(y=x1, color='m', linestyle='--', label='dispersive regime')
            plt.axvline(region[0], color='orange', linestyle='--', label='x1-like region start')
            plt.axvline(region[1], color='orange', linestyle='--', label='x1-like region end')
            plt.plot(power[pick_idx], x1, marker="*", color="r", markersize=15, label="Chosen Point")
            
        plt.xlabel('Power (arb. units)')
        plt.ylabel('Frequency (arb. units)')
        plt.title('Peak Drift & x1 Region Detection')
        plt.legend()
        plt.tight_layout()
        plt.show()

# %%
