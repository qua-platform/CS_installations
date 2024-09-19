
import os
import xarray as xr
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


 # %% Utils

def gaussian(x, a1, b1, c1):
    """
    Calculates the value of a Gaussian function at point x.
    
    Args:
        x: The input value.
        a1: The amplitude of the Gaussian.
        b1: The mean (center) of the Gaussian.
        c1: The standard deviation of the Gaussian.
    
    Returns:
        The value of the Gaussian function at x.
    """
    return a1 * np.exp(-(x - b1)**2 / (2 * c1**2))

def two_gaussian(x, a1, b1, c1, a2, b2, c2):
    """
    Calculates the sum of two Gaussian functions at point x.
    
    Args:
        x: The input value.
        a1, b1, c1: Parameters for the first Gaussian.
        a2, b2, c2: Parameters for the second Gaussian.
    
    Returns:
        The sum of two Gaussian functions at x.
    """
    return a1 * np.exp(-(x - b1)**2 / (2 * c1**2)) + a2 * np.exp(-(x - b2)**2 / (2 * c2**2))

def to_bins(data, bins):
    """
    Converts data into histogram bins.
    
    Args:
        data: The input data to be binned.
        bins: The number of bins or bin edges.
    
    Returns:
        A tuple of (counts, bin_centers).
    """
    counts, I_bin = np.histogram(data, bins=bins)
    I_bin = (I_bin[:-1] + I_bin[1:])/2
    return counts, I_bin


def find_intersection(a1, b1, c1, a2, b2, c2):
    """
    Finds the intersection point of two Gaussian functions.
    
    Args:
        a1, b1, c1: Parameters for the first Gaussian.
        a2, b2, c2: Parameters for the second Gaussian.
    
    Returns:
        The x-coordinate of the intersection point.
    """
    if b2 > b1:
        x = np.linspace(b1-np.abs(c1),b2+np.abs(c2),10000)
    else:
        x = np.linspace(b2-np.abs(c2),b1+np.abs(c1),10000)
    y1 = gaussian(x, a1, b1, c1)
    y2 = gaussian(x, a2, b2, c2)
    return x[np.argmin(np.abs(y1-y2))]

def load_dataset(serial_number, base_folder=r'C:\Users\tomdv\OneDrive - QM Machines LTD\Documents\other\adaptive_threshold\2024-08-14'):
    """
    Loads a dataset from a file based on the serial number.
    
    Args:
        serial_number: The serial number to search for.
        base_folder: The base directory to search in.
    
    Returns:
        An xarray Dataset if found, None otherwise.
    """
    # Find the subfolder with the matching serial number
    for subfolder in os.listdir(base_folder):
        if serial_number in subfolder:
            folder_path = os.path.join(base_folder, subfolder)
            
            # Look for .nc files in the subfolder
            nc_files = [f for f in os.listdir(folder_path) if f.endswith('.h5')]
            
            if nc_files:
                # Assuming there's only one .nc file per folder
                file_path = os.path.join(folder_path, nc_files[0])
                
                # Open the dataset
                ds = xr.open_dataset(file_path)
                return ds
            else:
                print(f"No .nc file found in folder: {folder_path}")
                return None
    
    print(f"No folder found for serial number: {serial_number}")
    return None



# %%

def find_threshold_with_error(data_array, bins=400, init_guess = None):
    """
    Finds the threshold for a bimodal distribution and calculates associated errors.
    
    Args:
        data_array: Input data to be analyzed.
        bins: Number of bins for the histogram.
    
    Returns:
        Tuple containing optimized parameters, errors, intersection point,
        infidelity, infidelity error, and a dataset with fitted curves.
    """
    def fit_gauss_left(x_data, y_data):
        
        center_of_mass = np.sum(x_data * y_data) / np.sum(y_data)
        center_of_mass_index = np.argmin(np.abs(x_data - center_of_mass))
        y_data_for_fit = y_data[:center_of_mass_index]
        x_data_for_fit = x_data[:center_of_mass_index]
        popt, pcov = curve_fit(gaussian, x_data_for_fit, y_data_for_fit, p0=[y_data_for_fit.max(), x_data_for_fit[np.argmax(y_data_for_fit)], 0.0001])
        return popt, pcov

    # print(data_array)
    counts, I_bin = to_bins(data_array.values.flatten(), bins=bins)

    x_data = I_bin
    y_data = counts
    

    
    # Fit both gaussians simultaneously
    if init_guess is None:
        popt_left, pcov_left = fit_gauss_left(x_data, y_data)
        # print(popt_left)
        center = popt_left[1]
        center_index = np.argmax(x_data > center)
        right_index = np.argwhere((y_data > 2 * gaussian(x_data, *popt_left))[center_index:])[0][0] + center_index 
        right_point = x_data[right_index]
        
        # Fit the remainder of the data to a second gaussian
        y_data2 = y_data - gaussian(x_data, *popt_left)
        
        y_data_for_fit2 = y_data2 * (x_data > right_point)
        popt_right, pcov_right = curve_fit(gaussian, x_data, y_data_for_fit2, p0=[y_data_for_fit2.max(), x_data[np.argmax(y_data_for_fit2)], 0.0001])
        initial_guess = [*popt_left, *popt_right]
    else:
        initial_guess = init_guess
    
    popt_final, pcov_final = curve_fit(two_gaussian, x_data, y_data, p0=initial_guess)
    # popt_final = initial_guess
    # Calculate the intersection point
    intersection = find_intersection(*popt_final)
    
    # Calculate errors
    perr_final = np.sqrt(np.diag(pcov_final))
    
    # Calculate infidelity and its error
    infidelity = popt_final[3] / (popt_final[0] + popt_final[3])
    infidelity_error = infidelity * np.sqrt((perr_final[3]/popt_final[3])**2 + 
                                            ((perr_final[0]**2 + perr_final[3]**2) / 
                                             (popt_final[0] + popt_final[3])**2))
    
    # Create a dataset with fitted values
    x_fit = np.linspace(x_data.min(), x_data.max(), 1000)
    y_fit_total = two_gaussian(x_fit, *popt_final)
    y_fit_gauss1 = gaussian(x_fit, *popt_final[:3])
    y_fit_gauss2 = gaussian(x_fit, *popt_final[3:])
    
    fit_dataset = xr.Dataset({
        'x': ('x', x_fit),
        'y_total': ('x', y_fit_total),
        'y_gauss1': ('x', y_fit_gauss1),
        'y_gauss2': ('x', y_fit_gauss2)
    })
    
    return popt_final, perr_final, intersection, infidelity, infidelity_error, fit_dataset

