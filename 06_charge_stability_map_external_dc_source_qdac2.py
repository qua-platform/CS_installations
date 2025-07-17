# %%
"""
        CHARGE STABILITY MAP - fast and slow axes: QDAC2 set to trigger mode
The goal of the script is to acquire the charge stability map.
Here two channels of the QDAC2 are parametrized to step though two preloaded voltage lists on the event of two digital
markers provided by the OPX (connected to ext1 and ext2). This method allows the fast acquisition of a 2D voltage map
and the data can be fetched from the OPX in real time to enable live plotting.
The speed can also be further improved by removing the live plotting and increasing the QDAC2 bandwidth.

The QUA program consists in sending the triggers to the QDAC2 to increment the voltages and measure the charge of the dot
AC lines.


A global average is performed (averaging on the most outer loop) and the data is extracted while the program is running
to display the full charge stability map with increasing SNR.

Prerequisites:
      QDAC2 external trigger ports.

    - (optional) Connect the OPX to the fast line of the plunger gates for playing the Coulomb pulse and calibrate the
      lever arm.

Before proceeding to the next node:
    - Identify the different charge occupation regions.
    - Update the config with the lever-arms.pyvisa_py
"""

from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from configuration_with_mwfem_lffem import *
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

sys.path.append(os.path.join(os.path.abspath(""), ".."))
from instruments.qdac_ryu import Qdac2 as QDAC
from scripts.station import Station
import scripts.measurementroutines as mr

matplotlib.use("TkAgg")
### Utils
if not "log_input" in globals().keys():
    log_input = dict()


def print_datetime():
    print("\33[4mExcecuted " + str(datetime.datetime.now()).split(".")[0] + "\033[0m")


def today():
    return datetime.datetime.today().strftime("%Y%m%d")[2:]


def now():
    return datetime.datetime.now().strftime("%Y%m%d%H%M")[2:]


###


###################
# The QUA program #
###################
n_avg = 1  # Number of averages
n_points_slow = 101  # Number of points for the slow axis
n_points_fast = 101  # Number of points for the fast axis
n_points_z = 1
Coulomb_amp = 0.0  # amplitude of the Coulomb pulse
slew_rate = 10
# How many Coulomb pulse periods to last the whole program
N = (
    (int((reflectometry_readout_length + 1_000) / (2 * step_length)) + 1)
    * n_points_fast
    * n_points_slow
    * n_avg
)

# Voltages in Volt
# voltage_values_right = np.linspace(0.05, 0.25, n_points_right)
# voltage_values_left = np.linspace(0.1, 0.3, n_points_left)

# voltage_values_right = np.linspace(0.2, 0.23, n_points_right)
# voltage_values_right = np.linspace(0.2, 0.21, n_points_right)
# voltage_values_right = np.linspace(0, 0.50, n_points_right)
# voltage_values_slow = np.linspace(1.350, 1.400, n_points_slow)
voltage_values_slow = np.linspace(1.25, 1.75, n_points_slow)
# voltage_values_slow = np.linspace(2.55, 2.75, n_points_slow)

# voltage_values_left = np.linspace(0.11, 0.14, n_points_left)
# voltage_values_left = np.linspace(0.115, 0.125, n_points_left)
# voltage_values_left = np.linspace(0, 0.50, n_points_left)
# voltage_values_fast = np.linspace(1.425, 1.475, n_points_fast)
voltage_values_fast = np.linspace(0.5, 1.5, n_points_fast)
# voltage_values_fast = np.linspace(2.35, 2.55, n_points_fast)

# voltage_values_z = np.linspace(1.0, 3.0, n_points_z)
voltage_values_z = [0]


vals_max = np.max(voltage_values_fast)
vals_min = np.min(voltage_values_fast)
wait_time_fast = int(np.ceil(1000 * np.abs((vals_max - vals_min)) / slew_rate * 5))
print(f"wait_time_fast = {wait_time_fast} ms")

wait_time_step = (
    1000 * (np.abs(voltage_values_fast[1] - voltage_values_fast[0])) / slew_rate * 5
)
wait_time_step = int(np.ceil(max(wait_time_step, 10)))
print(f"wait_time_step = {wait_time_step} ms")

