# %%
import matplotlib.pyplot as plt
import numpy as np
from qm import QuantumMachinesManager, SimulationConfig
from qm.qua import *
from qualang_tools.results.results import fetching_tool
from qualang_tools.units import unit
from qua_config.configuraiton_cluster4_3chassis_8fems422_band1 import *


###################
#  Util Function  #
###################

def autocorrelation(arr, max_shift=20):
    """Compute normalized autocorrelation function for shifts between -max_shift and +max_shift."""
    arr = np.asarray(arr)
    n = len(arr)
    mean = np.mean(arr)
    var = np.var(arr)  # Variance for normalization

    shifts = np.arange(-max_shift, max_shift + 1)
    correlations = []

    for s in shifts:
        if s == 0:
            corr = 1  # Auto-correlation at shift 0 is always 1
        elif s > 0:
            corr = np.sum((arr[:n-s] - mean) * (arr[s:] - mean)) / ((n - s) * var)
        else:  # Negative shift
            corr = np.sum((arr[-s:] - mean) * (arr[:n+s] - mean)) / ((n + s) * var)
        
        correlations.append(corr)

    return shifts, correlations




##################
#   Parameters   #
##################

##################
#      QUA       #
##################


with program() as PROG:

    b1 = declare(bool)
    b2 = declare(bool)
    b3 = declare(bool)
    b4 = declare(bool)

    n = declare(int)
    r = declare(int)
    rand = Random(seed=0)

    b1_st = declare_stream()
    b2_st = declare_stream()
    b3_st = declare_stream()
    b4_st = declare_stream()
    r_st = declare_stream()

    assign(b1, 1 == 1)
    assign(b2, 1 > 0)
    assign(b3, 1 < 0)
    assign(b4, ~b2)

    save(b1, b1_st)
    save(b2, b2_st)
    save(b3, b3_st)
    save(b4, b4_st)

    with for_(n, 0, n < 100, n + 1):
        assign(r, rand.rand_int(24))
        save(r, r_st)
        wait(250)

    with stream_processing():
        b1_st.save("b1")
        b2_st.save("b2")
        b3_st.save("b3")
        b4_st.save("b4")
        r_st.save_all("rand")


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=host_ip, port=qop_port, cluster_name=cluster_name)

qm = qmm.open_qm(config)
job = qm.execute(PROG)


# Save files
from qualang_tools.results.data_handler import DataHandler
script_name = Path(__file__).name
data_handler = DataHandler(root_data_folder=save_dir)
data_handler.additional_files = {script_name: script_name, **default_additional_files}
data_handler.save_data(data={"config": config}, name=script_name.replace(".py", ""))


######################################
#  Fetch & Analysis & Visualization  #
######################################

data = ["b1", "b2", "b3", "b4", "rand"]
results = fetching_tool(job, data_list=data)
fetched_data = results.fetch_all()

b1 = fetched_data[0]
b2 = fetched_data[1]
b3 = fetched_data[2]
b4 = fetched_data[3]
rd = fetched_data[4]

assert b1, "1 == 1"
assert b2, "1 > 0"
assert not b3, "1 < 0"
assert not b4, "~(1 > 0)"

print("success! booleans")

shifts, correlations = autocorrelation(rd, max_shift=20)

# Plot results. autocorrelation should be 1 only for shift=0 and the rest is nearly 0.
plt.figure(figsize=(8, 4))
plt.plot(shifts, correlations, marker='o', linestyle='-', label="Autocorrelation")
plt.axhline(0, color='gray', linestyle='--', alpha=0.7)
plt.xlabel("Shift")
plt.ylabel("Autocorrelation")
plt.title("Autocorrelation of Random Integer Array (-20 to 20)")
plt.legend()
plt.grid()
plt.show()

# %%
