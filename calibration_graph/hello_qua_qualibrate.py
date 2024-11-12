# %%
from qm.qua import *
from qm import QuantumMachinesManager
from qualang_tools.units import unit
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
# Class containing tools to help handling units and conversions.
u = unit(coerce_to_integer=True)


with program() as prog:
    n = declare(int)
    
    with for_(n, 0, n < node.parameters.num_reps, n + 1):
        play("CW", "qe1")
        play("CW", "qe2")


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config)
qm = qmm.open_qm(config)
job = qm.execute(prog)


# %%
