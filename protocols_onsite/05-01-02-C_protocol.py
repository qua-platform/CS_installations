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
qubits = [get_elements("qubit", cons=["con1"], fems=[1], ports=[3], duc=duc)]

print_elements_ports(qubits)

band = 1
full_scale_power_dbm = 1
amplitude = 0.5
freq_lo = 0.45 * u.GHz # IF = 50 * u.MHz

for con, con_val in config["controllers"].items():
    for fem, fem_val in con_val["fems"].items():
        for ao, ao_val in fem_val["analog_outputs"].items():
            ao_val["band"] = band
            ao_val["full_scale_power_dbm"] = full_scale_power_dbm
            ao_val["upconverters"][duc]["frequency"] = freq_lo
config["waveforms"]["const_wf"]["sample"] = amplitude

for qb in qubits:
    config["elements"][f"{qb}-twin"]["core"] = f"{qb}-twin"

flattops = [op for op in config["elements"][qubits[0]]["operations"] if op.startswith("gauss_flattop")]
flattops.sort()

durations = np.arange(4, )
duration_segment = int(1e8) # int(2e9 // 4)

##################
#      QUA       #
##################

n_avg = 1
with program() as PROG:
    n = declare(int)

    with infinite_loop_():
        for qb in qubits:
            twin = f"{qb}-twin"
            # for ft in flattops:
            #     play(ft, qb)
            #     wait(5, qb)

            play("gauss_rise_long", qb)
            wait(int(len(gauss_fall_long_wf) // 4), twin)

            with for_(n, 0, n < 25, n + 1):
                # play("const" * amp(GAUSS_AMP / CONST_AMP), twin, duration=duration_segment)
                play("const", twin, duration=duration_segment)
                wait(duration_segment, qb)

            play("gauss_fall_long", qb)
            wait(int(len(gauss_fall_long_wf) // 4), twin)

            wait(int(1e9 // 4), qb, twin)


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=host_ip, cluster_name=cluster_name, timeout=1200)
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
# import time;time.sleep(1);job.halt()
# job = qm.execute(PROG)


# # Save files
# from qualang_tools.results.data_handler import DataHandler
# script_name = Path(__file__).name
# data_handler = DataHandler(root_data_folder=save_dir)
# data_handler.additional_files = {script_name: script_name, debug_filepath: debug_filepath, **default_additional_files}
# data_handler.save_data(data={"config": config}, name=script_name.replace(".py", ""))


######################################
#  Fetch & Analysis & Visualization  #
######################################


# %%