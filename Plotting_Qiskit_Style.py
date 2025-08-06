#%%
from glob import glob
import re
import numpy as np
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def extract_leading_number(path):
    match = re.match(r"(\d+)", path.split("\\")[-1][1:])  
    return int(match.group(0))

def list_up_all_exps(sorted_list):
    print("=============================================")
    print("Experimental List:")
    for i, path_ in enumerate(sorted_list):
        print(f"[Index: {i:>3}] ", path_[3:])

def preview_array(arr, n=5):
    preview = np.array2string(arr[:n], separator=', ', precision=6)
    if arr.shape[0] > n:
        preview = preview.rstrip(']') + ', ...]'
    return preview

def preview_2d(arr, n_rows=5, n_cols=5, precision=6):
    rows, cols = arr.shape
    preview_lines = []
    
    for r in range(min(n_rows, rows)):
        row_data = arr[r, :min(n_cols, cols)]
        row_str = np.array2string(row_data, separator=', ', precision=precision, max_line_width=1e6)
        if cols > n_cols:
            row_str = row_str.rstrip(']') + ', ...]'
        preview_lines.append(row_str)
    
    if rows > n_rows:
        preview_lines.append("...")

    return "\n".join(preview_lines)

def summarize_npz(sorted_list, exp_id):
    name = sorted_list[exp_id][2:]
    exp_res_lst = glob(sorted_list[exp_id] + ".\\*")
    data = [np.load(i_) for i_ in exp_res_lst if "npz" in i_][0]

    print("=============================================")
    print(name)
    print(f"Found {len(data.files)} keys: {data.files}\n")

    for k in data.files:
        arr = data[k]
        print(f"## Key: `{k}`")
        print("- Dimension:", "1D" if arr.ndim == 1 else "2D")
        print(f"- Shape: {arr.shape}")
        print(f"- Dtype: {arr.dtype}")

        if np.issubdtype(arr.dtype, np.number):
            if arr.ndim == 1:
                print(f"- Min: {np.min(arr):.4g}, Max: {np.max(arr):.4g}")
                print(f"- Mean: {np.mean(arr):.4g}, Std: {np.std(arr):.4g}")
                print(f"- First 5 values: {preview_array(arr)}")
            elif arr.ndim == 2:
                print(f"- Axis 0 → Mean: {preview_array(np.mean(arr, axis=0))}")
                print(f"- Axis 1 → Mean: {preview_array(np.mean(arr, axis=1))}")
                print(f"- Preview (0, :5): {preview_2d(arr)}")
            else:
                print(f"- >2D data, shape: {arr.shape} — skipping detailed preview.")
        else:
            print(f"- Non-numeric data. Type: {type(arr)}")
        print()

def plot_res_png(sorted_list, exp_id):
    exp_res_lst = glob(sorted_list[exp_id]+".\\*")
    fig_path = [i_ for i_ in exp_res_lst if "png" in i_][0]
    img = mpimg.imread(fig_path)  
    plt.imshow(img)
    plt.axis('off')  
    plt.title("Original Plotting Style")  
    plt.show()

all_exp_lst = [i for i in glob(".\\*") if "#" in i]
sorted_list = sorted(all_exp_lst, key=extract_leading_number)
list_up_all_exps(sorted_list)

#%%
exp_id = 3
summarize_npz(sorted_list, exp_id)
plot_res_png(sorted_list, exp_id)

# %%
exp_id = 3
exp_res_lst = glob(sorted_list[exp_id] + ".\\*")
npz_path = [i_ for i_ in exp_res_lst if "npz" in i_][0]

#%%
exp_id = 1
exp_res_lst = glob(sorted_list[exp_id] + ".\\*")
npz_path = [i_ for i_ in exp_res_lst if "npz" in i_][0]
from plotting_tools import plot_resonator_spectroscopy
plot_resonator_spectroscopy(npz_path, 5.5)

