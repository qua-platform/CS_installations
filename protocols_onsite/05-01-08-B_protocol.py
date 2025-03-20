# %%
import matplotlib.pyplot as plt
import numpy as np
from qm import QuantumMachinesManager, SimulationConfig
from qm.qua import *
from qualang_tools.results import fetching_tool, progress_counter
from qualang_tools.loops.loops import from_array
from qualang_tools.units import unit
from qua_config.configuraiton_cluster1_1chassis_2fems2 import *


##################
#   Parameters   #
##################

rr1 = get_elements("resonator", cons="con1", fems=[1], ports=[2])
# rr2 = get_elements("resonator", cons="con2", fems=1, ports=1)
# rr3 = get_elements("resonator", cons="con3", fems=1, ports=1)
qb1 = get_elements("qubit", cons="con1", fems=[1], ports=[3])
# qb2 = get_elements("qubit", cons="con2", fems=1, ports=2)
# qb3 = get_elements("qubit", cons="con3", fems=1, ports=2)

qubits = [qb1]
resonators = [rr1]

print_elements_ports(qubits + resonators)


duc = 1
band = 1
full_scale_power_dbm = 1
amplitude = 0.5
freq_lo = 0.45 * u.GHz # IF = 50 * u.MHz

for con, con_val in config["controllers"].items():
    for fem, fem_val in con_val["fems"].items():
        for ao, ao_val in fem_val["analog_outputs"].items():
            ao_val["band"] = band
            ao_val["full_scale_power_dbm"] = full_scale_power_dbm
            ao_val["upconverters"][duc]["frequency"] = freq_lo
config["waveforms"]["const_wf"]["sample"] = amplitude




n_avg = 10

##################
#      QUA       #
##################


with program() as PROG:

    m = declare(int)
    n = declare(int)
    I = [declare(fixed) for _ in range(len(qubits))]
    Q = [declare(fixed) for _ in range(len(qubits))]

    # with for_(n, 0, n < n_avg, n+1):
    with infinite_loop_():
    
        for i, (qb, rr) in enumerate(zip(qubits, resonators)):
            play("const", qb)
            align(rr, qb)

            measure(
                "readout",
                rr,
                dual_demod.full("cos", "sin", I[i]),
                dual_demod.full("minus_sin", "cos", Q[i]),
            )
            align(rr, qb)

            with if_(I[i] > 0):
                update_frequency(qb, IF + 50 * u.MHz)
            # with else_():
            #     update_frequency(qb, IF - 50 * u.MHz)
            
            play("const", qb)

            wait(500, rr)


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


simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=500)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, PROG, simulation_config)
    # Plot the simulated samples
    job.get_simulated_samples().con1.plot()
    plt.show()

else:
    qm = qmm.open_qm(config)
    job = qm.execute(PROG)
    # import time;time.sleep(1);job.halt()
    # job = qm.execute(PROG)


    # # Save files
    # from qualang_tools.results.data_handler import DataHandler
    # script_name = Path(__file__).name
    # data_handler = DataHandler(root_data_folder=save_dir)
    # data_handler.additional_files = {script_name: script_name, debug_filepath: debug_filepath, **default_additional_files}
    # data_handler.save_data(data={"config": config}, name=script_name.replace(".py", ""))


######################################
#  Fetch & Analysis & Visualization  #
######################################




# %%