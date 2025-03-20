# %%
from qm import QuantumMachinesManager, SimulationConfig
from qm.qua import *
from qualang_tools.units import unit
from qua_config.configuraiton_cluster1_1chassis_2fems2 import *


##################
#   Parameters   #
##################

duc = 1
qubits = get_all_elements("qubit", duc=duc)
# qubits = get_elements("qubit", cons=["con3"], fems=[1, 2], ports=[2, 7], duc=duc)

print_elements_ports(qubits)

# The keyword "band" refers to the following frequency bands:
#   1: (50 MHz - 5.5 GHz)
#   2: (4.5 GHz - 7.5 GHz)
#   3: (6.5 GHz - 10.5 GHz)
# The keyword "full_scale_power_dbm" is the maximum power of
# normalized pulse waveforms in [-1,1]. To convert to voltage,
#   power_mw = 10**(full_scale_power_dbm / 10)
#   max_voltage_amp = np.sqrt(2 * power_mw * 50 / 1000)
#   amp_in_volts = waveform * max_voltage_amp
#   ^ equivalent to OPX+ amp
# Its range is -41dBm to +10dBm with 3dBm steps.

band = 2
duc1 = 1
duc2 = 2
full_scale_power_dbm = 7
amplitude = 0.0625
freq_lo1 = 5.0 * u.GHz # IF = 50 * u.MHz
freq_lo2 = 7.0 * u.GHz # IF = 50 * u.MHz
out_port = 8

for con, con_val in config["controllers"].items():
    for fem, fem_val in con_val["fems"].items():
        for ao, ao_val in fem_val["analog_outputs"].items():
            ao_val["band"] = band
            ao_val["full_scale_power_dbm"] = full_scale_power_dbm
            ao_val["upconverters"][duc1]["frequency"] = freq_lo1
            ao_val["upconverters"][duc2]["frequency"] = freq_lo2
config["waveforms"]["const_wf"]["sample"] = amplitude

for qb, qb_val in config["elements"].items():
    if qb.startswith("qubit") and qb.endswith("duc1"):
        con, fem, port, duc = qb.split("_")[-1].split("-")
        fem = int(fem[3:])
        port = int(port[4:])
        qb_val["MWInput"]["port"] = (con, fem, out_port)
        if port <= 4:
            freq_lo = freq_lo1
            qb_val["MWInput"]["upconverter"] = duc1
            qb_val["intermediate_frequency"] = (-375 + (port - 1) * 250) * u.MHz
        else:
            freq_lo = freq_lo2
            qb_val["MWInput"]["upconverter"] = duc2
            qb_val["intermediate_frequency"] = (-375 + (port - 5) * 250) * u.MHz
        
        # qb_val["intermediate_frequency"] = -(25 + (port - 1) * 50) * u.MHz
        print(qb, f'({con}, {fem}, {port} -> 1)', (freq_lo + qb_val["intermediate_frequency"])/u.GHz)
        

##################
#      QUA       #
##################


with program() as PROG:

    with infinite_loop_():
        for qb in qubits:
            play("const", qb)


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


# Save files
from qualang_tools.results.data_handler import DataHandler
script_name = Path(__file__).name
data_handler = DataHandler(root_data_folder=save_dir)
data_handler.additional_files = {script_name: script_name, debug_filepath: debug_filepath, **default_additional_files}
data_handler.save_data(data={"config": config}, name=script_name.replace(".py", ""))


######################################
#  Fetch & Analysis & Visualization  #
######################################



# %%
