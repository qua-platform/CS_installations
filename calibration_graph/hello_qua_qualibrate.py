# %%
from qm.qua import *
from qm import QuantumMachinesManager
from qua_config.configuration import *
from qualibrate import NodeParameters, QualibrationNode


# Define input parameters for QualibrationNode
class Parameters(NodeParameters):
    num_reps: int = 100


# Create QualibrationNode
node = QualibrationNode("hello_qua_qualibrate", parameters=Parameters())


###################################################
#  Load QuAM and open Communication with the QOP  #
###################################################


with program() as prog:
    n = declare(int)
    
    with for_(n, 0, n < node.parameters.num_reps, n + 1):
        play("cw", "qe")


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name)
qm = qmm.open_qm(config)
job = qm.execute(prog)


# %%
