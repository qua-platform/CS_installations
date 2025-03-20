# %%
import matplotlib.pyplot as plt
import numpy as np
from qm import QuantumMachinesManager, SimulationConfig
from qm.qua import *
from qualang_tools.results.results import fetching_tool
from qualang_tools.units import unit
from qua_config.configuraiton_cluster4_3chassis_8fems422_band1 import *


#####################
#       Utils       #
#####################

# resonators = get_all_elements("qubit")
# resonators = get_elements("qubit", cons=["con1", "con2"], fems=[1, 2], ports=[2, 7])
resonators = get_elements("resonator", cons=["con1", "con2", "con3"], fems=[1, 2, 3, 4], ports=[1, 8])
# jpas = get_elements("jpa", cons="con3", fems=[1, 2], ports=7)
print_elements_ports(resonators)


n_avg = 100  # number of averages
# Set maximum readout duration for this scan and update the configuration accordingly
readout_len = 1 * u.us  # Readout pulse duration
update_readout_length(readout_len, resonators)
# Set the sliced demod parameters
division_length = 10  # Size of each demodulation slice in clock cycles
number_of_divisions = int(readout_len / (4 * division_length))  # Number of slices
assert (4 * division_length) * number_of_divisions == readout_len
print("Integration weights chunk-size length in clock cycles:", division_length)
print("The readout has been sliced in the following number of divisions", number_of_divisions)

# Time axis for the plots at the end
x_plot = np.arange(division_length * 4, readout_len + 1, division_length * 4)


##################
#      QUA       #
##################


with program() as PROG:
    n = declare(int)
    ind = declare(int)
    II = [declare(fixed, size=number_of_divisions) for _ in range(len(resonators))]
    IQ = [declare(fixed, size=number_of_divisions) for _ in range(len(resonators))]
    QI = [declare(fixed, size=number_of_divisions) for _ in range(len(resonators))]
    QQ = [declare(fixed, size=number_of_divisions) for _ in range(len(resonators))]

    n_st = declare_stream()
    II_st = [declare_stream() for _ in range(len(resonators))]
    IQ_st = [declare_stream() for _ in range(len(resonators))]
    QI_st = [declare_stream() for _ in range(len(resonators))]
    QQ_st = [declare_stream() for _ in range(len(resonators))]

    with for_(n, 0, n < n_avg, n + 1):

        for i, rr in enumerate(resonators):

            measure(
                "readout",
                rr,
                demod.sliced("cos", II[i], division_length, "out1"),
                demod.sliced("minus_sin", IQ[i], division_length, "out2"),
                demod.sliced("sin", QI[i], division_length, "out1"),
                demod.sliced("cos", QQ[i], division_length, "out2"),
            )
            # Save the sliced data (time trace of the demodulated data with a resolution equals to the division length)
            with for_(ind, 0, ind < number_of_divisions, ind + 1):
                save(II[i][ind], II_st[i])
                save(IQ[i][ind], IQ_st[i])
                save(QI[i][ind], QI_st[i])
                save(QQ[i][ind], QQ_st[i])
            wait(250, rr)
            align()

    with stream_processing():
        for i, rr in enumerate(resonators):
            II_st[i].buffer(number_of_divisions).average().save(f"II_{rr}")
            IQ_st[i].buffer(number_of_divisions).average().save(f"IQ_{rr}")
            QI_st[i].buffer(number_of_divisions).average().save(f"QI_{rr}")
            QQ_st[i].buffer(number_of_divisions).average().save(f"QQ_{rr}")


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


fetch_names = []
for rr in resonators:
    fetch_names.extend([
        f"II_{rr}",
        f"IQ_{rr}",
        f"QI_{rr}",
        f"QQ_{rr}",
    ])

results = fetching_tool(job, data_list=fetch_names)
fetched_data = results.fetch_all()

nsqrt = int(np.ceil(np.sqrt(len(resonators))))
if (nsqrt - 1) * nsqrt >= len(resonators):
    ncols, nrows = nsqrt - 1, nsqrt
else:
    ncols, nrows = nsqrt, nsqrt

fig, axss = plt.subplots(ncols, nrows, figsize=(3 * nrows, 3 * ncols))
for i, (ax, rr) in enumerate(zip(axss.ravel(), resonators)):
    II = fetched_data[2 * i]
    IQ = fetched_data[2 * i + 1]
    QI = fetched_data[2 * i + 2]
    QQ = fetched_data[2 * i + 3]
    # v_max = max(abs(x), abs(y))
    ax.set_title(rr)
    ax.plot(x_plot, II)
    ax.plot(x_plot, IQ)
    ax.plot(x_plot, QI)
    ax.plot(x_plot, QQ)
    ax.set_xlabel("time [ns]") if i // nrows == ncols - 1 else None
    ax.set_ylabel("signal [V]") if i % nrows == 0 else None
    ax.legend(["II", "IQ", "QI", "QQ"])
plt.tight_layout()
plt.show()


# %%