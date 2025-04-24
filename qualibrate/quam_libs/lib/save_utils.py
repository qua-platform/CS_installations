from qualibrate.config.resolvers import get_quam_state_path
from qualibrate.storage.local_storage_manager import LocalStorageManager
from qualibrate_config.resolvers import get_qualibrate_config_path, get_qualibrate_config
from qualibrate_app.config import get_config_path, get_settings
from quam_libs.components import QuAM
import os
from pathlib import Path
import xarray as xr
import json
import numpy as np

def extract_string(input_string):
    # Find the index of the first occurrence of a digit in the input string
    index = next((i for i, c in enumerate(input_string) if c.isdigit()), None)

    if index is not None:
        # Extract the substring from the start of the input string to the index
        extracted_string = input_string[:index]
        return extracted_string
    else:
        return None


def unwrap_structured_array(arr):
    """
    Converts a structured array of shape (N,) with dtype [('value', ..., (1, 30))]
    into a plain 2D ndarray of shape (N, 30).
    """
    return np.stack([entry['value'][0] for entry in arr])

def fetch_results_as_xarray(handles, qubits, measurement_axis):
    """
    Fetches measurement results as an xarray dataset.
    Parameters:
    - handles : A dictionary containing stream handles, obtained through handles = job.result_handles after the execution of the program.
    - qubits (list): A list of qubits.
    - measurement_axis (dict): A dictionary containing measurement axis information, e.g. {"frequency" : freqs, "flux",}.
    Returns:
    - ds (xarray.Dataset): An xarray dataset containing the fetched measurement results.
    """

    stream_handles = handles.keys()
    meas_vars = list(set([extract_string(handle) for handle in stream_handles if extract_string(handle) is not None]))

    values = [
        [handles.get(f"{meas_var}{i + 1}").fetch_all() for i, qubit in enumerate(qubits)] for meas_var in meas_vars
    ]

    if np.array(values).shape[-1] == 1:
        values = np.array(values).squeeze(axis=-1)
    measurement_axis["qubit"] = [qubit.name for qubit in qubits]
    measurement_axis = {key: measurement_axis[key] for key in reversed(measurement_axis.keys())}
    
    
    ds = xr.Dataset(
        {f"{meas_var}": ([key for key in measurement_axis.keys()], values[i]) for i, meas_var in enumerate(meas_vars)},
        coords=measurement_axis,
    )

    return ds


