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


rr1 = get_elements("resonator", cons="con1", fems=1, ports=1)
rr2 = get_elements("resonator", cons="con1", fems=2, ports=1)
qb1 = get_elements("qubit", cons="con1", fems=1, ports=2)
qb2 = get_elements("qubit", cons="con1", fems=2, ports=2)

qubits = [qb1, qb2]
resonators = [rr1, rr2]


print_elements_ports(qubits + resonators)

# for elem in qubits + resonators + jpas:
#     config["elements"][elem].pop("thread", None)

for qb in qubits:
    con, fem, port = qb.split("_")[1].split("-")
    if con in ["con2", "con3"]:
        for fem, fem_val in config["controllers"][con]["fems"].items():
            for port, port_val in fem_val["analog_outputs"].items():
                port_val["delay"] = 4


new_readout_length = 400
for rr in resonators:
    config["pulses"]["readout_pulse"]["length"] = new_readout_length
config["pulses"]["const_pulse"]["length"] = new_readout_length


update_readout_length(new_readout_length, resonators)

##################
#      QUA       #
##################


with program() as PROG:

    # I = [declare_local(fixed, element=qb.resonator.name) for qb in qubits]
    # Q = [declare_local(fixed, element=qb.resonator.name) for qb in qubits]
    I = [declare(fixed) for _ in range(len(resonators))]
    Q = [declare(fixed) for _ in range(len(resonators))]
    s = [declare(bool) for _ in range(len(resonators))]
    feedback_condition = declare(bool)

    def inter_chassis_feedback(rr1, rr2, qb1, qb2, I1, Q1, s1, I2, Q2, s2):
        measure(
            "readout",
            rr1,
            dual_demod.full("cos", "sin", I1),
            dual_demod.full("minus_sin", "cos", Q1),
        )
        measure(
            "readout",
            rr2,
            dual_demod.full("cos", "sin", I2),
            dual_demod.full("minus_sin", "cos", Q2),
        )
        assign(s1, I1 >= -8)
        assign(s2, I2 >= -8)
        assign(feedback_condition, broadcast.and_(s1, s2))
        # assign(feedback_condition, broadcast.or_(s1, s2))
        # assign(feedback_condition, broadcast.xor_(s1, s2))
        
        align(rr1, qb1)
        align(rr2, qb2)
        with if_(feedback_condition):
            play("const", qb1)
            play("const", qb2)


    with infinite_loop_():
        inter_chassis_feedback(rr1, rr2, qb1, qb2, I[0], Q[0], s[0], I[1], Q[1], s[1])
        wait(500)

        # inter_chassis_feedback(rr2, rr3, qb2, qb3, I[1], Q[1], s[1], I[2], Q[2], s[2])
        # wait(500)

        # inter_chassis_feedback(rr3, rr1, qb3, qb1, I[2], Q[2], s[2], I[0], Q[0], s[0])
        # wait(500)


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