with program() as charge_stability_prog:
    n = declare(int)  # QUA integer used as an index for the averaging loop
    counter = declare(int)  # QUA integer used as an index for the Coulomb pulse
    i = declare(int)  # QUA integer used as an index to loop over the voltage points
    j = declare(int)  # QUA integer used as an index to loop over the voltage points
    k = declare(int)
    m = declare(int)
    n_st = declare_stream()  # Stream for the iteration number (progress bar)
    I = declare(fixed)
    Q = declare(fixed)

    # Ensure that the result variables are assign to the pulse processor used for readout
    assign_variables_to_element("tank_circuit", I, Q)
    # # Play the Coulomb pulse continuously for the whole sequence
    # #      ____      ____      ____      ____
    # #     |    |    |    |    |    |    |    |
    # # ____|    |____|    |____|    |____|    |...
    # with for_(counter, 0, counter < N, counter + 1):
    #     # The Coulomb pulse
    #     play("step" * amp(Coulomb_amp / P1_step_amp), "P1")
    #     play("step" * amp(-Coulomb_amp / P1_step_amp), "P1")

    # 20250427
    with for_(k, 0, k < n_points_z, k + 1):
        with for_(j, 0, j < n_points_slow, j + 1):
            # Trigger the QDAC2 channel to output the next voltage level from the list
            # wait(1 * u.ms)
            with for_(i, 0, i < n_points_fast, i + 1):
                # Trigger the QDAC2 channel to output the next voltage level from the list
                pause()

                wait(10 * u.ms)

                with for_(n, 0, n < n_avg, n + 1):  # The averaging loop
                    # RF reflectometry: the voltage measured by the analog input 2 is recorded, demodulated at the readout
                    # frequency and the integrated quadratures are stored in "I" and "Q"

                    I, Q, I_st, Q_st = RF_reflectometry_macro(
                        operation="long_readout", I=I, Q=Q
                    )
                    wait(5 * u.us)  # in ns

                # wait(10 * u.ms)  # in ns
            # Save the LO iteration to get the progress ba
            assign(m, k * n_points_slow + j)
            save(m, n_st)

    # Stream processing section used to process the data before saving it.
    with stream_processing():
        n_st.save("iteration")
        # Cast the data into a 2D matrix and performs a global averaging of the received 2D matrices together.
        # RF reflectometry
        I_st.buffer(n_avg).map(FUNCTIONS.average()).buffer(n_points_fast).save_all("I")
        Q_st.buffer(n_avg).map(FUNCTIONS.average()).buffer(n_points_fast).save_all("Q")


# for vol_c in vol_center:
#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name)
sourceFile = open("debug.py", "w")
print(generate_qua_script(charge_stability_prog, config), file=sourceFile)
sourceFile.close()

##################################################################################
## QDAC2 section

###
rm = pyvisa.ResourceManager()
resources = rm.list_resources()
print(f"resources: {resources}")

print_datetime()
if not "s" in globals().keys():
    s = Station(fridge="Genbu", dut="None")

s.set_device(QDAC(addr="ASRL3::INSTR", name="QDACa", debug=False), name="daca")
s.set_device(QDAC(addr="ASRL4::INSTR", name="QDACb", debug=False), name="dacb")

gate_voltage_lim = [-5, 5]
ohmic_voltage_lim = [-5e-3, 5e-3]
gate_range = "HIGH"
ohmic_range = "LOW"
gate_slew_rate = 10  # V/s
ohmic_slew_rate = 1

