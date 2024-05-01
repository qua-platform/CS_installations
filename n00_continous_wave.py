# %%
"""
        PLAY A CONTINUOUS TONE
"""

import qm.qua as qua
import qm as qm_api
from configuration import config, qop_ip, cluster_name

###################
# The QUA program #
###################

with qua.program() as continuous_wave:

    with qua.infinite_loop_():
        qua.play('cw', 'resonator')


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = qm_api.QuantumMachinesManager(host=qop_ip, cluster_name=cluster_name)

#######################
# Simulate or execute #
#######################

# Open the quantum machine
qm = qmm.open_qm(config)
# Send the QUA program to the OPX, which compiles and executes it
job = qm.execute(continuous_wave)

# %%
