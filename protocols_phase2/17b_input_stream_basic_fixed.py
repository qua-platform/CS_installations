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

qubits = get_elements("qubit", cons="con1", fems=[1, 2], ports=2)

print_elements_ports(qubits)

config["pulses"]["const_pulse"]["length"] = 40

seed = 0
seq_len = 1000


###################
# The QUA program #
###################
##################
#      QUA       #
##################


with program() as PROG:
    # n = declare(int)
    m = declare(int)
    k = declare(int)
    seq_ist = declare_input_stream(
        fixed,
        name="_seq",
        size=seq_len,
    )
    seq_ost = declare_stream()


    advance_input_stream(seq_ist)


    with for_(m, 0, m < seq_len, m + 1):
        
        with for_(k, 0, k < 10, k + 1):
            play("const", qubits[0])

        save(seq_ist[m], seq_ost)
    

    with stream_processing():
        seq_ost.buffer(seq_len).save("sequence")



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


from datetime import datetime

def print_this_log(start_time, seq_len, seq):
    current_datetime = datetime.now()
    current_datetime_str = current_datetime.strftime("%Y/%m/%d-%H:%M:%S")
    elapsed_time = current_datetime - start_time
    elapsed_time_secs = int(elapsed_time.total_seconds())
    _this_log = f"{current_datetime_str}, seq_len: {seq_len}, elapsed_secs: {elapsed_time_secs}, seq: {seq}"
    print(_this_log)


# fetch_names = ["iteration", "sequence"]
fetch_names = ["sequence"]
results = fetching_tool(job, data_list=fetch_names)


ress = []
seq_instream = np.zeros(seq_len).astype(int)
seq_outstream = np.zeros(seq_len).astype(int)
start_time = datetime.now()
np.random.seed(seed)


seq_instream = np.random.rand(seq_len)

# Get log
print_this_log(start_time, seq_len, seq_instream)

# Input stream encoded circuit
job.push_to_input_stream("_seq", seq_instream.tolist())

# Fetch results
print("fetch result!")
seq_outstream = results.fetch_all()[0]

assert np.allclose(seq_instream, seq_outstream), "input stream is not equal to output streams"
print("Success!")

qm.close()

# %%