s.set_channel(
    s.daca.ch01,
    ch_name="A1",
    voltage_limit=gate_voltage_lim,
    slew_rate=gate_slew_rate,
    voltage_range=gate_range,
)
s.set_channel(
    s.daca.ch02,
    ch_name="A2",
    voltage_limit=gate_voltage_lim,
    slew_rate=gate_slew_rate,
    voltage_range=gate_range,
)
s.set_channel(
    s.daca.ch03,
    ch_name="A3",
    voltage_limit=gate_voltage_lim,
    slew_rate=gate_slew_rate,
    voltage_range=gate_range,
)
s.set_channel(
    s.daca.ch04,
    ch_name="v_B4",
    voltage_limit=gate_voltage_lim,
    slew_rate=gate_slew_rate,
    voltage_range=gate_range,
)
s.set_channel(
    s.daca.ch05,
    ch_name="v_P4",
    voltage_limit=gate_voltage_lim,
    slew_rate=gate_slew_rate,
    voltage_range=gate_range,
)
# s.set_channel(s.daca.ch05, ch_name = 'v_RB1', voltage_limit = gate_voltage_lim, slew_rate = gate_slew_rate, voltage_range = gate_range)
s.set_channel(
    s.daca.ch06,
    ch_name="A6",
    voltage_limit=ohmic_voltage_lim,
    slew_rate=ohmic_slew_rate,
    voltage_range=ohmic_range,
)
s.set_channel(
    s.daca.ch07,
    ch_name="A7",
    voltage_limit=gate_voltage_lim,
    slew_rate=gate_slew_rate,
    voltage_range=gate_range,
)
s.set_channel(
    s.daca.ch08,
    ch_name="A8",
    voltage_limit=gate_voltage_lim,
    slew_rate=gate_slew_rate,
    voltage_range=gate_range,
)
s.set_channel(
    s.daca.ch09,
    ch_name="A9",
    voltage_limit=gate_voltage_lim,
    slew_rate=gate_slew_rate,
    voltage_range=gate_range,
)
s.set_channel(
    s.daca.ch10,
    ch_name="A10",
    voltage_limit=gate_voltage_lim,
    slew_rate=gate_slew_rate,
    voltage_range=gate_range,
)
s.set_channel(
    s.daca.ch11,
    ch_name="v_MWIN",
    voltage_limit=gate_voltage_lim,
    slew_rate=gate_slew_rate,
    voltage_range=gate_range,
)
s.set_channel(
    s.daca.ch12,
    ch_name="A12",
    voltage_limit=ohmic_voltage_lim,
    slew_rate=ohmic_slew_rate,
    voltage_range=ohmic_range,
)
s.set_channel(
    s.daca.ch13,
    ch_name="v_B3",
    voltage_limit=gate_voltage_lim,
    slew_rate=gate_slew_rate,
    voltage_range=gate_range,
)
s.set_channel(
    s.daca.ch14,
    ch_name="v_B5",
    voltage_limit=gate_voltage_lim,
    slew_rate=gate_slew_rate,
    voltage_range=gate_range,
)
s.set_channel(
    s.daca.ch15,
    ch_name="A15",
    voltage_limit=gate_voltage_lim,
    slew_rate=gate_slew_rate,
    voltage_range=gate_range,
)
s.set_channel(
    s.daca.ch16,
    ch_name="v_B1",
    voltage_limit=gate_voltage_lim,
    slew_rate=gate_slew_rate,
    voltage_range=gate_range,
)
s.set_channel(
    s.daca.ch17,
    ch_name="v_RDG",
    voltage_limit=gate_voltage_lim,
    slew_rate=gate_slew_rate,
    voltage_range=gate_range,
)
s.set_channel(
    s.daca.ch18,
    ch_name="v_RDN",
    voltage_limit=ohmic_voltage_lim,
    slew_rate=ohmic_slew_rate,
    voltage_range=ohmic_range,
)
s.set_channel(
    s.daca.ch19,
    ch_name="v_C2",
    voltage_limit=gate_voltage_lim,
    slew_rate=gate_slew_rate,
    voltage_range=gate_range,
)
s.set_channel(
    s.daca.ch20,
    ch_name="v_P1",
    voltage_limit=gate_voltage_lim,
    slew_rate=gate_slew_rate,
    voltage_range=gate_range,
)
s.set_channel(
    s.daca.ch21,
    ch_name="v_B2",
    voltage_limit=gate_voltage_lim,
    slew_rate=gate_slew_rate,
    voltage_range=gate_range,
)
s.set_channel(
    s.daca.ch22,
    ch_name="A22",
    voltage_limit=gate_voltage_lim,
    slew_rate=gate_slew_rate,
    voltage_range=gate_range,
)
s.set_channel(
    s.daca.ch23,
    ch_name="A23",
    voltage_limit=gate_voltage_lim,
    slew_rate=gate_slew_rate,
    voltage_range=gate_range,
)
s.set_channel(
    s.daca.ch24,
    ch_name="v_LDN",
    voltage_limit=ohmic_voltage_lim,
    slew_rate=ohmic_slew_rate,
    voltage_range=ohmic_range,
)