def find_threshold_with_error_and_guess_fixed(data_array, initial_guess, bins=400):
    """
    Finds the threshold for a bimodal distribution using an initial guess with fixed separation.
    
    Args:
        data_array: Input data to be analyzed.
        initial_guess: Initial parameter estimates for the two Gaussians.
        bins: Number of bins for the histogram.
    
    Returns:
        Tuple containing optimized parameters, errors, intersection point,
        infidelity, infidelity error, and a dataset with fitted curves.
    """
    counts, I_bin = to_bins(data_array.values.flatten(), bins=bins)

    x_data = I_bin
    y_data = counts
    
    # Use the provided initial guess, but fit amplitudes, widths, and the location of the first Gaussian
    initial_guess_reduced = [initial_guess[0], initial_guess[1], initial_guess[2], initial_guess[3], initial_guess[5]]
    
    # Define a wrapper function for curve_fit that uses the fixed separation
    def two_gaussian_fixed_separation(x, a1, b1, c1, a2, c2):
        separation = initial_guess[4] - initial_guess[1]
        return two_gaussian(x, a1, b1, c1, a2, b1 + separation, c2)
    
    popt_reduced, pcov_reduced = curve_fit(two_gaussian_fixed_separation, x_data, y_data, p0=initial_guess_reduced)
    
    # Reconstruct full parameter set
    separation = initial_guess[4] - initial_guess[1]
    popt_final = [popt_reduced[0], popt_reduced[1], popt_reduced[2], 
                  popt_reduced[3], popt_reduced[1] + separation, popt_reduced[4]]
    
    # Calculate the intersection point
    intersection = find_intersection(*popt_final)
    
    # Calculate errors (note: error for b2 will be the same as b1)
    perr_reduced = np.sqrt(np.diag(pcov_reduced))
    perr_final = [perr_reduced[0], perr_reduced[1], perr_reduced[2], 
                  perr_reduced[3], perr_reduced[1], perr_reduced[4]]
    
    # Calculate infidelity and its error
    infidelity = popt_final[3] / (popt_final[0] + popt_final[3])
    infidelity_error = infidelity * np.sqrt((perr_final[3]/popt_final[3])**2 + 
                                            ((perr_final[0]**2 + perr_final[3]**2) / 
                                             (popt_final[0] + popt_final[3])**2))
    
    # Create a dataset with fitted values
    x_fit = np.linspace(x_data.min(), x_data.max(), 1000)
    y_fit_total = two_gaussian(x_fit, *popt_final)
    y_fit_gauss1 = gaussian(x_fit, popt_final[0], popt_final[1], popt_final[2])
    y_fit_gauss2 = gaussian(x_fit, popt_final[3], popt_final[4], popt_final[5])
    
    fit_dataset = xr.Dataset({
        'x': ('x', x_fit),
        'y_total': ('x', y_fit_total),
        'y_gauss1': ('x', y_fit_gauss1),
        'y_gauss2': ('x', y_fit_gauss2)
    })
    
    return popt_final, perr_final, intersection, infidelity, infidelity_error, fit_dataset

