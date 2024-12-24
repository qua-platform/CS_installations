# %%
"""
        RF REFLECTOMETRY SPECTROSCOPY
The goal of this script is to perform the spectroscopy of the RF-reflectometry readout.
For this, the frequency of the element (pulser) used for reflectometry readout is being swept and the signal reflected
by the tank circuit is being acquired, demodulated and integrated by the OPX.

A global averaging is performed (averaging on the most outer loop) and the data is extracted while the program is running
to display the frequency response of the tank circuit with increasing SNR.

Prerequisites:
    - Connect the tank circuit to the corresponding output and input channels.

Before proceeding to the next node:
    - Update the config with the resonance frequency for reflectometry readout.
"""

from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from configuration_with_lf_fem import *
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.loops import from_array
import matplotlib.pyplot as plt
from scipy import signal
from datetime import datetime
from pathlib import Path
import copy
import matplotlib

from qdac2_driver import load_voltage_list

matplotlib.use('TkAgg')


###################
# The QUA program #
###################
# total_duration = 10 * 60 * 60 * u.s
# # total_duration = 120 * u.s
# num_elements = 2
# sub_duration_per_element = 30 * u.s
# sub_duration = num_elements * sub_duration_per_element
# reflectometry_readout_long_length = 0.5 * u.ms 
total_duration = 10 * 60 * 60 * u.us
# total_duration = 120 * u.s
num_elements = 2
sub_duration_per_element = 30 * u.us
sub_duration = num_elements * sub_duration_per_element
reflectometry_readout_long_length = 1 * u.us 
num_reps = total_duration // reflectometry_readout_long_length
num_outer = total_duration // sub_duration_per_element  # Number of averaging loops
num_inner = (
    sub_duration_per_element // reflectometry_readout_long_length
)  # Number of averaging loops
ts_s = np.arange(0, total_duration, reflectometry_readout_long_length)


with program() as reflectometry_spectro:
    m = declare(int)  # QUA variable for the averaging loop
    n = declare(int)  # QUA variable for the averaging loop
    I1 = declare(fixed)  # QUA variable for the measured 'I' quadrature
    Q1 = declare(fixed)  # QUA variable for the measured 'Q' quadrature
    I2 = declare(fixed)  # QUA variable for the measured 'I' quadrature
    Q2 = declare(fixed)  # QUA variable for the measured 'Q' quadrature
    n_st = declare_stream()  # Stream for the averaging iteration 'n'
    I_st = declare_stream()  # Stream for the 'I' quadrature
    Q_st = declare_stream()  # Stream for the 'Q' quadrature

    with for_(n, 0, n < num_outer, n + 1):
        with for_(m, 0, m < num_inner, m + 1):
            # RF reflectometry: the voltage measured by the analog input 2 is recorded, demodulated at the readout
            # Please choose the right "out1" or "out2" according to the connectivity

            # with for_(1..10):
            measure(
                "long_readout",
                "tank_circuit",
                None,
                demod.full("cos", I1, "out1"),
                demod.full("sin", Q1, "out1"),
            )
            save(I1, I_st)
            save(Q1, Q_st)
            wait(measurement_delay * u.ns)  # in ns

            wait(reflectometry_readout_long_length * u.ns, "tank_circuit_twin")
            
            measure(
                "long_readout",
                "tank_circuit_twin",
                None,
                demod.full("cos", I2, "out1"),
                demod.full("sin", Q2, "out1"),
            )
            save(I2, I_st)
            save(Q2, Q_st)
            # wait(1_000 * u.ns)  # in ns

            wait(reflectometry_readout_long_length * u.ns, "tank_circuit")
            
            # Please choose the right "out1" or "out2" according to the connectivity
            measure(
                "long_readout",
                "tank_circuit",
                None,
                demod.full("cos", I1, "out1"),
                demod.full("sin", Q1, "out1"),
            )
            save(I1, I_st)
            save(Q1, Q_st)
            # wait(1_000 * u.ns)  # in ns

            wait(reflectometry_readout_long_length * u.ns, "tank_circuit_twin")
            
            measure(
                "long_readout",
                "tank_circuit_twin",
                None,
                demod.full("cos", I2, "out1"),
                demod.full("sin", Q2, "out1"),
            )
            save(I2, I_st)
            save(Q2, Q_st)
            # wait(1_000 * u.ns)  # in ns

        save(n, n_st)
        # wait(1_000 * u.ns)  # in ns

    with stream_processing():
        I_st.buffer(num_elements * num_inner).save("I")
        Q_st.buffer(num_elements * num_inner).save("Q")
        n_st.save("iteration")

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(
    host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config
)

import pyvisa
rm = pyvisa.ResourceManager('')
qdac = rm.open_resource('ASRL7::INSTR')