#%%
exp_id = 5
exp_res_lst = glob(sorted_list[exp_id] + ".\\*")
npz_path = [i_ for i_ in exp_res_lst if "npz" in i_][0]
from plotting_tools import plot_qubit_spectroscopy
plot_qubit_spectroscopy(npz_path)


#%%
exp_id = 8
exp_res_lst = glob(sorted_list[exp_id] + ".\\*")
npz_path = [i_ for i_ in exp_res_lst if "npz" in i_][0]
from plotting_tools import plot_power_rabi
plot_power_rabi(npz_path)

#%%
exp_id = 10
exp_res_lst = glob(sorted_list[exp_id] + ".\\*")
npz_path = [i_ for i_ in exp_res_lst if "npz" in i_][0]
from plotting_tools import plot_t1
plot_t1(npz_path) 

# %% ######## Ramsey Chevron 2D ########
exp_id = 11
exp_res_lst = glob(sorted_list[exp_id] + ".\\*")
npz_path = [i_ for i_ in exp_res_lst if "npz" in i_][0]
from plotting_tools import plot_ramsey
plot_ramsey(npz_path, cut_detuning_idx=6)


# %% ######## Rabi Chevron(amp) 2D ########
exp_id = 7
exp_res_lst = glob(sorted_list[exp_id] + ".\\*")
npz_path = [i_ for i_ in exp_res_lst if "npz" in i_][0]
from plotting_tools import plot_rabi_chevron
plot_rabi_chevron(npz_path, cut_detuning_idx=6)

# %% ######## RB ########
exp_id = 14
exp_res_lst = glob(sorted_list[exp_id] + ".\\*")
npz_path = [i_ for i_ in exp_res_lst if "npz" in i_][0]
from plotting_tools import plot_rb
plot_rb(npz_path, delta_clifford=10)


# %% ######## IQ Blob ########
exp_id = 15
exp_res_lst = glob(sorted_list[exp_id] + ".\\*")
npz_path = [i_ for i_ in exp_res_lst if "npz" in i_][0]
from plotting_tools import plot_iq_blob
plot_iq_blob(npz_path)


# %% ######## Drag ########
exp_id = 17
exp_res_lst = glob(sorted_list[exp_id] + ".\\*")
npz_path = [i_ for i_ in exp_res_lst if "npz" in i_][0]
from plotting_tools import plot_drag
plot_drag(npz_path)


# %% ######## Err Amp ########
exp_id = 9
exp_res_lst = glob(sorted_list[exp_id] + ".\\*")
npz_path = [i_ for i_ in exp_res_lst if "npz" in i_][0]
from plotting_tools import plot_err_amp
plot_err_amp(npz_path)
#%%
'''
Experimental List:
[Index:   0]  1_resonator_spectroscopy_093621
[Index:   1]  2_resonator_spectroscopy_094134
[Index:   2]  3_resonator_spectroscopy_094219
[Index:   3]  4_resonator_spectroscopy_094320
[Index:   4]  5_resonator_spectroscopy_vs_amplitude_094522
[Index:   5]  6_qubit_spectroscopy_094702
[Index:   6]  7_rabi_chevron_duration_094902
[Index:   7]  8_rabi_chevron_amplitude_095219
[Index:   8]  9_power_rabi_095259
[Index:   9]  10_power_rabi_error_amplification_095348
[Index:  10]  12_T1_095552
[Index:  11]  13_ramsey_chevron_095802
[Index:  12]  14_ramsey_w_virtual_rotation_095904
[Index:  13]  15_echo_100214
[Index:  14]  16_randomized_benchmarking_101323
[Index:  15]  17_IQ_blobs_141728
[Index:  16]  18_IQ_blobs_142226
[Index:  17]  37_DRAG_calibration_Google_070317

The Qiskit reference list from Dr.Minje

manuals/verification/randomized_benchmarking.html
manuals/characterization/t1.html
manuals/characterization/t2hahn.html
manuals/characterization/t2ramsey.html
manuals/characterization/tphi.html
manuals/measurement/readout_mitigation.html
manuals/measurement/restless_measurements.html
'''