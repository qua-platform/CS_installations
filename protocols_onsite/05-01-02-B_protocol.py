# %%
from qm import QuantumMachinesManager, SimulationConfig
from qm.qua import *
from qualang_tools.units import unit
from qualang_tools.results.results import fetching_tool
from qua_config.configuraiton_cluster1_1chassis_2fems2 import *
import matplotlib.pyplot as plt


##################
#   Parameters   #
##################

duc = 1
# qubits = get_all_elements("qubit", duc=duc)
resonators = get_elements("resonator", cons=["con1"], fems=[2, 3], ports=[1], duc=duc)
print_elements_ports(resonators)

band = 1
full_scale_power_dbm = 1
amplitude = 0.5
freq_lo = 0.05 * u.GHz # IF = 50 * u.MHz

for con, con_val in config["controllers"].items():
    for fem, fem_val in con_val["fems"].items():
        for ao, ao_val in fem_val["analog_outputs"].items():
            ao_val["band"] = band
            ao_val["full_scale_power_dbm"] = full_scale_power_dbm
            ao_val["upconverters"][duc]["frequency"] = freq_lo
config["waveforms"]["const_wf"]["sample"] = amplitude

arb_amp = 0.5
arb_len = 80
seed = 0
np.random.seed(seed)
i_array = arb_amp * np.random.rand(arb_len)
q_list = [0] * arb_len
config["pulses"]["arb_pulse"]["length"] = arb_len
config["waveforms"]["arb_I_wf"]["samples"] = i_array.tolist()
config["waveforms"]["arb_Q_wf"]["samples"] = q_list
wghs = config["integration_weights"]
wghs["cosine_arb_weights"]["cosine"] = [(1.0, arb_len)]
wghs["cosine_arb_weights"]["sine"] = [(0.0, arb_len)]
wghs["sine_arb_weights"]["cosine"] = [(0.0, arb_len)]
wghs["sine_arb_weights"]["sine"] = [(1.0, arb_len)]
wghs["minus_sine_arb_weights"]["cosine"] = [(0.0, arb_len)]
wghs["minus_sine_arb_weights"]["sine"] = [(-1.0, arb_len)]


##################
#      QUA       #
##################

n_avg = 1
with program() as PROG:
    n = declare(int)
    adc_st = [declare_stream(adc_trace=True) for _ in range(len(resonators))]

    with for_(n, 0, n < n_avg, n + 1):
        for i, rr in enumerate(resonators):
            reset_if_phase(rr)
            measure("readout", rr, adc_stream=adc_st[i])

    with stream_processing():
        for i, rr in enumerate(resonators):
            if config["elements"][rr]["MWOutput"]["port"][2] == 1:
                adc_st[i].input1().real().save(f"adc_I_{rr}")
                adc_st[i].input1().image().save(f"adc_Q_{rr}")
            else:
                adc_st[i].input2().real().save(f"adc_I_{rr}")
                adc_st[i].input2().image().save(f"adc_Q_{rr}")

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=host_ip, cluster_name=cluster_name)
qmm.clear_all_job_results()
qmm.close_all_qms()

from pathlib import Path
from qm import generate_qua_script
debug_filepath = sourceFile = f"debug_{Path(__file__).stem}.py"
sourceFile = open(debug_filepath, "w")
print(generate_qua_script(PROG, config), file=sourceFile)
sourceFile.close()


qm = qmm.open_qm(config)
job = qm.execute(PROG)
import time;time.sleep(1);job.halt()
job = qm.execute(PROG)


# Save files
from qualang_tools.results.data_handler import DataHandler
script_name = Path(__file__).name
data_handler = DataHandler(root_data_folder=save_dir)
data_handler.additional_files = {script_name: script_name, debug_filepath: debug_filepath, **default_additional_files}
data_handler.save_data(data={"config": config}, name=script_name.replace(".py", ""))


######################################
#  Fetch & Analysis & Visualization  #
######################################

fetch_names = []
for rr in resonators:
    fetch_names.append(f"adc_I_{rr}")
    fetch_names.append(f"adc_Q_{rr}")

results = fetching_tool(job, data_list=fetch_names)
fetched_data = results.fetch_all()

nsqrt = int(np.ceil(np.sqrt(len(resonators))))
if (nsqrt - 1) * nsqrt >= len(resonators):
    ncols, nrows = nsqrt - 1, nsqrt
else:
    ncols, nrows = nsqrt, nsqrt

fig, axss = plt.subplots(ncols, nrows, figsize=(3 * nrows, 3 * ncols), sharex=True, sharey=True)
for i, (ax, rr) in enumerate(zip(axss.ravel(), resonators)):
    val = config["elements"][rr]["MWOutput"]["port"]
    ax.set_title(rr)
    ax.plot(u.raw2volts(fetched_data[2 * i]))
    ax.plot(u.raw2volts(fetched_data[2 * i + 1]))
    ax.legend(["I", "Q"])
    ax.set_xlabel("time [ns]") if i // nrows == ncols - 1 else None
    ax.set_ylabel("voltage [V]") if i % nrows == 0 else None
plt.tight_layout()
plt.show()


# %%s