# %%
"""
(45) システムは、FPGA/VHDLプログラミングを必要とせず、if/else分岐、forル
ープ、whileループ、スイッチ・ケースを含む包括的な制御フローを実行可
能であること。 
⑤ ソフトウェア
"""

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

duc = 1
qubits = get_all_elements("qubit", duc=duc)

print_elements_ports(qubits)


config["pulses"]["const_pulse"]["length"] = 40
config["waveforms"]["const_wf"]["sample"] = 0.5


n_avg = 50

##################
#      QUA       #
##################


with program() as PROG:

    I = [declare(fixed) for _ in range(len(qubits))]
    Q = [declare(fixed) for _ in range(len(qubits))]
    I_st = [declare_stream() for _ in range(len(qubits))]
    Q_st = [declare_stream() for _ in range(len(qubits))]

    with infinite_loop_():
    
        for i, qb in enumerate(qubits):

            m = declare(int)
            n = declare(int)
            
            with for_(m, 0, m < 3, m + 1):
                # marker
                with switch_(m, unsafe=True):
                    with case_(0):
                        wait(10, qb) # qb.xy.wait(20)  # I
                        wait(4, qb)
                    with case_(1):
                        play("const", qb)
                        wait(4, qb)
                    with case_(2):
                        play("const", qb)
                        play("const", qb)
                        wait(4, qb)
                    with case_(3):
                        play("const", qb)
                        play("const", qb)
                        play("const", qb)
                        wait(4, qb)

                with if_(m > 1):
                    play("const" * amp(1.5), qb)
                    wait(4, qb)
                with else_():
                    play("const" * amp(0.5), qb)
                    wait(4, qb)

                assign(n, 0)
                with while_(n < 5):
                    play("const" * amp(0.2), qb)
                    wait(4, qb)                    
                    assign(n, n + 1)


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