s.set_channel(
    s.dacb.ch01,
    ch_name="v_P2",
    voltage_limit=gate_voltage_lim,
    slew_rate=gate_slew_rate,
    voltage_range=gate_range,
)
s.set_channel(
    s.dacb.ch02,
    ch_name="v_LB2",
    voltage_limit=gate_voltage_lim,
    slew_rate=gate_slew_rate,
    voltage_range=gate_range,
)
s.set_channel(
    s.dacb.ch03,
    ch_name="B3",
    voltage_limit=gate_voltage_lim,
    slew_rate=gate_slew_rate,
    voltage_range=gate_range,
)
s.set_channel(
    s.dacb.ch04,
    ch_name="v_LDG",
    voltage_limit=gate_voltage_lim,
    slew_rate=gate_slew_rate,
    voltage_range=gate_range,
)
s.set_channel(
    s.dacb.ch05,
    ch_name="B5",
    voltage_limit=gate_voltage_lim,
    slew_rate=gate_slew_rate,
    voltage_range=gate_range,
)
s.set_channel(
    s.dacb.ch06,
    ch_name="v_RSN",
    voltage_limit=ohmic_voltage_lim,
    slew_rate=ohmic_slew_rate,
    voltage_range=ohmic_range,
)
s.set_channel(
    s.dacb.ch07,
    ch_name="B7",
    voltage_limit=gate_voltage_lim,
    slew_rate=gate_slew_rate,
    voltage_range=gate_range,
)
s.set_channel(
    s.dacb.ch08,
    ch_name="v_C1",
    voltage_limit=gate_voltage_lim,
    slew_rate=gate_slew_rate,
    voltage_range=gate_range,
)
s.set_channel(
    s.dacb.ch09,
    ch_name="v_LB1",
    voltage_limit=gate_voltage_lim,
    slew_rate=gate_slew_rate,
    voltage_range=gate_range,
)
s.set_channel(
    s.dacb.ch10,
    ch_name="B10",
    voltage_limit=gate_voltage_lim,
    slew_rate=gate_slew_rate,
    voltage_range=gate_range,
)
s.set_channel(
    s.dacb.ch11,
    ch_name="B11",
    voltage_limit=gate_voltage_lim,
    slew_rate=gate_slew_rate,
    voltage_range=gate_range,
)
s.set_channel(
    s.dacb.ch12,
    ch_name="v_LSN",
    voltage_limit=ohmic_voltage_lim,
    slew_rate=ohmic_slew_rate,
    voltage_range=ohmic_range,
)
s.set_channel(
    s.dacb.ch13,
    ch_name="v_MWOUT",
    voltage_limit=gate_voltage_lim,
    slew_rate=gate_slew_rate,
    voltage_range=gate_range,
)
s.set_channel(
    s.dacb.ch14,
    ch_name="B14",
    voltage_limit=gate_voltage_lim,
    slew_rate=gate_slew_rate,
    voltage_range=gate_range,
)
s.set_channel(
    s.dacb.ch15,
    ch_name="B15",
    voltage_limit=gate_voltage_lim,
    slew_rate=gate_slew_rate,
    voltage_range=gate_range,
)
s.set_channel(
    s.dacb.ch16,
    ch_name="B16",
    voltage_limit=gate_voltage_lim,
    slew_rate=gate_slew_rate,
    voltage_range=gate_range,
)
s.set_channel(
    s.dacb.ch17,
    ch_name="v_RSG",
    voltage_limit=gate_voltage_lim,
    slew_rate=gate_slew_rate,
    voltage_range=gate_range,
)
s.set_channel(
    s.dacb.ch18,
    ch_name="B18",
    voltage_limit=ohmic_voltage_lim,
    slew_rate=ohmic_slew_rate,
    voltage_range=ohmic_range,
)
s.set_channel(
    s.dacb.ch19,
    ch_name="v_P3",
    voltage_limit=gate_voltage_lim,
    slew_rate=gate_slew_rate,
    voltage_range=gate_range,
)
s.set_channel(
    s.dacb.ch20,
    ch_name="B20",
    voltage_limit=gate_voltage_lim,
    slew_rate=gate_slew_rate,
    voltage_range=gate_range,
)
s.set_channel(
    s.dacb.ch21,
    ch_name="v_RB2",
    voltage_limit=gate_voltage_lim,
    slew_rate=gate_slew_rate,
    voltage_range=gate_range,
)
s.set_channel(
    s.dacb.ch22,
    ch_name="v_RB1",
    voltage_limit=gate_voltage_lim,
    slew_rate=gate_slew_rate,
    voltage_range=gate_range,
)
# s.set_channel(s.dacb.ch22, ch_name = 'v_P4', voltage_limit = gate_voltage_lim, slew_rate = gate_slew_rate, voltage_range = gate_range)
s.set_channel(
    s.dacb.ch23,
    ch_name="B23",
    voltage_limit=gate_voltage_lim,
    slew_rate=gate_slew_rate,
    voltage_range=gate_range,
)
s.set_channel(
    s.dacb.ch24,
    ch_name="B24",
    voltage_limit=ohmic_voltage_lim,
    slew_rate=ohmic_slew_rate,
    voltage_range=ohmic_range,
)

