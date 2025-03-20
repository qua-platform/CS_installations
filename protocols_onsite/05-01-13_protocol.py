# %%
import matplotlib.pyplot as plt
import numpy as np
from qm import QuantumMachinesManager, SimulationConfig
from qm.qua import *
from qualang_tools.results.results import fetching_tool
from qualang_tools.units import unit
from qua_config.configuraiton_cluster1_1chassis_2fems2 import *


##################
#   Parameters   #
##################

rr1 = get_elements("resonator", cons="con1", fems=1, ports=1)
qb1 = get_elements("qubit", cons="con1", fems=1, ports=2)

print_elements_ports([rr1, qb1])


##################
#      QUA       #
##################

set_pt = -0.011
T = 100  # Integral gain time constant
alpha = 1 / T
kp = 1
ki = 5
kd = 0
initial_amp = 0.1

with program() as PROG:
    point = declare(fixed, value=0)
    set_point = declare(fixed, value=set_pt)
    error = declare(fixed, value=0.002)
    prev_error = declare(fixed, value=0)  # previous step error
    accum = declare(fixed, value=0)
    gradient = declare(fixed, value=0.017)
    a = declare(fixed, value=initial_amp)
    b = declare(fixed)
    c = Random()

    with for_(b, 0, b<1, b + 0.1):

        frame_rotation_2pi(c.rand_fixed(), "readout_demod")
        measure(rr1, "readout_demod", None, integration.full("cos", point))
        align()

        # save(point, p_st)
        assign(prev_error, error)
        assign(error, (point - set_point) << 1)

        # save(error, "debug1")
        assign(accum, (1 - alpha) * accum + alpha * error)

        # save(accum, "debug2")
        assign(gradient, error - prev_error)
        assign(a, a + kp * error + 5 * (5 * (ki * accum)) + kd * gradient)

        # save(a, "debug3")
        play("const"*amp(a), qb1)




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
