# %%
import matplotlib.pyplot as plt
import numpy as np
from qm import CompilerOptionArguments, QuantumMachinesManager, SimulationConfig
from qm.qua import *
from qualang_tools.results import fetching_tool, progress_counter
from qualang_tools.loops.loops import from_array
from qualang_tools.units import unit
from qua_config.configuraiton_cluster4_3chassis_8fems422_band1 import *


##################
#   Parameters   #
##################

# qubits = get_all_elements("qubit")
# qubits = get_elements("qubit", cons=["con1", "con2"], fems=[1, 2], ports=[2, 7])
# resonators = get_elements("resonator", cons=["con1", "con2", "con3"], fems=[1, 2, 3, 4], ports=[1, 8])
resonators = get_elements("resonator", cons=["con1"], fems=[1], ports=[1, 8])
# jpas = get_elements("jpa", cons="con3", fems=[1, 2], ports=7)
print_elements_ports(resonators)


n_shots = 10


###################
# The QUA program #
###################
##################
#      QUA       #
##################


with program() as PROG:
    n = declare(int)
    m = declare(int)
    I = [declare(fixed) for _ in range(len(resonators))]
    Q = [declare(fixed) for _ in range(len(resonators))]
    I_st = [declare_stream() for _ in range(len(resonators))]
    Q_st = [declare_stream() for _ in range(len(resonators))]

    with for_(n, 0, n < n_shots, n + 1):
        
        for i, rr in enumerate(resonators):
            measure(
                "readout",
                rr,
                dual_demod.full("cos", "sin", I[i]),
                dual_demod.full("minus_sin", "cos", Q[i]),
            )
            wait(250, rr)
            save(I[i], I_st[i])
            save(Q[i], Q_st[i])
        
        pause()

    with stream_processing():
        for i, rr in enumerate(resonators):
            I_st[i].save_all(f"I_{rr}")
            Q_st[i].save_all(f"Q_{rr}")


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

fetch_names = []
for rr in resonators:
    fetch_names.append(f"I_{rr}")
    fetch_names.append(f"Q_{rr}")


ress = []
for _n in range(n_shots):
    # Fetch Data by chunk
    if job.is_paused():
        # Wait until the program reaches the 'pause' statement again, indicating that the QUA program is done
        if _n == 0:
            print("get a fetching tool")
            results = fetching_tool(job, data_list=fetch_names, mode="live")

        # Fetch results
        print(f"fetch result! {_n}")
        fetched_data = results.fetch_all()
        ress.append(fetched_data)

        # Resume
        print(f"---> fetched and resuming! {_n}")
        job.resume()

# Fetch all the data
fetched_data = results.fetch_all()

nsqrt = int(np.ceil(np.sqrt(len(resonators))))
if (nsqrt - 1) * nsqrt >= len(resonators):
    ncols, nrows = nsqrt - 1, nsqrt
else:
    ncols, nrows = nsqrt, nsqrt

fig, axss = plt.subplots(ncols, nrows, figsize=(3 * nrows, 3 * ncols), sharex=True, sharey=True)
for i, (ax, rr) in enumerate(zip(axss.ravel(), resonators)):
    x = fetched_data[2 * i].mean()
    y = fetched_data[2 * i + 1].mean()
    v_max = max(abs(x), abs(y))
    ax.set_title(rr)
    ax.vlines(x=0, ymin=-1.2 * v_max, ymax=+1.2 * v_max, color='k', alpha=0.2)
    ax.hlines(y=0, xmin=-1.2 * v_max, xmax=+1.2 * v_max, color='k', alpha=0.2)
    ax.scatter(x=x, y=y, c='r')
    ax.set_xlim([-1.2 * v_max, 1.2 * v_max])
    ax.set_ylim([-1.2 * v_max, 1.2 * v_max])
    ax.set_xlabel("I [V]") if i // nrows == ncols - 1 else None
    ax.set_ylabel("Q [V]") if i % nrows == 0 else None
plt.tight_layout()
plt.show()


# %%