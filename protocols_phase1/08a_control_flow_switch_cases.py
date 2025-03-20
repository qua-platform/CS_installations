# %%
import matplotlib.pyplot as plt
import numpy as np
from qm import QuantumMachinesManager, SimulationConfig
from qm.qua import *
from qualang_tools.results import fetching_tool, progress_counter
from qualang_tools.loops.loops import from_array
from qualang_tools.units import unit
from qua_config.configuraiton_cluster4_3chassis_8fems422_band1 import *


##################
#   Parameters   #
##################

# resonators = get_elements("resonator", cons=["con1", "con2", "con3"], fems=[1, 2, 3, 4], ports=[1, 8])
# jpas = get_elements("jpa", cons="con3", fems=[1, 2], ports=7)


# pick an specified rr
resonators = get_elements("resonator", cons=["con1", "con2", "con3"], fems=[1, 2, 3, 4], ports=[1, 8])
qubits = get_elements("qubit", cons=["con1", "con2", "con3"], fems=[1, 2, 3, 4], ports=[2, 7])


print_elements_ports(resonators + resonators)


config["pulses"]["const_pulse"]["length"] = 40


n_avg = 50

##################
#      QUA       #
##################


with program() as PROG:

    m = declare(int)
    n = declare(int)
    I = [declare(fixed) for _ in range(len(qubits))]
    Q = [declare(fixed) for _ in range(len(qubits))]
    I_st = [declare_stream() for _ in range(len(qubits))]
    Q_st = [declare_stream() for _ in range(len(qubits))]

    with for_(n, 0, n < n_avg, n+1):
    
        for i, (qb, rr) in enumerate(zip(qubits, resonators)):

            with for_(m, 0, m < 24, m + 1):
                # marker
                with switch_(m, unsafe=True):
                    with case_(0):
                        wait(25, qb) # qb.xy.wait(20)  # I
                    with case_(1):
                        play("const", qb)
                    with case_(2):
                        play("const", qb)
                        play("const", qb)
                    with case_(3):
                        play("const", qb)
                        play("const", qb)
                        play("const", qb)
                    with case_(4):
                        play("const", qb)
                        play("const", qb)
                        play("const", qb)
                        play("const", qb)
                    with case_(5):
                        play("x180", qb)
                    with case_(6):
                        play("x180", qb)
                        play("x180", qb)
                    with case_(7):
                        play("x180", qb)
                        play("x180", qb)
                        play("x180", qb)
                    with case_(8):
                        play("x180", qb)
                        play("x180", qb)
                        play("x180", qb)
                        play("x180", qb)
                    with case_(9):
                        play("const_S", qb)
                    with case_(10):
                        play("const_S", qb)
                        play("const_S", qb)
                    with case_(11):
                        play("const_S", qb)
                        play("const_S", qb)
                        play("const_S", qb)
                    with case_(12):
                        play("const_S", qb)
                        play("const_S", qb)
                        play("const_S", qb)
                        play("const_S", qb)
                    with case_(13):
                        play("x90", qb)
                    with case_(14):
                        play("x90", qb)
                        play("x90", qb)
                    with case_(15):
                        play("x90", qb)
                        play("x90", qb)
                        play("x90", qb)
                    with case_(16):
                        play("x90", qb)
                        play("x90", qb)
                        play("x90", qb)
                        play("x90", qb)
                    with case_(17):
                        play("const_L", qb)
                    with case_(18):
                        play("const_L", qb)
                        play("const_L", qb)
                    with case_(19):
                        play("const_L", qb)
                        play("const_L", qb)
                        play("const_L", qb)
                    with case_(20):
                        play("const_L", qb)
                        play("const_L", qb)
                        play("const_L", qb)
                        play("const_L", qb)
                    with case_(21):
                        play("y180", qb)
                    with case_(22):
                        play("y180", qb)
                        play("y180", qb)
                    with case_(23):
                        play("y180", qb)
                        play("y180", qb)
                        play("y180", qb)

            measure(
                "readout",
                rr,
                dual_demod.full("cos", "sin", I[i]),
                dual_demod.full("minus_sin", "cos", Q[i]),
            )


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