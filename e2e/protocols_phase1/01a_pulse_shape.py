# %%
from qm import QuantumMachinesManager, SimulationConfig
from qm.qua import *
from qualang_tools.units import unit
from qua_config.configuraiton_cluster4_3chassis_8fems422_band1 import *
from qua_config.configuraiton_cluster4_3chassis_8fems422_band1 import *


##################
#   Parameters   #
##################
##################

qubits = get_all_elements("qubit")
# qubits = get_elements("qubit", cons=["con1", "con2"], fems=[1, 2], ports=[2, 7])
# resonators = get_elements("resonator", cons=["con1", "con2"], fems=[1, 2], ports=[1, 8])
# jpas = get_elements("jpa", cons="con3", fems=[1, 2], ports=7)
print_elements_ports(qubits)

config["pulses"]["const_pulse"]["length"] = 40

##################
#      QUA       #
##################


with program() as PROG:

    with infinite_loop_():

        for qb in qubits:
            play("const", qb)
            wait(10, qb)
            play("const", qb)
            wait(10, qb)
            play("x180", qb)
            wait(10, qb)
            play("x180", qb)
            wait(10, qb)

        wait(25)


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=host_ip, port=qop_port, cluster_name=cluster_name)

qm = qmm.open_qm(config)
job = qm.execute(PROG)


# Save files
from qualang_tools.results.data_handler import DataHandler
script_name = Path(__file__).name
data_handler = DataHandler(root_data_folder=save_dir)
data_handler.additional_files = {script_name: script_name, **default_additional_files}
data_handler.save_data(data={"config": config}, name=script_name.replace(".py", ""))


######################################
#  Fetch & Analysis & Visualization  #
######################################



# %%