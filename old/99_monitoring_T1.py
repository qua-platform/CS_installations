# %%
"""
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
from datetime import datetime, timezone, timedelta
from pathlib import Path
import copy
import matplotlib


matplotlib.use('TkAgg')


###################
# The QUA program #
###################

n_reps = 400
t_wait = 60

n_avg = 100
t_delays = np.arange(4, 10_000, 4) # in clock cycles

with program() as reflectometry_monitoring:
    d = delcare(int)
    n = declare(int)  # QUA variable for the averaging loop
    I = declare(fixed)  # QUA variable for the measured 'I' quadrature
    Q = declare(fixed)  # QUA variable for the measured 'Q' quadrature
    n_st = declare_stream()  # Stream for the averaging iteration 'n'
    I_st = declare_stream()  # Stream for the 'I' quadrature
    Q_st = declare_stream()  # Stream for the 'Q' quadrature

    with for_(n, 0, n < n_avg, n + 1):
        with for_(*from_array(d, t_delays)):
            
            play("x180", "q1_xy")
            align("q1_xy", "rr1")
            measure(
                "readout",
                "rr1",
                None,
                dual_demod.full("cos", "sin", I),
                dual_demod.full("minus_sin", "cos", Q),
            )
            save(I, I_st)
            save(Q, Q_st)
            wait(5_000)
        save(n, n_st)

    with stream_processing():
        I_st.buffer(len(t_delays)).average().save("I")
        Q_st.buffer(len(t_delays)).average().save("Q")
        n_st.save("iteration")


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config)


#######################
# Simulate or execute #
#######################
simulate = False
save_data = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, reflectometry_monitoring, simulation_config)
    # Plot the simulated samples
    job.get_simulated_samples().con1.plot()
    plt.show()

else:
    # Open the quantum machine
    qm = qmm.open_qm(config)

    # make a temporal directory for the data
    if save_data:
        from qualang_tools.results.data_handler import DataHandler

        # Save results
        script_name = Path(__file__).name
        data_handler = DataHandler(root_data_folder=save_dir)
        data_handler.create_data_folder(name="monitoring_reflectometry")

    dt_arr = np.empty(n_reps, dtype='datetime64[us]') 
    Is_arr = np.zeros(n_reps, len(t_delays))
    Qs_arr = np.zeros(n_reps, len(t_delays))
    T1s_arr = np.zeros(n_reps)

    for rep in range(n_reps):

        # Record timestamp
        datetime_now = datetime.now(timezone(timedelta(hours=9)))
        dt_arr[rep] = np.datetime64(datetime_now, 's')

        current_datetime = datetime_now.strftime("%Y/%m/%d-%H:%M:%S")
        _log_this = f"{current_datetime}, repetition={rep+1}"

        # Send the QUA program to the OPX, which compiles and executes it
        job = qm.execute(reflectometry_monitoring)

        results = fetching_tool(job, data_list=["I", "Q", "iteration"], mode="live")

        # Live plotting
        fig = plt.figure()
        interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
        while results.is_processing():
            # Fetch results
            I, Q, iteration = results.fetch_all()

            # Progress bar
            progress_counter(iteration, n_avg, start_time=results.get_start_time())

        # Record I&Q
        Is_arr[rep, :] = I
        Qs_arr[rep, :] = Q

        try:
            from qualang_tools.plot.fitting import Fit

            fit = Fit()
            fig = plt.figure()
            plt.suptitle("T1 measurement")
            decay_fit = fit.T1(4 * t_delays, I, plot=True)
            qubit_T1 = np.round(np.abs(decay_fit["T1"][0]) / 4) * 4
            plt.xlabel("Delay [ns]")
            plt.ylabel("I quadrature [V]")
            _log_this = f"{_log_this}: qubit_T1 = {qubit_T1:.0f} ns"
            plt.legend((f"depletion time = {qubit_T1:.0f} ns",))
            plt.title(f"T1: rep: {rep + 1}")
            plt.tight_layout()
            plt.show()

            # Record T1
            T1s_arr[rep] = qubit_T1

        except (Exception,):
            _log_this = f"{_log_this}: fitting failed"
            pass

        print(_log_this)

        # Save log
        if save_data:
            # Open the log file in append mode and write the log
            with open(data_handler.path / "log.txt", encoding="utf8", mode="a") as f:
                f.write(_log_this.replace("_", "") + "\n")  # Append the log message to the file

            # Data to save
            np.savez(
                file = data_handler.path / "data.npz",
                I = Is_arr,
                Q = Qs_arr,
                T1 = T1s_arr,
                dt = dt_arr,
            )
            save_data_dict = {}
            save_data_dict["I"] = Is_arr
            save_data_dict["Q"] = Qs_arr
            save_data_dict["T1"] = T1s_arr
            save_data_dict["timestamp"] = dt_arr
            data_handler.save_data(data=save_data_dict, node_contents=None)

        plt.close()
        plt.pause(t_wait)
        qm.close()

    if save_data:
        from qualang_tools.results.data_handler import DataHandler

        # Data to save
        save_data_dict = {}
        # save_data_dict["elapsed_time"] =  np.array([elapsed_time])
        save_data_dict["I"] = Is_arr
        save_data_dict["Q"] = Qs_arr
        save_data_dict["T1"] = T1s_arr
        save_data_dict["timestamp"] = dt_arr

        # Save results
        data_handler.additional_files = {
            script_name: script_name,
            **default_additional_files,
        }
        data_handler.save_data(data=save_data_dict)


# %%
