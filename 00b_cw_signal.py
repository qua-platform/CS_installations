# QUA embedded in a Python 
import qm.qua as qua  
from qm import QuantumMachinesManager, SimulationConfig
from configuration import config, qop_ip, cluster_name
#from qm_saas import QmSaas, QOPVersion
import matplotlib.pyplot as plt
import time 
from qm.octave import QmOctaveConfig
import os

###################
# The QUA program #
###################

with qua.program() as cw_output:  
    with qua.infinite_loop_():
        qua.play("const", "qubit2")


#####################################
#  Open Communication with the QOP  #
#####################################

simulate = False
simulation_in_cloud = False

if simulate: 

    if simulation_in_cloud:
        client = QmSaas(
        host="qm-saas.dev.quantum-machines.co",
        email="benjamin.safvati@quantum-machines.co",
        password="ubq@yvm3RXP1bwb5abv")        
        instance = client.simulator(QOPVersion.v2_5_0)
        instance.spawn()
        qmm = QuantumMachinesManager(host=instance.host,
                                    port=instance.port,
                                    connection_headers=instance.default_connection_headers)
    else:
        qmm = QuantumMachinesManager(host=qop_ip, 
                                    cluster_name=cluster_name)

    simulation_config = SimulationConfig(duration=1_000) # duration is in units of clock cycles, i.e., 4 nanoseconds
    job = qmm.simulate(config, cw_output, simulation_config)
    job.get_simulated_samples().con1.plot()
    if simulation_in_cloud:
        instance.close()
    plt.show()

else:
    qmm = QuantumMachinesManager(host=qop_ip, cluster_name=cluster_name, octave_calibration_db_path=os.getcwd())
    qm = qmm.open_qm(config)
    job = qm.execute(cw_output)
    time.sleep(20)
    qmm.close_all_qms()
    job.halt()