def find_threshold_with_error_and_guess_free(data_array, initial_guess, bins=400):
    """
    Finds the threshold for a bimodal distribution using an initial guess with all parameters free to vary.
    
    Args:
        data_array: Input data to be analyzed.
        initial_guess: Initial parameter estimates for the two Gaussians.
        bins: Number of bins for the histogram.
    
    Returns:
        Tuple containing optimized parameters, errors, intersection point,
        infidelity, infidelity error, and a dataset with fitted curves.
    """
    counts, I_bin = to_bins(data_array.values.flatten(), bins=bins)

    x_data = I_bin
    y_data = counts
    
    # Use the provided initial guess, but allow all parameters to vary
    popt_final, pcov_final = curve_fit(two_gaussian, x_data, y_data, p0=initial_guess)
    
    # Calculate the intersection point
    intersection = find_intersection(*popt_final)
    
    # Calculate errors
    perr_final = np.sqrt(np.diag(pcov_final))
    
    # Calculate infidelity and its error
    infidelity = popt_final[3] / (popt_final[0] + popt_final[3])
    infidelity_error = infidelity * np.sqrt((perr_final[3]/popt_final[3])**2 + 
                                            ((perr_final[0]**2 + perr_final[3]**2) / 
                                             (popt_final[0] + popt_final[3])**2))
    
    # Create a dataset with fitted values
    x_fit = np.linspace(x_data.min(), x_data.max(), 1000)
    y_fit_total = two_gaussian(x_fit, *popt_final)
    y_fit_gauss1 = gaussian(x_fit, popt_final[0], popt_final[1], popt_final[2])
    y_fit_gauss2 = gaussian(x_fit, popt_final[3], popt_final[4], popt_final[5])
    
    fit_dataset = xr.Dataset({
        'x': ('x', x_fit),
        'y_total': ('x', y_fit_total),
        'y_gauss1': ('x', y_fit_gauss1),
        'y_gauss2': ('x', y_fit_gauss2)
    })
    
    return popt_final, perr_final, intersection, infidelity, infidelity_error, fit_dataset

def plot_threshold_analysis(ds, popt_final, perr_final, intersection, infidelity, infidelity_error, fit_dataset, logplot = True, figsize=(10, 6), lables = True):
    """
    Plots the threshold analysis results.
    
    Args:
        ds: The original dataset.
        popt_final: Optimized parameters for the two Gaussians.
        perr_final: Errors on the optimized parameters.
        intersection: The intersection point of the two Gaussians.
        infidelity: The calculated infidelity.
        infidelity_error: The error on the infidelity.
        fit_dataset: Dataset containing the fitted curves.
    """
    # Plot the data and fitted Gaussians
    f,ax = plt.subplots(figsize=figsize)
    if lables:
        if logplot:
            ax.semilogy(fit_dataset.x * 1000, fit_dataset.y_total, label='Total Fit', color='red')
            ax.semilogy(fit_dataset.x * 1000, fit_dataset.y_gauss1, label='Gaussian 1', color='green', linestyle='--')
            ax.semilogy(fit_dataset.x * 1000, fit_dataset.y_gauss2, label='Gaussian 2', color='blue', linestyle='--')
        else:
            ax.plot(fit_dataset.x * 1000, fit_dataset.y_total, label='Total Fit', color='red')
            ax.plot(fit_dataset.x * 1000, fit_dataset.y_gauss1, label='Gaussian 1', color='green', linestyle='--')
            ax.plot(fit_dataset.x * 1000, fit_dataset.y_gauss2, label='Gaussian 2', color='blue', linestyle='--')
    else:
        if logplot:
            ax.semilogy(fit_dataset.x * 1000, fit_dataset.y_total, color='red')
            ax.semilogy(fit_dataset.x * 1000, fit_dataset.y_gauss1, color='green', linestyle='--')
            ax.semilogy(fit_dataset.x * 1000, fit_dataset.y_gauss2, color='blue', linestyle='--')
        else:
            ax.plot(fit_dataset.x * 1000, fit_dataset.y_total, color='red')
            ax.plot(fit_dataset.x * 1000, fit_dataset.y_gauss1, color='green', linestyle='--')
            ax.plot(fit_dataset.x * 1000, fit_dataset.y_gauss2, color='blue', linestyle='--')        
    # Plot the original data
    counts, bins = np.histogram(ds.I.values[0], bins=400)
    bin_centers = (bins[:-1] + bins[1:]) / 2
    if lables:
        if logplot:
            ax.semilogy(bin_centers * 1000, counts, 'o', label='Data', alpha=0.5, markersize=3)
        else:
            ax.plot(bin_centers * 1000, counts, 'o', label='Data', alpha=0.5, markersize=3)
        ax.axvline(intersection * 1000, color='k', linestyle=':', label='Intersection')
    else:
        if logplot:
            ax.semilogy(bin_centers * 1000, counts, 'o', alpha=0.5, markersize=3)
        else:
            ax.plot(bin_centers * 1000, counts, 'o', alpha=0.5, markersize=3)
        ax.axvline(intersection * 1000, color='k', linestyle=':')
    ax.set_xlabel('I (mV)')
    ax.set_ylabel('Counts')
    ax.set_title('State Histogram with Fitted Gaussians')
    ax.legend()
    ax.set_ylim(1, np.max(counts) * 1.2)

    # Print results
    print(f"Intersection point: {intersection * 1000:.4f} mV")
    print(f"Infidelity: {infidelity:.4f} ± {infidelity_error:.4f}")
    print(f"Fidelity: {1-infidelity:.4f} ± {infidelity_error:.4f}")

    return f
