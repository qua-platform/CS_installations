# %%
import glob
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# === Functions ===

def prepare_data(ds, qubit='qC1'):
    """Assigns freq_GHz and selects a qubit slice."""
    return ds.assign_coords(freq_GHz=ds.full_freq / 1e9).loc[{'qubit': qubit}]

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

paths = glob.glob("/workspaces/data/QPU_project/2025-05-23/*resonator_spectroscopy_vs_power**/ds_raw.h5")
paths.sort()

for qubit in ["qC1", "qC2"]:
    for path in paths:
        ds = xr.open_dataset(path, engine="netcdf4")
        # Step 1: Prepare dataset
        ds_sliced = prepare_data(ds)
        freq = ds_sliced.freq_GHz
        power = ds_sliced.power
        data = ds_sliced.IQ_abs.values

        # Step 2: Find top 2 frequency peaks
        top_freq_indices, freq_profile = find_two_main_peaks(data)
        peak_freqs = freq[top_freq_indices].values
        print("Top 2 frequency peak indices:", top_freq_indices)
        print("Top 2 frequency values [GHz]:", peak_freqs)
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
        axs[0, 0].set_ylabel("Frequency [GHz]")
        # Horizontal lines at both peak frequencies
        axs[0, 0].hlines(peak_freqs, xmin=power.min(), xmax=power.max(), colors=["g", "m"], linestyles="--")
        # Add star marker at the chosen power + higher frequency
        higher_freq_idx = top_freq_indices[1]  # Assuming top_two are sorted by frequency
        axs[0, 0].plot(power[power_pick_index], freq[higher_freq_idx], marker="*", color="r", markersize=15, label="Chosen Point")
        axs[0, 0].legend()

        # (0, 1): Frequency-averaged data and peaks
        axs[0, 1].plot(freq, data.mean(axis=1), label="Mean over power")
        axs[0, 1].axvline(x=peak_freqs[0], color="g", linestyle="--", label=f"Peak 1: {peak_freqs[0]:.4f} GHz")
        axs[0, 1].axvline(x=peak_freqs[1], color="m", linestyle="--", label=f"Peak 2: {peak_freqs[1]:.4f} GHz")
        axs[0, 1].set_title("Top Frequency Peaks")
        axs[0, 1].set_xlabel("Frequency [GHz]")
        axs[0, 1].legend()

        # (1, 0): Frequency-cut and all-power averages
        axs[1, 0].plot(power, avg_cut, color="m", label=f"Avg (freq={freq[higher_freq_idx]:1.3f} GHz)")
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
        
        plt.pause(0.5)

# %%