def fetch_results_as_xarray_for_1_pulse_heralding(handles, qubits, measurement_axis, threshold=0.5, mask_axis=1):
    """
    Fetches measurement results as an xarray dataset.
    Parameters:
    - handles : A dictionary containing stream handles, obtained through handles = job.result_handles after the execution of the program.
    - qubits (list): A list of qubits.
    - measurement_axis (dict): A dictionary containing measurement axis information, e.g. {"frequency" : freqs, "flux",}.
    Returns:
    - ds (xarray.Dataset): An xarray dataset containing the fetched measurement results.
    """

    stream_handles = handles.keys()
    meas_vars = list(set([extract_string(handle) for handle in stream_handles if extract_string(handle) is not None]))

    values = [
        [handles.get(f"{meas_var}{i + 1}").fetch_all() for i, qubit in enumerate(qubits)] for meas_var in meas_vars
    ]
    # Define threshold
    threshold = 0.5

    # Processed output
    processed = []
    valid_masks = []
    for row_group in values:
        processed_row = []
        for row_arr in row_group:
            raw = row_arr['value']

            # Apply threshold rule: keep value if previous value > threshold, else NaN
            result = np.empty_like(raw, dtype=float)
            for i, row in enumerate(raw):
                new_row = [np.nan]  # First value always NaN
                for j in range(1, len(row)):
                    new_row.append(row[j] if row[j - 1] < threshold else np.nan)
                result[i] = np.array(new_row)

            # find the columns that contain only NaN
            # only_nan_mask = np.all(np.isnan(result), axis=0)
            # valid_mask = ~only_nan_mask
            #
            # # Delete all the columns that contain only NaN results
            # result_valid = result[:, valid_mask]
            # Average over columns, ignoring NaN
            result_avg = np.nanmean(result, axis=0)

            processed_row.append(np.array(result_avg))
            # valid_masks.append(valid_mask)
        # Wrap the entire processed row
        processed.append(processed_row)

    # find the most number of Nans
    # nan_counts = [np.isnan(arr).sum() for arr in processed[0]]
    # # Find index of array with the most NaNs
    # max_nan_index = np.argmax(nan_counts)
    # # crate the Nan mask
    # nan_mask = np.isnan(processed[0][max_nan_index])
    nan_mask = np.any(np.isnan(processed[0]), axis=0)
    valid_mask = ~nan_mask
    # # to make the lengths of the vactor the same, we take the results with the most amount of columns with all Nans
    # false_counts = [np.sum(~arr) for arr in valid_masks]
    # max_false_index = np.argmax(false_counts)
    # Nan_mask = valid_masks[max_false_index]
    #
    # diff_mask = (~valid_masks[max_false_index])& (valid_masks[1-max_false_index])
    #
    # # apply the mask on the processed data
    # for i in range(len(qubits)):
    #     if len(processed[0][i]) != len(Nan_mask):
    processed_masked = [
        [arr[valid_mask] for arr in row_group]
        for row_group in processed
    ]
    if np.array(processed_masked).shape[-1] == 1:
        processed_masked = np.array(processed_masked).squeeze(axis=-1)
    measurement_axis["qubit"] = [qubit.name for qubit in qubits]
    measurement_axis = {key: measurement_axis[key] for key in reversed(measurement_axis.keys())}
    measurement_axis_valid = {key: value if key=="qubit" else value[valid_mask] for key, value in measurement_axis.items()}

    ds = xr.Dataset(
        {f"{meas_var}": ([key for key in measurement_axis_valid.keys()], processed_masked[i]) for i, meas_var in enumerate(meas_vars)},
        coords=measurement_axis_valid,
    )

    return ds, valid_mask

