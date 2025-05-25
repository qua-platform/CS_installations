# %%
import glob
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

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

# === Pipeline Execution ===

paths = glob.glob("/workspaces/data/QPU_project/2025-04-29/*Resonator_Spectroscopy_vs_amplitude**/ds.h5")
paths.sort()

for path in paths:
    ds = xr.open_dataset(path, engine="netcdf4")
    for qubit in ds.qubit.values.tolist():
        # Step 1: Prepare dataset
        ds_sliced = prepare_data(ds, qubit=qubit)
        freq = ds_sliced.freq_MHz
        power = ds_sliced.power_dbm
        data = ds_sliced.IQ_abs.values
        data = data / data.mean(axis=0, keepdims=True)

        # Step 2: Find top 2 frequency peaks
        top_freq_indices, freq_profile = find_two_main_peaks(data)
        peak_freqs = freq[top_freq_indices].values
        print("Top 2 frequency peak indices:", top_freq_indices)
        print("Top 2 frequency values [MHz]:", peak_freqs)
        print("Peak values:", freq_profile[top_freq_indices])

        # Step 3: Find most deviant power point
        top_power_index, power_deviation, avg_cut, avg_all = find_most_deviant_power(data, top_freq_indices[1])
        power_pick_index = top_power_index - 5
        print("Pikced Power index:", power_pick_index)
        print("Top power deviation index:", top_power_index)
        print("Power value:", power[top_power_index].item())
        print("Deviation:", power_deviation[top_power_index])



        # === Visualization ===

        fig, axs = plt.subplots(2, 2, figsize=(12, 8))

        # (0, 0): 2D data map
        pcm = axs[0, 0].pcolormesh(power, freq, np.log(data), shading="auto")
        fig.colorbar(pcm, ax=axs[0, 0])
        axs[0, 0].set_title("IQ_abs vs Frequency and Power")
        axs[0, 0].set_xlabel("Power")
        axs[0, 0].set_ylabel("Frequency [MHz]")
        # Horizontal lines at both peak frequencies
        axs[0, 0].hlines(peak_freqs, xmin=power.min(), xmax=power.max(), colors=["g", "m"], linestyles="--")
        # Add star marker at the chosen power + higher frequency
        higher_freq_idx = top_freq_indices[1]  # Assuming top_two are sorted by frequency
        axs[0, 0].plot(power[power_pick_index], freq[higher_freq_idx], marker="*", color="r", markersize=15, label="Chosen Point")
        axs[0, 0].legend()

        # (0, 1): Frequency-averaged data and peaks
        axs[0, 1].plot(freq, data.mean(axis=1), label="Mean over power")
        axs[0, 1].axvline(x=peak_freqs[0], color="g", linestyle="--", label=f"Peak 1: {peak_freqs[0]:.4f} MHz")
        axs[0, 1].axvline(x=peak_freqs[1], color="m", linestyle="--", label=f"Peak 2: {peak_freqs[1]:.4f} MHz")
        axs[0, 1].set_title("Top Frequency Peaks")
        axs[0, 1].set_xlabel("Frequency [MHz]")
        axs[0, 1].legend()

        # (1, 0): Frequency-cut and all-power averages
        axs[1, 0].plot(power, avg_cut, color="m", label=f"Avg (freq={freq[higher_freq_idx]:1.3f} MHz)")
        axs[1, 0].plot(power, avg_all, color="c", label="Avg (all freq)", linestyle="--")
        axs[1, 0].set_title("Power Sweep Comparison")
        axs[1, 0].set_xlabel("Power")
        axs[1, 0].legend()

        # (1, 1): Deviation
        axs[1, 1].plot(power, power_deviation, color="m", label="Deviation = all - cut")
        axs[1, 1].axvline(x=power[top_power_index], color="k", linestyle="--", label="Peak")
        axs[1, 1].axvline(x=power[power_pick_index], color="r", linestyle="--", label="Picked Power")
        axs[1, 1].set_title("Deviation from Mean Power Response")
        axs[1, 1].set_xlabel("Power")
        axs[1, 1].legend()

        plt.tight_layout()
        plt.show()
        
        plt.pause(1)

        break
