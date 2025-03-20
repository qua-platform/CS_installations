# %%
from qm.qua import *
from qualang_tools.units import unit
from qm import QuantumMachinesManager, SimulationConfig
from qua_config.configuraiton_cluster4_3chassis_8fems422_band1 import *


##################
#   Parameters   #
##################

rr1 = get_elements("resonator", cons="con1", fems=1, ports=1)
rr2 = get_elements("resonator", cons="con1", fems=1, ports=8)
qb1 = get_elements("qubit", cons="con1", fems=1, ports=2)
qb2 = get_elements("qubit", cons="con1", fems=1, ports=7)

qubits = [qb1, qb2]
resonators = [rr1, rr2]


print_elements_ports(qubits + resonators)


new_readout_length = 400
for rr in resonators:
    config["pulses"]["readout_pulse"]["length"] = new_readout_length
config["pulses"]["const_pulse"]["length"] = new_readout_length


update_readout_length(new_readout_length, resonators)

##################
#      QUA       #
##################


with program() as PROG:

    with infinite_loop_():

        for qb, rr in zip(qubits, resonators):
            play("const", qb)
            wait(25, qb)
            play("const", qb)
            align(qb, rr)
            play("const", rr)
        
        wait(50)

        
#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=host_ip, cluster_name=cluster_name)
qmm.clear_all_job_results()
qmm.close_all_qms()

# Open a quantum machine to execute the QUA program

from pathlib import Path
from qm import generate_qua_script
debug_filepath = sourceFile = f"debug_{Path(__file__).stem}.py"
sourceFile = open(debug_filepath, "w")
print(generate_qua_script(PROG, config), file=sourceFile)
sourceFile.close()

qm = qmm.open_qm(config)

# Send the QUA program to the OPX, which compiles and executes it - Execute does not block python!
job = qm.execute(PROG)
# %%
