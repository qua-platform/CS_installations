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


def detect_peak_regions_with_kde(data, freq, power, delta_power_idx=2):
    num_power = len(power)
    peak_freqs = []
    peak_freqs_idx = []

    # # Now estimate the PDF using KDE
    # if len(peak_freqs) < 2:
    #     raise ValueError("Not enough peaks detected to perform KDE.")

    # kde = gaussian_kde(peak_freqs)
    # xs = np.linspace(min(freq), max(freq), 1000)
    # density = kde(xs)

    # # Find peaks in KDE
    # kde_peaks, _ = find_peaks(density)
    # peak_freqs_estimated = xs[kde_peaks]
    # top_two = peak_freqs_estimated[np.argsort(density[kde_peaks])][-2:]

    # # Ensure x1 > x2
    # x1, x2 = sorted(top_two, reverse=True)

    # return x1, x2, peak_freqs, xs, density

    for i in range(num_power):
        i1 = i - delta_power_idx if (i - delta_power_idx) > 0 else 0
        i2 = i + delta_power_idx if (i + delta_power_idx) < num_power else num_power
        data_sliced = data[:, i1:i2].mean(axis=1)
        # print(i, i1, i2)
        # Detect peaks
        peaks, _ = find_peaks(data_sliced, prominence=0.05)  # tune threshold if needed
        if len(peaks) == 0:
            continue

        # Choose the largest peak (most prominent feature)
        peak_idx = peaks[np.argmax(data_sliced[peaks])]
        peak_freqs.append(freq[peak_idx])
        peak_freqs_idx.append(peak_idx)
        # print(i, peak_idx)
        
        # plt.plot(freq, data_sliced)
        # plt.axvline(x=freq[peak_idx], ymin=0, ymax=1, color="r")
        # plt.show()
        # plt.pause(0.5)

    return peak_freqs, peak_freqs_idx

def apply_kde(peak_freqs, freq):

    kde = gaussian_kde(peak_freqs, bw_method=0.3)
    xs = np.linspace(min(freq), max(freq), 1000)
    density = kde(xs)

    # Find peaks in KDE
    kde_peaks, _ = find_peaks(density)
    peak_freqs_estimated = xs[kde_peaks]
    peak_freqs_estimated = peak_freqs_estimated[np.argsort(density[kde_peaks])]
    
    if len(peak_freqs_estimated) < 2:
        top_two = np.insert(peak_freqs_estimated, 0, 0)
    else:
        top_two = peak_freqs_estimated[-2:]

    # Ensure x1 > x2
    f1, f2 = sorted(top_two, reverse=True)

    plt.figure(figsize=(8, 4))
    plt.hist(peak_freqs, bins=50, alpha=0.3, label="Peak freq histogram")
    plt.plot(xs, density * len(peak_freqs), label="KDE", color='red')
    plt.axvline(f1, color='green', linestyle='--', label=f'f1 = {f1:.3f}')
    plt.axvline(f2, color='blue', linestyle='--', label=f'f2 = {f2:.3f}')
    plt.xlabel("Frequency")
    plt.ylabel("Count / Density")
    plt.legend()
    plt.title("Peak frequency distribution across power slices")
    plt.tight_layout()
    plt.show()
    
    return f1, f2, density

    # peak_freqs = np.array(peak_freqs)

    # # Automatically find the two most common peaks via histogram if f1 not given
    # if x1 is None:
    #     hist, bin_edges = np.histogram(peak_freqs[~np.isnan(peak_freqs)], bins=100)
    #     bin_centers = 0.5 * (bin_edges[1:] + bin_edges[:-1])
    #     sorted_peaks = bin_centers[np.argsort(hist)[::-1]]
    #     x1 = sorted_peaks[0]  # most common peak

    # # Find region where peak_freq is close to x1
    # mask = np.abs(peak_freqs - x1) < delta
    # idx_true = np.where(mask)[0]

    # groups = []
    # for k, g in groupby(enumerate(idx_true), lambda i_x: i_x[0] - i_x[1]):
    #     group = list(map(itemgetter(1), g))
    #     groups.append(group)

    # if not groups:
    #     return x1, peak_freqs, None

    # largest_region = max(groups, key=len)
    # start_idx = largest_region[0]
    # end_idx = largest_region[-1]
    # pick_idx = int(0.8 * end_idx + 0.2 * start_idx)

    # return x1, peak_freqs, (power[start_idx], power[end_idx]), pick_idx

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
        
        peak_freqs, peak_freqs_idx = detect_peak_regions_with_kde(data, freq, power, delta_power_idx=2)
        f1, f2, density = apply_kde(peak_freqs, freq)
        # x1, peak_freqs, region, pick_idx = detect_peak_regions_with_kde(data, freq, power, delta=0.1)


        import matplotlib.pyplot as plt

        # Plot the 2D charge map
        plt.figure(figsize=(8, 6))
        plt.pcolormesh(power, freq, data, shading='auto', cmap='viridis')
        plt.colorbar(label='Signal')

        # Overlay the detected peak positions
        plt.plot(power, peak_freqs, color='red', label='Detected peak')

        # Mark x1-like region with vertical lines
        plt.axhline(y=f1, color='m', linestyle='--', label='dispersive regime')
        #     plt.axvline(region[0], color='orange', linestyle='--', label='x1-like region start')
        #     plt.axvline(region[1], color='orange', linestyle='--', label='x1-like region end')
        #     plt.plot(power[pick_idx], x1, marker="*", color="r", markersize=15, label="Chosen Point")
            
        plt.xlabel('Power (arb. units)')
        plt.ylabel('Frequency (arb. units)')
        plt.title('Peak Drift & x1 Region Detection')
        plt.legend()
        plt.tight_layout()
        plt.show()

        print("=" * 100)
        print("=" * 100)

# %%
