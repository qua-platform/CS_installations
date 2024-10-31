# %%
from qm.qua import *
from qm import QuantumMachinesManager, SimulationConfig
from qualang_tools.units import unit
from configuration_with_lffem import *
import matplotlib.pyplot as plt
import numpy as np

###################################################
#  Load QuAM and open Communication with the QOP  #
###################################################
# Class containing tools to help handling units and conversions.
u = unit(coerce_to_integer=True)


with program() as prog:
    play("CW", "qe1")
    play("CW", "qe2")
    play("X", "clifford_gate")
    align()
    play("CW", "simple_element")
    align()
    play("CW", "gateL")
    play("CW", "gateM")
    play("CW", "gateR")
    align()
    play("CW", "Trigger5")
    play("CW", "Trigger6")
    play("CW", "lockin")
    play("CW", "lockin2")
    wait(1_000)


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config)
qm = qmm.open_qm(config)
job = qm.execute(prog)
# plt.show()


# %%
