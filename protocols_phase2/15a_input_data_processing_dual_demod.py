# %%
import matplotlib.pyplot as plt
import numpy as np
from qm import QuantumMachinesManager, SimulationConfig
from qm.qua import *
from qualang_tools.results.results import fetching_tool
from qualang_tools.units import unit
from qua_config.configuraiton_cluster4_3chassis_8fems422_band1 import *


#############
#   Parameters   #
##################

# qubits = get_all_elements("qubit")
# qubits = get_elements("qubit", cons=["con1", "con2"], fems=[1, 2], ports=[2, 7])
resonators = get_elements("resonator", cons=["con1", "con2", "con3"], fems=[1, 2, 3, 4], ports=[1, 8])
# jpas = get_elements("jpa", cons="con3", fems=[1, 2], ports=7)
print_elements_ports(resonators)

##################
#      QUA       #
##################


with program() as PROG:

    n = declare(int)
    I = [declare(fixed) for _ in range(len(resonators))]
    Q = [declare(fixed) for _ in range(len(resonators))]
    I_st = [declare_stream() for _ in range(len(resonators))]
    Q_st = [declare_stream() for _ in range(len(resonators))]

    with for_(n, 0, n < 100, n+1):
        for i, rr in enumerate(resonators):
            measure(
                "readout",
                rr,
                dual_demod.full("cos", "sin", I[i]),
                dual_demod.full("minus_sin", "cos", Q[i]),
            )
            wait(250, rr)
            save(I[i], I_st[i])
            save(Q[i], Q_st[i])

    with stream_processing():
        for i, rr in enumerate(resonators):
            I_st[i].average().save(f"I_{rr}")
            Q_st[i].average().save(f"Q_{rr}")


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
    fetch_names.append(f"I_{rr}")
    fetch_names.append(f"Q_{rr}")

results = fetching_tool(job, data_list=fetch_names)
fetched_data = results.fetch_all()

nsqrt = int(np.ceil(np.sqrt(len(resonators))))
if (nsqrt - 1) * nsqrt >= len(resonators):
    ncols, nrows = nsqrt - 1, nsqrt
else:
    ncols, nrows = nsqrt, nsqrt

fig, axss = plt.subplots(ncols, nrows, figsize=(3 * nrows, 3 * ncols))
for i, (ax, rr) in enumerate(zip(axss.ravel(), resonators)):
    x = fetched_data[2 * i]
    y = fetched_data[2 * i + 1]
    v_max = max(abs(x), abs(y))
    ax.set_title(rr)
    ax.vlines(x=0, ymin=-1.2 * v_max, ymax=+1.2 * v_max, color='k', alpha=0.2)
    ax.hlines(y=0, xmin=-1.2 * v_max, xmax=+1.2 * v_max, color='k', alpha=0.2)
    ax.scatter(x=x, y=y, c='r')
    ax.set_xlim([-1.2 * v_max, 1.2 * v_max])
    ax.set_ylim([-1.2 * v_max, 1.2 * v_max])
    ax.set_xlabel("I [V]") if i // nrows == ncols - 1 else None
    ax.set_ylabel("Q [V]") if i % nrows == 0 else None
plt.tight_layout()
plt.show()


# %%