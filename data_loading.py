import os
import glob
import json
import numpy as np
import math
import matplotlib.pyplot as plt

def retrieve_data(file_number, date):
    saved_data_path = os.path.join(date, f'#*{file_number}_*')
    matching_directories = glob.glob(saved_data_path)
    print(matching_directories)

    if not matching_directories:
        print(f"No directory found matching the pattern '{saved_data_path}'.")
        return None
    else:
        # Filter the matching directories based on the exact file_number
        desired_directory = None
        for directory in matching_directories:
            if f'#{file_number}_' in directory:
                desired_directory = directory
                break

        if desired_directory is None:
            print(f"No directory found with the exact file number '#{file_number}'.")
            return None

        try:
            # Load the data from data.json
            json_file_path = os.path.join(desired_directory, 'data.json')
            with open(json_file_path, 'r') as file:
                data_paths = json.load(file)

            # Load the arrays from the npz file
            npz_file_path = os.path.join(desired_directory, 'arrays.npz')
            npz_data = np.load(npz_file_path)

            # Access the arrays selectively based on the keys in data.json
            arrays = {}
            for key, value in data_paths.items():
                if isinstance(value, str) and value.startswith('./arrays.npz#'):
                    array_key = value.split('#')[1]
                    arrays[key] = npz_data[array_key]
                    print("the shape of", key, "is", arrays[key].shape)
                else:
                    arrays[key] = value
                    print("the value of", key, "is", arrays[key])

            return arrays

        except FileNotFoundError as e:
            print(f"Error: {e}")
        except KeyError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    return None

FILE_NUMBER = 10
DATE = "2024-05-13"

arrays = retrieve_data(FILE_NUMBER, DATE)

arrays.keys()