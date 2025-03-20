# %%
import matplotlib.pyplot as plt
import numpy as np
from qm import QuantumMachinesManager, SimulationConfig
from qm.qua import *
from qualang_tools.results.results import fetching_tool
from qualang_tools.loops.loops import from_array
from qualang_tools.units import unit
from qua_config.configuraiton_cluster4_3chassis_8fems422_band1 import *


##################
#   Parameters   #
##################

# resonators = get_all_elements("qubit")
# resonators = get_elements("qubit", cons=["con1", "con2"], fems=[1, 2], ports=[2, 7])
resonators = get_elements("resonator", cons=["con1", "con2", "con3"], fems=[1, 2, 3, 4], ports=[1, 8])
# jpas = get_elements("jpa", cons="con3", fems=[1, 2], ports=7)
print_elements_ports(resonators)


config["pulses"]["const_pulse"]["length"] = 100


n_avg = 50
frequencies = np.arange(0, 10, 2) * u.MHz
##################
#      QUA       #
##################


with program() as PROG:

    f = declare(int)
    n = declare(int)
    I = [declare(fixed) for _ in range(len(resonators))]
    Q = [declare(fixed) for _ in range(len(resonators))]
    s1 = [declare(bool) for _ in range(len(resonators))]
    s2 = [declare(bool) for _ in range(len(resonators))] 

    I_st = [declare_stream() for _ in range(len(resonators))]
    Q_st = [declare_stream() for _ in range(len(resonators))]
    s1_st = [declare_stream() for _ in range(len(resonators))] 
    s2_st = [declare_stream() for _ in range(len(resonators))] 

    with for_(*from_array(f, frequencies)):

        with for_(n, 0, n < n_avg, n+1):

            for i, rr in enumerate(resonators):
                measure(
                    "readout",
                    rr,
                    dual_demod.full("cos", "sin", I[i]),
                    dual_demod.full("minus_sin", "cos", Q[i]),
                )
                wait(250, rr)

                assign(I[i], 1.0)
                assign(Q[i], -1.0)
                assign(s1[i], 1 > 0)
                assign(s2[i], 1 < 0)

                save(I[i], I_st[i])
                save(Q[i], Q_st[i])
                save(s1[i], s1_st[i])
                save(s2[i], s2_st[i])

    with stream_processing():
        for i, rr in enumerate(resonators):
            # I_st[i].buffer(len(frequencies)).average().save(f"I_{rr}")
            # Q_st[i].buffer(len(frequencies)).average().save(f"Q_{rr}")
            I_st[i].buffer(len(frequencies)).buffer(n_avg).map(FUNCTIONS.average()).save(f"I_avg_{rr}")
            Q_st[i].buffer(len(frequencies)).buffer(n_avg).map(FUNCTIONS.average()).save(f"Q_avg_{rr}")
            s1_st[i].boolean_to_int().buffer(len(frequencies)).average().save(f"s1_{rr}")
            s2_st[i].boolean_to_int().buffer(len(frequencies)).average().save(f"s2_{rr}")




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


qm = qmm.open_qm(config)
job = qm.execute(PROG)
import time;time.sleep(1);job.halt()
job = qm.execute(PROG)


# Save files
from qualang_tools.results.data_handler import DataHandler
script_name = Path(__file__).name
data_handler = DataHandler(root_data_folder=save_dir)
data_handler.additional_files = {script_name: script_name, debug_filepath: debug_filepath, **default_additional_files}
data_handler.save_data(data={"config": config}, name=script_name.replace(".py", ""))


######################################
#  Fetch & Analysis & Visualization  #
######################################


data = []
for rr in resonators:
    data.extend([
        # f"I_{rr}",
        # f"Q_{rr}",
        f"I_avg_{rr}",
        f"Q_avg_{rr}",
        f"s1_{rr}",
        f"s2_{rr}",
    ])

results = fetching_tool(job, data_list=data)

fetched_data = results.fetch_all()

for i, rr in enumerate(resonators):
    # I = fetched_data[4 * i]
    # Q = fetched_data[4 * i + 1]
    I_avg = fetched_data[4 * i]
    Q_avg = fetched_data[4 * i + 1]
    s1 = fetched_data[4 * i + 2]
    s2 = fetched_data[4 * i + 3]
    
    # assert np.array_equal(I, I_avg)
    # assert np.array_equal(Q, Q_avg)
    assert len(I_avg) == len(frequencies)
    assert len(Q_avg) == len(frequencies)
    assert np.array_equal(I_avg, np.ones(len(frequencies)))
    assert np.array_equal(Q_avg, -np.ones(len(frequencies)))
    assert np.array_equal(s1, np.ones(len(frequencies)))
    assert np.array_equal(s2, np.zeros(len(frequencies)))

print("success! buffer, average, map(FUNCTIONS.average(), boolean_to_int")

# %%
