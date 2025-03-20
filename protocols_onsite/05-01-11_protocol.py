# %%
import matplotlib.pyplot as plt
import numpy as np
from qm import QuantumMachinesManager, SimulationConfig
from qm.qua import *
from qualang_tools.results import fetching_tool, progress_counter
from qualang_tools.loops.loops import from_array
from qualang_tools.units import unit
from qua_config.configuraiton_cluster1_1chassis_2fems2 import *


##################
#   Parameters   #
##################

rr1 = get_elements("resonator", cons="con1", fems=1, ports=1)
rr2 = get_elements("resonator", cons="con2", fems=1, ports=1)
# rr3 = get_elements("resonator", cons="con3", fems=1, ports=1)
qb1 = get_elements("qubit", cons="con1", fems=1, ports=2)
qb2 = get_elements("qubit", cons="con2", fems=1, ports=2)
# qb3 = get_elements("qubit", cons="con3", fems=1, ports=2)

qubits = [qb1, qb2]
resonators = [rr1, rr2]

print_elements_ports(qubits + resonators)

for qb in qubits:
    con = qb.split("_")[1].split("-")[0]
    if con in ["con2", "con3"]:
        for fem, fem_val in config["controllers"][con]["fems"].items():
            for port, port_val in fem_val["analog_outputs"].items():
                port_val["delay"] = 4

n_avg = 100

##################
#      QUA       #
##################


with program() as PROG:

    m = declare(int)
    n = declare(int)
    thresh = declare(fixed)
    s = declare(bool)
    I = [declare(fixed) for _ in range(len(qubits))]
    Q = [declare(fixed) for _ in range(len(qubits))]
    I_st = [declare_stream() for _ in range(len(qubits))]
    Q_st = [declare_stream() for _ in range(len(qubits))]

    with for_(n, 0, n < n_avg, n+1):
    
        for i, (qb, rr) in enumerate(zip(qubits, resonators)):
            measure(
                "readout",
                rr,
                dual_demod.full("cos", "sin", I[i]),
                dual_demod.full("minus_sin", "cos", Q[i]),
            )
            align(rr, qb)
            
            with if_(I > 1):
                assign(I, 1)
            with elif_(I < -1):
                assign(I, -1)

            play("const" * amp(I), qb)

            wait(250, rr)


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




# %%