def fetch_results_as_xarray_for_2_pulse_heralding(handles, qubits, measurement_axis, threshold=0.5, mask_axis=1):
    """
    Fetches measurement results as an xarray dataset.
    Parameters:
    - handles : A dictionary containing stream handles, obtained through handles = job.result_handles after the execution of the program.
    - qubits (list): A list of qubits.
    - measurement_axis (dict): A dictionary containing measurement axis information, e.g. {"frequency" : freqs, "flux",}.
    Returns:
    - ds (xarray.Dataset): An xarray dataset containing the fetched measurement results.
    """

    stream_handles = handles.keys()
    meas_vars = list(set([extract_string(handle) for handle in stream_handles if extract_string(handle) is not None]))

    values = [
        [handles.get(f"{meas_var}{i + 1}").fetch_all() for i, qubit in enumerate(qubits)] for meas_var in meas_vars
    ]
    # Define threshold
    threshold = 0.5

    # Processed output
    processed = []
    valid_masks = []
    for row_group in values:
        processed_row = []
        for row_arr in row_group:
            raw = row_arr['value']

            # Apply threshold rule: keep value if previous value > threshold, else NaN
            result = np.empty((raw.shape[0], raw.shape[1] - 1), dtype=float)
            for i, row in enumerate(raw):
                new_row = []
                for j in range(0, len(row)):
                    new_row.append(row[j][1] if row[j][0] < threshold else np.nan)
                result[i] = np.array(new_row)

            # find the columns that contain only NaN
            # only_nan_mask = np.all(np.isnan(result), axis=0)
            # valid_mask = ~only_nan_mask
            #
            # # Delete all the columns that contain only NaN results
            # result_valid = result[:, valid_mask]
            # Average over columns, ignoring NaN
            result_avg = np.nanmean(result, axis=0)

            processed_row.append(np.array(result_avg))
            # valid_masks.append(valid_mask)
        # Wrap the entire processed row
        processed.append(processed_row)

    # find the most number of Nans
    # nan_counts = [np.isnan(arr).sum() for arr in processed[0]]
    # # Find index of array with the most NaNs
    # max_nan_index = np.argmax(nan_counts)
    # # crate the Nan mask
    # nan_mask = np.isnan(processed[0][max_nan_index])
    nan_mask = np.any(np.isnan(processed[0]), axis=0)
    valid_mask = ~nan_mask
    # # to make the lengths of the vactor the same, we take the results with the most amount of columns with all Nans
    # false_counts = [np.sum(~arr) for arr in valid_masks]
    # max_false_index = np.argmax(false_counts)
    # Nan_mask = valid_masks[max_false_index]
    #
    # diff_mask = (~valid_masks[max_false_index])& (valid_masks[1-max_false_index])
    #
    # # apply the mask on the processed data
    # for i in range(len(qubits)):
    #     if len(processed[0][i]) != len(Nan_mask):
    processed_masked = [
        [arr[valid_mask] for arr in row_group]
        for row_group in processed
    ]
    if np.array(processed_masked).shape[-1] == 1:
        processed_masked = np.array(processed_masked).squeeze(axis=-1)
    measurement_axis["qubit"] = [qubit.name for qubit in qubits]
    measurement_axis = {key: measurement_axis[key] for key in reversed(measurement_axis.keys())}
    measurement_axis_valid = {key: value if key=="qubit" else value[valid_mask] for key, value in measurement_axis.items()}

    ds = xr.Dataset(
        {f"{meas_var}": ([key for key in measurement_axis_valid.keys()], processed_masked[i]) for i, meas_var in enumerate(meas_vars)},
        coords=measurement_axis_valid,
    )

    return ds, valid_mask

# def fetch_results_as_xarray_for_heralding(handles, qubits, measurement_axis):
#     """
#     Fetches measurement results as an xarray dataset.
#     Parameters:
#     - handles : A dictionary containing stream handles, obtained through handles = job.result_handles after the execution of the program.
#     - qubits (list): A list of qubits.
#     - measurement_axis (dict): A dictionary containing measurement axis information, e.g. {"frequency" : freqs, "flux",}.
#     Returns:
#     - ds (xarray.Dataset): An xarray dataset containing the fetched measurement results.
#     """
#
#     stream_handles = handles.keys()
#     meas_vars = list(set([extract_string(handle) for handle in stream_handles if extract_string(handle) is not None]))
#     values = [
#         [handles.get(f"{meas_var}{i + 1}").fetch_all() for i, qubit in enumerate(qubits)] for meas_var in meas_vars
#     ]
#
#     threshold = 0.5  # or any other threshold you'd like
#     post_selected_avg = []
#
#     for qidx in range(len(values[0])):  # loop over qubits
#         amp_data = values[0][qidx]  # shape: (10,), each item has ('value', (2, 4))
#
#         # Extract raw data into shape (10, 2, 4)
#         raw = np.stack([entry[0] for entry in amp_data])  # (10, 2, 4)
#         raw = raw.astype(float)  # so we can assign NaN
#
#         # Initialize selection with NaN
#         selected = np.full_like(raw, np.nan)
#
#         # Always keep the first shot (or you can use other logic)
#         selected[0] = raw[0]
#
#         # Apply threshold condition: if previous shot passes threshold, keep current
#         for t in range(1, raw.shape[0]):
#             # Let's use channel 0 and time 0 for thresholding; adjust if needed
#             condition = raw[t - 1, 0, 0] > threshold
#             if condition:
#                 selected[t] = raw[t]
#             # else it remains NaN
#
#         # Now average over the 10 shots (axis=0), ignoring NaNs
#         mean_selected = np.nanmean(selected, axis=0)  # shape: (2, 4)
#         post_selected_avg.append(mean_selected)
#
#         new_values = [post_selected_avg]
#     if len(meas_vars) != 1:
#         raise ValueError("Expected exactly one measurement variable (e.g. 'state') for heralded post-selection.")
#
#
#     if np.array(new_values).shape[-1] == 1:
#         new_values = np.array(new_values).squeeze(axis=-1)
#     measurement_axis["qubit"] = [qubit.name for qubit in qubits]
#     measurement_axis = {key: measurement_axis[key] for key in reversed(measurement_axis.keys())}
#
#     # ds = xr.Dataset(
#     #     {meas_var: ([key for key in measurement_axis.keys()], values)},
#     #     coords=measurement_axis,
#     # )
#     ds = xr.Dataset(
#         {f"{meas_var}": ([key for key in measurement_axis.keys()], new_values[i]) for i, meas_var in enumerate(meas_vars)},
#         coords=measurement_axis,
#     )
#
#     return ds