s.daca.EXT1
s.daca.EXT2
s.daca.INT1
s.dacb.EXT1
s.dacb.EXT2
s.dacb.INT1

print(s.daca.errors())
print(s.dacb.errors())
###


print_datetime()
s.daca.reset_trigger()
s.dacb.reset_trigger()

s.v_LSN.voltage = 0
s.v_LDN.voltage = 0
s.v_RSN.voltage = 0
s.v_RDN.voltage = 0

s.v_LDG.voltage = 0
s.v_LB1.voltage = 0.0816
s.v_LB2.voltage = 0.1152

s.v_RDG.voltage = 0
s.v_RSG.voltage = 0
s.v_RB1.voltage = 0
s.v_RB2.voltage = 0

s.v_C1.voltage = 0
s.v_C2.voltage = 0
s.v_B5.voltage = 0
s.v_P4.voltage = 0
s.v_B4.voltage = 0
s.v_P3.voltage = 0
s.v_B3.voltage = 0
s.v_P2.voltage = 0
s.v_B2.voltage = 0
s.v_P1.voltage = 0
s.v_B1.voltage = 0

s.v_MWIN.voltage = 0
s.v_MWOUT.voltage = 0

##################################################################################

###########################
# Run or Simulate Program #
###########################
simulate = False
save_data = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=100_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, charge_stability_prog, simulation_config)
    job.get_simulated_samples().con1.plot()

