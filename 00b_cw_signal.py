# QUA embedded in a Python 
import qm.qua as qua  
from qm import QuantumMachinesManager, SimulationConfig
from configuration import config, qop_ip, cluster_name
#from qm_saas import QmSaas, QOPVersion
import matplotlib.pyplot as plt
import time 
import os

###################
# The QUA program #
###################

with qua.program() as cw_output:  
    with qua.infinite_loop_():
        qua.play("const", "q2")


#####################################
#  Open Communication with the QOP  #
#####################################

simulate = False

if simulate: 

    qmm = QuantumMachinesManager(host=qop_ip, 
                                    cluster_name=cluster_name)

    simulation_config = SimulationConfig(duration=1_000) # duration is in units of clock cycles, i.e., 4 nanoseconds
    job = qmm.simulate(config, cw_output, simulation_config)
    job.get_simulated_samples().con1.plot()
    plt.show()

else:
    qmm = QuantumMachinesManager(host=qop_ip, cluster_name=cluster_name, octave_calibration_db_path=os.getcwd())
    qm = qmm.open_qm(config)
    job = qm.execute(cw_output)
    time.sleep(20)
    qmm.close_all_qms()
    job.halt()