# set up other DC voltages
load_voltage_list(
    qdac,
    channel=15,
    dwell=2e-6,
    slew_rate=10,
    trigger_port=None,
    output_range="High",
    output_filter="med",
    voltage_list=[3],
)
load_voltage_list(
    qdac,
    channel=21,
    dwell=2e-6,
    slew_rate=10,
    trigger_port=None,
    output_range="High",
    output_filter="med",
    voltage_list=[3],
)
load_voltage_list(
    qdac,
    channel=24,
    dwell=2e-6,
    slew_rate=10,
    trigger_port=None,
    output_range="High",
    output_filter="med",
    voltage_list=[3],
)
load_voltage_list(
    qdac,
    channel=7,
    dwell=2e-6,
    slew_rate=10,
    trigger_port=None,
    output_range="High",
    output_filter="med",
    voltage_list=[0.45],
)
# P left
load_voltage_list(
    qdac,
    channel=19,
    dwell=2e-6,
    slew_rate=10,
    trigger_port=None,
    output_range="High",
    output_filter="med",
    voltage_list=[0.12],
)

# center barrier gate
load_voltage_list(
    qdac,
    channel=3,
    dwell=2e-6,
    slew_rate=10,
    trigger_port=None,
    output_range="High",
    output_filter="med",
    voltage_list=[0.38],
)

# P right
load_voltage_list(
    qdac,
    channel=1,
    dwell=2e-6,
    slew_rate=10,
    trigger_port=None,
    output_range="High",
    output_filter="med",
    voltage_list=[0.2],
)

load_voltage_list(
    qdac,
    channel=5,
    dwell=2e-6,
    slew_rate=10,
    trigger_port=None,
    output_range="High",
    output_filter="med",
    voltage_list=[0.35],
)
load_voltage_list(
    qdac,
    channel=2,
    dwell=2e-6,
    slew_rate=10,
    trigger_port=None,
    output_range="High",
    output_filter="med",
    voltage_list=[3],
)


#######################
# Simulate or execute #
#######################
simulate = True
save_data = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=3_000)  # In clock cycles = 4ns
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

    # make a temporal directory for the data
    if save_data:
        from qualang_tools.results.data_handler import DataHandler

        # Save results
        script_name = Path(__file__).name
        data_handler = DataHandler(root_data_folder=save_dir)
        data_handler.create_data_folder(name="monitoring_reflectometry")

    # results = fetching_tool(job, data_list=["I", "Q", "I_all", "Q_all", "iteration"], mode="live")
    results = fetching_tool(job, data_list=["I", "Q", "iteration"], mode="live")
    Is, Qs = [], []
    _I, _Q = np.zeros(num_elements * num_inner), np.zeros(num_elements * num_inner)
    do_plot = 0
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    while results.is_processing():
        # Fetch results
        I, Q, iteration = results.fetch_all()

        # Progress bar
        progress_counter(iteration, num_outer, start_time=results.get_start_time())

        if not np.allclose(I, _I):
            Is.append(I)
            _I = copy.deepcopy(I)
            I_flat = np.array(Is).ravel()
            ts_I = np.arange(I_flat.shape[0]) * (reflectometry_readout_long_length / u.s)

        if not np.allclose(Q, _Q):
            Qs.append(Q)
            _Q = copy.deepcopy(Q)
            Q_flat = np.array(Qs).ravel()
            ts_Q = np.arange(Q_flat.shape[0]) * (reflectometry_readout_long_length / u.s)

        # Print log
        current_datetime = datetime.now().strftime("%Y/%m/%d-%H:%M:%S")
        _log_this = f"{current_datetime}, len-I={I_flat.shape[0]:_}, len-Q={Q_flat.shape[0]:_}, iteration={iteration+1}"
        print(_log_this)

        # Save log
        if save_data:
            # Open the log file in append mode and write the log
            with open(data_handler.path / "log.txt", encoding="utf8", mode="a") as f:
                f.write(
                    _log_this.replace("_", "") + "\n"
                )  # Append the log message to the file

            # Data to save
            np.savez(
                file = data_handler.path / "data.npz",
                I = I_flat,
                Q = Q_flat,
            )
            # save_data_dict = {}
            # save_data_dict["I"] = I_flat
            # save_data_dict["Q"] = Q_flat
            # data_handler.save_data(data=save_data_dict, node_contents=None)

        if do_plot % 15 == 0:
            # Plot results
            plt.suptitle("RF-reflectometry")
            plt.subplot(211)
            plt.cla()
            plt.plot(ts_I, I_flat)
            plt.xlabel("Time [sec]")
            plt.ylabel("I Voltage [V]")
            plt.subplot(212)
            plt.cla()
            plt.plot(ts_Q, Q_flat)
            plt.xlabel("Time [sec]")
            plt.ylabel("Q Voltage [V]")
            plt.tight_layout()
        do_plot += 1
        plt.pause(2)


    if save_data:
        from qualang_tools.results.data_handler import DataHandler

        # Data to save
        save_data_dict = {}
        # save_data_dict["elapsed_time"] =  np.array([elapsed_time])
        save_data_dict["I"] = I_flat
        save_data_dict["Q"] = Q_flat

        # Save results
        save_data_dict.update({"fig_live": fig})
        data_handler.additional_files = {
            script_name: script_name,
            **default_additional_files,
        }
        data_handler.save_data(data=save_data_dict)

    # plt.show()
    qm.close()

# %%
