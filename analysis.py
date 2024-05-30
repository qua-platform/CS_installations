import matplotlib.pyplot as plt
import numpy as np
import json
import os
import glob
from scipy.optimize import curve_fit
from datetime import datetime

def retrieve_data(file_number, date):
    saved_data_path = os.path.join(date, f'#*{file_number}_*')
    matching_directories = glob.glob(saved_data_path)

    if not matching_directories:
        return None, None
    else:
        desired_directory = None
        for directory in matching_directories:
            if f'#{file_number}_' in directory:
                desired_directory = directory
                break

        if desired_directory is None:
            return None, None

        try:
            json_file_path = os.path.join(desired_directory, 'data.json')
            with open(json_file_path, 'r') as file:
                data_paths = json.load(file)

            npz_file_path = os.path.join(desired_directory, 'arrays.npz')
            npz_data = np.load(npz_file_path)

            arrays = {}
            for key, value in data_paths.items():
                if isinstance(value, str) and value.startswith('./arrays.npz#'):
                    array_key = value.split('#')[1]
                    arrays[key] = npz_data[array_key]
                else:
                    arrays[key] = value

            return arrays, desired_directory

        except FileNotFoundError as e:
            print(f"Error: {e}")
        except KeyError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    return None, None

def exponential_decay(x, A, tau, C):
    return A * np.exp(-x / tau) + C

def initial_guesses(I_data, x_data):
    A = np.max(I_data)
    C = np.min(I_data)
    tau = x_data[np.argmax(I_data <= A / np.exp(1))]
    return [A, tau, C]

def moving_average_with_std(data, window_size):
    half_window = window_size // 2
    moving_avg = np.convolve(data, np.ones(window_size) / window_size, mode='valid')
    moving_std = [np.std(data[max(0, i - half_window):min(len(data), i + half_window + 1)]) for i in range(len(data))]
    moving_avg = np.pad(moving_avg, (half_window, half_window), mode='edge')
    moving_std = np.pad(moving_std, (half_window, half_window), mode='edge')
    return moving_avg[:len(data)], moving_std[:len(data)]

# Define the date and file numbers
date_file_ranges = {
    "2024-05-29": range(118, 601),
    "2024-05-30": range(601, 900)
}

time_constants = []
file_times = []

# Flag for debug plotting
debug_plotting = False

# Iterate over the dates and file numbers
for date, file_numbers in date_file_ranges.items():
    for file_number in file_numbers:
        arrays, directory = retrieve_data(file_number, date)
        if arrays is not None and 'I' in arrays:
            I_data = arrays['I']
            
            x_data = np.geomspace(16, 800_000, 50)  # x_data in nanoseconds
            
            # Calculate initial guesses
            initial_guesses_values = initial_guesses(I_data, x_data)
            
            # Perform the fitting
            try:
                params, _ = curve_fit(exponential_decay, x_data, I_data, p0=initial_guesses_values)
                
                # Extract the parameters
                A, tau, C = params
                time_constants.append(tau)
                
                # Extract the file time from the directory name
                file_time_str = os.path.basename(directory).split('_')[-1]
                file_time = datetime.strptime(file_time_str, '%H%M%S')
                file_times.append(file_time.strftime('%H:%M:%S'))
                
                # Plot the data and the fit if debug plotting is enabled
                if debug_plotting:
                    plt.figure()
                    plt.plot(x_data, I_data, 'bo', label='Data')
                    plt.plot(x_data, exponential_decay(x_data, A, tau, C), 'r-', label=f'Fit: A={A:.2f}, tau={tau:.2f}, C={C:.2f}')
                    plt.xlabel('Time (ns)')
                    plt.ylabel('I')
                    plt.legend()
                    plt.title(f'File Number: {file_number}')
                    plt.show()
            except RuntimeError as e:
                print(f"Error fitting data for file number {file_number}: {e}")

# Specify how often to display x-axis ticks
tick_interval = 10  # Change this value to adjust the interval

# Calculate moving average and standard deviation
window_size = 10  # Change this value to adjust the window size
moving_avg_tau, moving_std_tau = moving_average_with_std(time_constants, window_size)

# Plot the time constants vs the time of each file
plt.figure()
plt.plot(file_times, time_constants, 'bo-', label='Time Constants')
plt.plot(file_times, moving_avg_tau, 'r-', label='Moving Average', alpha=0.5)
plt.fill_between(file_times, moving_avg_tau - moving_std_tau, moving_avg_tau + moving_std_tau, color='red', alpha=0.2)
plt.xlabel('Time (HH:MM:SS)')
plt.ylabel('Time Constant (tau)')
plt.title('Time Constants vs File Time')
plt.xticks(ticks=range(0, len(file_times), tick_interval), labels=[file_times[i] for i in range(0, len(file_times), tick_interval)], rotation=45)
plt.legend()
plt.tight_layout()
plt.show()