def get_storage_path():
    settings = get_settings(get_config_path())
    storage_location = settings.qualibrate.storage.location
    return Path(storage_location)


def find_numbered_folder(base_path, number):
    """
    Find folder that starts with '#number_'
    Will match '#number_something' but not '#number' alone
    """
    search_prefix = f"#{number}_"
    
    # Manual search for folder starting with #number_ and having something after
    for root, dirs, _ in os.walk(base_path):
        matching_dirs = [d for d in dirs if d.startswith(search_prefix) and len(d) > len(search_prefix)]
        if matching_dirs:
            return os.path.join(root, matching_dirs[0])
    
    return None



def load_dataset(serial_number, target_filename = "ds", parameters = None):
    """
    Loads a dataset from a file based on the serial number.
    
    Args:
        serial_number: The serial number to search for.
        base_folder: The base directory to search in.
    
    Returns:
        An xarray Dataset if found, None otherwise.
    """
    if not isinstance(serial_number, int):
        raise ValueError("serial_number must be an integer")
        
    base_folder = find_numbered_folder(get_storage_path(),serial_number)
    # Look for .nc files in the subfolder
    nc_files = [f for f in os.listdir(base_folder) if f.endswith('.h5')]
    
    # look for filename.h5
    is_present = target_filename in [file.split('.')[0] for file in nc_files]
    filename = [file for file in nc_files if target_filename == file.split('.')[0]][0] if is_present else None
    json_filename = "data.json"
    
    if nc_files:
        # Assuming there's only one .nc file per folder
        file_path = os.path.join(base_folder, filename)
        json_path = os.path.join(base_folder, json_filename)
        # Open the dataset
        ds = xr.open_dataset(file_path)
        with open(json_path, 'r') as f:
            json_data = json.load(f)
        try:
            machine = QuAM.load(base_folder + "//quam_state.json")
        except Exception as e:
            print(f"Error loading machine: {e}")
            machine = None
        qubits = [machine.qubits[qname] for qname in ds.qubit.values]    
        if parameters is not None:
            for param_name, param_value in parameters:
                if param_name != "load_data_id":
                    if param_name in json_data["initial_parameters"]:
                        setattr(parameters, param_name, json_data["initial_parameters"][param_name])
            return ds, machine, json_data, qubits,parameters
        else:
            return ds, machine, json_data, qubits
    else:
        print(f"No .nc file found in folder: {base_folder}")
        return None

def get_node_id() -> int:
    
    q_config_path = get_qualibrate_config_path()
    qs = get_qualibrate_config(q_config_path)
    state_path = get_quam_state_path(qs)
    storage_manager = LocalStorageManager(
                root_data_folder=qs.storage.location,
                active_machine_path=state_path,
            )
    
    return storage_manager.data_handler.generate_node_contents()['id']