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

##################
#      QUA       #
##################


with program() as PROG:

    b1 = declare(int)
    b2 = declare(int)
    b3 = declare(fixed)
    b4 = declare(int, size=2)

    b1_st = declare_stream()
    b2_st = declare_stream()
    b3_st = declare_stream()
    b4_st = declare_stream()

    assign(b1, 2 + 3)
    assign(b2, 2 * 3)
    assign(b3, Math.cos(1))
    assign(b4, Math.max(2, 3))

    save(b1, b1_st)
    save(b2, b2_st)
    save(b3, b3_st)
    save(b4, b4_st)

    with stream_processing():
        b1_st.save("b1")
        b2_st.save("b2")
        b3_st.save("b3")
        b4_st.save("b4")


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

data = ["b1", "b2", "b3", "b4"]
results = fetching_tool(job, data_list=data)
fetched_data = results.fetch_all()

b1 = fetched_data[0]
b2 = fetched_data[1]
b3 = fetched_data[2]
b4 = fetched_data[3]

assert b1 == 5, "2 + 3"
assert b2 == 6, "2 *3"
assert np.allclose(b3, np.array([np.cos(1)])), "cos(1)"
assert b4 == 3, "max(2, 3)"

print("success!")



# %%