else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(charge_stability_prog)
    # Get results from QUA program and initialize live plotting

    # Live plotting
    fig = plt.figure(figsize=(12, 6))
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    for z in range(n_points_z):
        # s.v_LDG.voltage = voltage_values_z[z]
        # s.daca.reset_trigger()
        # s.dacb.reset_trigger()
        s.v_B5.voltage = voltage_values_z[z]
        # sleep(0.5)
        for a in tqdm(range(n_points_slow)):
            # s.v_LB2.voltage = voltage_values_slow[a]
            # s.v_LB1.voltage = voltage_values_slow[a]
            # s.daca.reset_trigger()
            # s.dacb.reset_trigger()
            s.v_LDG.voltage = voltage_values_slow[a]
            # sleep(0.2)
            for b in range(n_points_fast):
                # s.v_LB1.voltage = voltage_values_fast[b]
                # s.v_LB2.voltage = voltage_values_fast[b]
                # s.daca.reset_trigger()
                # s.dacb.reset_trigger()
                s.v_P4.voltage = voltage_values_fast[b]

                print(f"z = {z}, a = {a}, b = {b}")
                print(
                    f"z = {s.v_B5.voltage}, a = {s.v_LDG.voltage}, b = {s.v_P4.voltage}"
                )

                # print("here 4")
                job.resume()

                if (
                    z + 1 == n_points_z
                    and a + 1 == n_points_slow
                    and b + 1 == n_points_fast
                ):
                    break

                # Wait until the program reaches the 'pause' statement again, indicating that the QUA program is done
                wait_until_job_is_paused(job)

            if b == 0 and k == 0:
                # Get results from QUA program and initialize live plotting
                results = fetching_tool(
                    job, data_list=["I", "Q", "iteration"], mode="live"
                )

            # Fetch the data from the last OPX run corresponding to the current slow axis iteration
            I, Q, iteration = results.fetch_all()
            print(f"I.shape = {I.shape}, Q.shape = {Q.shape}, iteration = {iteration}")
            m = I.shape[0] % n_points_slow or n_points_slow
            I_this = I[-m:, :]
            Q_this = Q[-m:, :]
            I_this = I_this.reshape(i + 1, n_points_fast)
            Q_this = Q_this.reshape(i + 1, n_points_fast)
            # Convert results into Volts
            S = u.demod2volts(
                I_this + 1j * Q_this,
                config["pulses"]["reflectometry_readout_long_pulse"]["length"],
            )
            R = np.abs(S)  # Amplitude
            phase = np.angle(S)  # Phase
            # Progress bar
            progress_counter(
                iteration, n_points_slow * n_points_z, start_time=results.start_time
            )
            # Plot data
            plt.subplot(121)
            plt.cla()
            plt.title(r"$R=\sqrt{I^2 + Q^2}$ [V]")
            plt.pcolor(voltage_values_fast, voltage_values_slow[:m], R)
            plt.xlabel("Fast voltage axis [V]")
            plt.ylabel("Slow voltage axis [V]")
            plt.colorbar()
            plt.subplot(122)
            plt.cla()
            plt.title("Phase [rad]")
            plt.pcolor(voltage_values_fast, voltage_values_slow[:m], phase)
            plt.xlabel("Fast voltage axis [V]")
            plt.ylabel("Slow voltage axis [V]")
            plt.colorbar()
            plt.tight_layout()
            plt.pause(1)

    I, Q, iteration = results.fetch_all()
    I = I.reshape(n_points_z, n_points_slow, n_points_fast)
    Q = Q.reshape(n_points_z, n_points_slow, n_points_fast)

    if save_data:
        from qualang_tools.results.data_handler import DataHandler

        # Data to save
        save_data_dict = {}
        # save_data_dict["elapsed_time"] =  np.array([elapsed_time])
        save_data_dict["I"] = I
        save_data_dict["Q"] = Q
        save_data_dict["S"] = S
        save_data_dict["x"] = voltage_values_fast
        save_data_dict["x_label"] = "Fast gate voltage"
        save_data_dict["x_unit"] = "V"
        save_data_dict["y"] = voltage_values_slow
        save_data_dict["y_label"] = "Slow gate voltage"
        save_data_dict["y_unit"] = "V"
        save_data_dict["z"] = voltage_values_z

        # Save results
        script_name = Path(__file__).name
        data_handler = DataHandler(root_data_folder=save_dir)
        save_data_dict.update({"fig_live": fig})
        data_handler.additional_files = {
            script_name: script_name,
            **default_additional_files,
        }
        data_handler.save_data(
            data=save_data_dict,
            name="charge_stability_map_with_no_trigger_qdac2"
            # data=save_data_dict, name=f'charge_stability_map_with_triggered_qdac2_{vol_c}'
        )

    # plt.show()
    s.dacb.all_voltages = 0
    s.daca.all_voltages = 0
    qm.close()
    winsound.Beep(2000, 500)

# %%
