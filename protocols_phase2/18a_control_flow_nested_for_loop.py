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

# resonators = get_elements("resonator", cons=["con1", "con2", "con3"], fems=[1, 2, 3, 4], ports=[1, 8])
# jpas = get_elements("jpa", cons="con3", fems=[1, 2], ports=7)


# pick an specified rr
resonators = get_elements("resonator", cons=["con1", "con2", "con3"], fems=[1, 2, 3, 4], ports=[1, 8])
qubits = get_elements("qubit", cons=["con1", "con2", "con3"], fems=[1, 2, 3, 4], ports=[2, 3, 4, 5, 6, 7])


print_elements_ports(qubits + resonators)

n_avg = 50
frequencies = np.arange(0, 100, 1) * u.MHz

##################
#      QUA       #
##################


with program() as PROG:

    f = declare(int)
    n = declare(int)
    I = [declare(fixed) for _ in range(len(resonators))]
    Q = [declare(fixed) for _ in range(len(resonators))]
    I_st = [declare_stream() for _ in range(len(resonators))]
    Q_st = [declare_stream() for _ in range(len(resonators))]

    with for_(n, 0, n < n_avg, n+1):

        with for_(*from_array(f, frequencies)):

            for i, rr in enumerate(resonators):

                update_frequency(rr, f)

                measure(
                    "readout",
                    rr,
                    dual_demod.full("cos", "sin", I[i]),
                    dual_demod.full("minus_sin", "cos", Q[i]),
                )
                wait(250, rr)

                save(I[i], I_st[i])
                save(Q[i], Q_st[i])

    with stream_processing():
        for i, rr in enumerate(resonators):
            I_st[i].buffer(len(frequencies)).average().save(f"I_{rr}")
            Q_st[i].buffer(len(frequencies)).average().save(f"Q_{rr}")


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
for i, rr in enumerate(resonators):
    data.append(f"I_{rr}")
    data.append(f"Q_{rr}")

results = fetching_tool(job, data_list=data)

fetched_data = results.fetch_all()

nsqrt = int(np.ceil(np.sqrt(len(resonators))))
if (nsqrt - 1) * nsqrt >= len(resonators):
    ncols, nrows = nsqrt - 1, nsqrt
else:
    ncols, nrows = nsqrt, nsqrt

fig, axss = plt.subplots(ncols, nrows, figsize=(3 * nrows, 3 * ncols), squeeze=False)
for i, (ax, rr) in enumerate(zip(axss.ravel(), resonators)):
    I = fetched_data[2 * i]
    Q = fetched_data[2 * i + 1]
    assert I.shape == frequencies.shape
    assert Q.shape == frequencies.shape
    ax.set_title(rr)
    ax.plot(frequencies / u.MHz, I)
    ax.plot(frequencies / u.MHz, Q)
    ax.set_xlabel("Frequencies [MHz]") if i // nrows == ncols - 1 else None
    ax.set_ylabel("Voltage [V]") if i % nrows == 0 else None
plt.tight_layout()
plt.show()

# %%