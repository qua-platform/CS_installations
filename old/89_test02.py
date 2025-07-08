from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from configuration_with_opxplus import *
from qualang_tools.results import (
    progress_counter,
    fetching_tool,
    wait_until_job_is_paused,
)
from qualang_tools.plot import interrupt_on_close
from qualang_tools.addons.variables import assign_variables_to_element
from qdac2_driver import QDACII, load_voltage_list
import matplotlib.pyplot as plt
from macros import RF_reflectometry_macro
import matplotlib
from qm import generate_qua_script

import os
import sys
from pprint import pprint
from time import sleep
from time import time
import matplotlib.pyplot as plt
import numpy as np
import pyvisa
import xarray as xr
from tqdm import tqdm
from lmfit import Model
from matplotlib.colors import LogNorm
import winsound
import datetime

sys.path.append(os.path.join(os.path.abspath(''), '..'))
from instruments.qdac_ryu import Qdac2 as QDAC
from scripts.station import Station
import scripts.measurementroutines as mr

matplotlib.use('TkAgg')
### Utils
if not 'log_input' in globals().keys():
    log_input = dict()

def print_datetime():
    print('\33[4mExcecuted ' + str(datetime.datetime.now()).split('.')[0] + '\033[0m')

def today():
    return datetime.datetime.today().strftime('%Y%m%d')[2:]

def now():
    return datetime.datetime.now().strftime('%Y%m%d%H%M')[2:]
###


print_datetime()
print(f"{sampling_rate/1e9}GHz")
print(f"{reflectometry_readout_amp}V")
print(f"{resonator_IF/1e6}MHz")
print(f"{reflectometry_readout_length/1e3}us")
print(f"{reflectometry_readout_long_length/1e6}ms")

print_all_voltage()
###################
# The QUA program #
###################
total_duration = 60 * 60 * u.s

sub_duration = 5 * u.s
num_outer = total_duration // sub_duration  # Number of averaging loops

with program() as reflectometry_spectro:
    m = declare(int)  # QUA variable for the averaging loop
    n = declare(int)  # QUA variable for the averaging loop
    I = declare(fixed)  # QUA variable for the measured 'I' quadrature
    Q = declare(fixed)  # QUA variable for the measured 'Q' quadrature
    n_st = declare_stream()  # Stream for the averaging iteration 'n'
    I_st = declare_stream()  # Stream for the 'I' quadrature
    Q_st = declare_stream()  # Stream for the 'Q' quadrature

    with for_(n, 0, n < num_outer, n + 1):
        # RF reflectometry: the voltage measured by the analog input 2 is recorded, demodulated at the readout
        # Please choose the right "out1" or "out2" according to the connectivity
        measure(
            # "long_readout_trimmed",
            "readout",
            # "long_readout",
            "tank_circuit",
            None,
            demod.full("cos", I, "out1"),
            demod.full("sin", Q, "out1"),
        )

        
        save(I, I_st)
        save(Q, Q_st)

        pause()

        wait(5 *u.s)  
        save(n, n_st)

    with stream_processing():
        I_st.buffer(num_outer).save("I")
        Q_st.buffer(num_outer).save("Q")
        # I_st.buffer(num_inner).save_all("I_all")
        # Q_st.buffer(num_inner).save_all("Q_all")
        n_st.save("iteration")

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(
    host=qop_ip, port=qop_port, cluster_name=cluster_name
)


#######################
# Simulate or execute #
#######################
simulate = False
save_data = True
qm = None

def solve_for_voltage(amplitude, A, gamma, Vpeak, B):
    # 安全性チェック
    if amplitude <= B or amplitude >= A + B:
        raise ValueError("amplitude must be between B and A + B for real solution")

    inside_sqrt = A / (amplitude - B)
    arccosh_arg = np.sqrt(inside_sqrt)
    delta = np.arccosh(arccosh_arg) / gamma

    # 2つの解（対称性により ±）
    # V1 = Vpeak + delta
    V2 = Vpeak - delta

    return V2

try:
    if simulate:
        # Simulates the QUA program for the specified duration
        simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
        # Simulate blocks python until the simulation is done
        job = qmm.simulate(config, reflectometry_spectro, simulation_config)
        # Plot the simulated samples
        job.get_simulated_samples().con1.plot()
        plt.show()

    else:
        # Open the quantum machine
        qm = qmm.open_qm(config)
        # Send the QUA program to the OPX, which compiles and executes it
        job = qm.execute(reflectometry_spectro)

        for z in tqdm(range(num_outer)):
            if z == 0:
                results = fetching_tool(job, data_list=["I", "Q", "iteration"], mode="live")
            I, Q, iteration = results.fetch_all()
            I = I[z] / 2**12
            Q = Q[z] / 2**12
            amplitude = np.sqrt(I**2 + Q**2)

            V_change = solve_for_voltage(amplitude=amplitude, A=1.0382e-4, gamma=451.233302, Vpeak=2.040795, B=9.313e-5)
            if V_change < 2.035 and V_change > 2.040795:
                raise ValueError("Outside the voltage range!")

            s.v_LDG.voltage = V_change # Feedback voltage
            print(f'{V_change}V')


            # s.v_LDG.voltage = 2.039
            job.resume()

            if z + 1 == num_outer:
                break

            # Wait until the program reaches the 'pause' statement again, indicating that the QUA program is done
            wait_until_job_is_paused(job)
            
        # results = fetching_tool(job, data_list=["I", "Q", "I_all", "Q_all", "iteration"], mode="live")
        results = fetching_tool(job, data_list=["I", "Q", "iteration"], mode="live")
        
        # Live plotting
        fig = plt.figure()
        interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
        while results.is_processing():
            # Fetch results
            I, Q, iteration = results.fetch_all()

        if save_data:
            from qualang_tools.results.data_handler import DataHandler

            # Save results
            script_name = "meas_Genbu_20250522_w_OPX.ipynb"  # 実際のNotebook名に変更
            data_handler = DataHandler(root_data_folder=save_dir)
            data_handler.create_data_folder(name="monitoring_reflectometry_feedback")

            # Data to save
            save_data_dict = {}
            # save_data_dict["elapsed_time"] =  np.array([elapsed_time])
            save_data_dict["I"] = I
            save_data_dict["Q"] = Q
            # save_data_dict["time"] = ts_s

            # Save results
            save_data_dict.update({"fig_live": fig})
            data_handler.additional_files = {
                script_name: script_name,
                **default_additional_files,
            }
            data_handler.save_data(data=save_data_dict)
finally:
    if qm is not None:
        qm.close()
    winsound.Beep(2000, 500)