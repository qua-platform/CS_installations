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

import copy
from datetime import datetime
from pathlib import Path

import matplotlib.pyplot as plt
from qm import QuantumMachinesManager, SimulationConfig
from qm.qua import *
from qualang_tools.loops import from_array
from qualang_tools.plot import interrupt_on_close

# from configuration import *
from qualang_tools.results import fetching_tool, progress_counter
from scipy import signal

from configuration_with_octave import *

###################
# The QUA program #
###################
# total_duration = 2 * 60 * 60 * u.s
total_duration = 30 * u.s
sub_duration = 10 * u.s
reflectometry_readout_long_length = 1 * u.ms
num_reps = total_duration // reflectometry_readout_long_length
num_outer = total_duration // sub_duration  # Number of averaging loops
num_inner = (
    sub_duration // reflectometry_readout_long_length
)  # Number of averaging loops
ts_s = np.arange(0, total_duration, reflectometry_readout_long_length)
config["pulses"]["reflectometry_readout_long_pulse"][
    "length"
] = reflectometry_readout_long_length


with program() as reflectometry_spectro:
    m = declare(int)  # QUA variable for the averaging loop
    n = declare(int)  # QUA variable for the averaging loop
    I = declare(fixed)  # QUA variable for the measured 'I' quadrature
    Q = declare(fixed)  # QUA variable for the measured 'Q' quadrature
    n_st = declare_stream()  # Stream for the averaging iteration 'n'
    I_st = declare_stream()  # Stream for the 'I' quadrature
    Q_st = declare_stream()  # Stream for the 'Q' quadrature

    with for_(n, 0, n < num_outer, n + 1):
        with for_(m, 0, m < num_inner, m + 1):
            # RF reflectometry: the voltage measured by the analog input 2 is recorded, demodulated at the readout
            # Please choose the right "out1" or "out2" according to the connectivity
            measure(
                "long_readout",
                "tank_circuit",
                None,
                demod.full("cos", I, "out1"),
                demod.full("sin", Q, "out1"),
            )
            save(I, I_st)
            save(Q, Q_st)
            wait(1_000 * u.ns)  # in ns

        save(n, n_st)
        wait(1_000 * u.ns)  # in ns

    with stream_processing():
        I_st.buffer(num_inner).save("I")
        Q_st.buffer(num_inner).save("Q")
        # I_st.buffer(num_inner).save_all("I_all")
        # Q_st.buffer(num_inner).save_all("Q_all")
        n_st.save("iteration")

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(
    host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config
)

#######################
# Simulate or execute #
#######################
simulate = False
save_data = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, reflectometry_spectro, simulation_config)
    # Plot the simulated samples
    job.get_simulated_samples().con1.plot()

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
    _I, _Q = np.zeros(num_inner), np.zeros(num_inner)
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
            ts_I = np.arange(I_flat.shape[0]) * reflectometry_readout_long_length / u.s

        if not np.allclose(Q, _Q):
            Qs.append(Q)
            _Q = copy.deepcopy(Q)
            Q_flat = np.array(Qs).ravel()
            ts_Q = np.arange(Q_flat.shape[0]) * reflectometry_readout_long_length / u.s

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
                file=data_handler.path / "data.npz",
                I=I_flat,
                Q=Q_flat,
            )

        # Plot results
        plt.suptitle("RF-reflectometry")
        plt.cla()
        plt.plot(ts_I, I_flat, alpha=0.8)
        plt.plot(ts_Q, Q_flat, alpha=0.8)
        plt.legend(["I", "Q"])
        plt.xlabel("Time [sec]")
        plt.ylabel("Voltage [V]")
        plt.tight_layout()
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

    plt.show()
    qm.close()

# %%