# %%

# data_norm = data / data.mean(axis=0, keepdims=True)
# # plt.pcolor(power, freq, data_norm)
# # # plt.show()

# d = 5
# n = len(power) // 5 + 1
# cc = np.linspace(0, 1, n)
# for i in range(0, len(power), d):
#     j = i + d if i + d < len(power) else len(power)
#     k = i // d
#     data_norm_avg = data_norm[:, i:j].mean(axis=1)
#     plt.plot(freq, data_norm_avg, color=(cc[k], 0, 1 - cc[k]))
# plt.show()



import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from scipy.stats import gaussian_kde

# Assume:
# data.shape = (len(freq), len(power))
# freq and power are 1D arrays matching the axes
# axis 0: freq (x-axis in your case), axis 1: power (slow scan direction)

def detect_peak_freqs_via_kde(data, freq, power, delta_power=1):
    """
    Returns the two most frequent peak frequencies across power strips.
    """
    peak_freqs = []
    num_strips = len(power) // delta_power

    for i in range(num_strips):
        # Slice and average over delta_power along power axis
        slice_start = i * delta_power
        slice_end = min((i + 1) * delta_power, len(power))

        slice_data = np.mean(data[:, slice_start:slice_end], axis=1)  # average along power

        # # Smooth the slice to reduce noise (optional)
        # from scipy.ndimage import gaussian_filter1d
        # smooth_data = gaussian_filter1d(slice_data, sigma=1)

        # Detect peaks
        peaks, _ = find_peaks(slice_data, prominence=0.05)  # tune threshold if needed
        if len(peaks) == 0:
            continue

        # Choose the largest peak (most prominent feature)
        peak_index = peaks[np.argmax(slice_data[peaks])]
        peak_freqs.append(freq[peak_index])

    # Now estimate the PDF using KDE
    if len(peak_freqs) < 2:
        raise ValueError("Not enough peaks detected to perform KDE.")

    kde = gaussian_kde(peak_freqs)
    xs = np.linspace(min(freq), max(freq), 1000)
    density = kde(xs)

    # Find peaks in KDE
    kde_peaks, _ = find_peaks(density)
    peak_freqs_estimated = xs[kde_peaks]
    top_two = peak_freqs_estimated[np.argsort(density[kde_peaks])][-2:]

    # Ensure x1 > x2
    x1, x2 = sorted(top_two, reverse=True)

    return x1, x2, peak_freqs, xs, density


x1, x2, peak_freqs, xs, density = detect_peak_freqs_via_kde(data.max() - data, freq, power)

plt.figure(figsize=(8, 4))
plt.hist(peak_freqs, bins=50, alpha=0.3, label="Peak freq histogram")
plt.plot(xs, density * len(peak_freqs), label="KDE", color='red')
plt.axvline(x1, color='green', linestyle='--', label=f'x1 = {x1:.3f}')
plt.axvline(x2, color='blue', linestyle='--', label=f'x2 = {x2:.3f}')
plt.xlabel("Frequency")
plt.ylabel("Count / Density")
plt.legend()
plt.title("Peak frequency distribution across power slices")
plt.tight_layout()
plt.show()


# %%
import numpy as np
from scipy.stats import gaussian_kde
from itertools import groupby
from operator import itemgetter

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

        x1, peak_freqs, region, pick_idx = detect_peak_regions_with_kde(data, freq, power, delta=0.3)


        import matplotlib.pyplot as plt

        # Plot the 2D charge map
        plt.figure(figsize=(8, 6))
        plt.pcolormesh(power, freq, data, shading='auto', cmap='viridis')
        plt.colorbar(label='Signal')

        # Overlay the detected peak positions
        plt.plot(power, peak_freqs, color='red', label='Detected peak')

        # Mark x1-like region with vertical lines
        if region:
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
