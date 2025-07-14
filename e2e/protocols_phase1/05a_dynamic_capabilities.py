# %%
import matplotlib.pyplot as plt
import numpy as np
from qm import QuantumMachinesManager, SimulationConfig
from qm.qua import *
from qualang_tools.results.results import fetching_tool
from qualang_tools.units import unit
from qua_config.configuraiton_cluster4_3chassis_8fems422_band1 import *


##################
#   Parameters   #
##################

qubits = get_all_elements("qubit")
# qubits = get_elements("qubit", cons=["con1", "con2"], fems=[1, 2], ports=[2, 7])
# resonators = get_elements("resonator", cons=["con1", "con2", "con3"], fems=[1, 2, 3, 4], ports=[1, 8])
# jpas = get_elements("jpa", cons="con3", fems=[1, 2], ports=7)
print_elements_ports(qubits)

config["pulses"]["const_pulse"]["length"] = 100
config["waveforms"]["const_wf"]["sample"] = 1.0

##################
#      QUA       #
##################


with program() as PROG:

    amps = declare(fixed, value=[0.333, 0.666, 1.00])
    times = declare(int, value=[25, 50, 75])
    freqs = declare(int, value=[-450e6])
    phase = declare(fixed, value=[0.0, -0.5, 0.5])

    with infinite_loop_():

        # test amp, check on the scope
        for qb in qubits:
            play("const" * amp(amps[0]), qb)
            wait(25, qb)
            play("const" * amp(amps[1]), qb)
            wait(25, qb)
            play("const" * amp(amps[2]), qb)
            wait(25, qb)

        # wait(25)
        # align()

        # # test the duration, check on the scope
        # for qb in qubits:
        #     play("const", rr, duration=times[0])
        #     wait(25, qb)
        #     play("const", rr, duration=times[1])
        #     wait(25, qb)
        #     play("const", rr, duration=times[2])
        #     wait(25, qb)

        # wait(25)
        # align()

        # # test the frequency, check on the scope
        # for qb in qubits:
        #     update_frequency(rr, freqs[0])
        #     play("const", qb)
        #     wait(25, qb)
            # update_frequency(rr, freqs[1])
            # play("const", qb)
            # wait(25, qb)

        # wait(25)
        # align()

        # # test the phase, check on the scope
        # reset_global_phase()
        # for qb in qubits:
        #     frame_rotation_2pi(phase[0], qb)
        #     play("const", qb)
        #     wait(25, qb)

        
        # reset_global_phase()
        # for qb in qubits:
        #     frame_rotation_2pi(phase[1], qb)
        #     play("const", qb)
        #     wait(25, qb)

        # wait(50)


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