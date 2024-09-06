# %%
"""
        RAMSEY CHEVRON (IDLE TIME VS FREQUENCY)
The program consists in playing a Ramsey sequence (x90 - idle_time - x90 - measurement) for different qubit intermediate
frequencies and idle times.
From the results, one can estimate the qubit frequency more precisely than by doing Rabi and also gets a rough estimate
of the qubit coherence time.

Prerequisites:
    - Having found the resonance frequency of the resonator coupled to the qubit under study (resonator_spectroscopy).
    - Having calibrated qubit pi pulse (x180) by running qubit, spectroscopy, rabi_chevron, power_rabi and updated the config.
    - (optional) Having calibrated the readout (readout_frequency, amplitude, duration_optimization IQ_blobs) for better SNR.

Next steps before going to the next node:
    - Update the qubit frequency (qubit_IF_q) in the configuration.
"""

from qm import QuantumMachinesManager, SimulationConfig
from qm.qua import *
# from configuration_opxplus_with_octave import *
from configuration_opxplus_without_octave import *
import matplotlib.pyplot as plt
from qualang_tools.loops import from_array
from qualang_tools.results import fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.results import progress_counter
from macros import qua_declaration, multiplexed_readout, active_reset
import math
from qualang_tools.results.data_handler import DataHandler
import time, datetime

##################
#   Parameters   #
##################

# Qubits and resonators 
qc = 2 # index of control qubit
qt = 3 # index of target qubit

# Parameters Definition
n_reps = 20
n_avg = 10  # The number of averages
t_max = 400
t_min = 4
t_step = 4
t_delays = np.arange(t_min, t_max, t_step)  # Idle time sweep in clock cycles (Needs to be a list of integers)
pause_repetition = 30

# Readout Parameters
weights = "rotated_" # ["", "rotated_", "opt_"]
reset_method = "wait" # ["wait", "active"]
readout_operation = "readout" # ["readout", "midcircuit_readout"]

# Derived parameters
qc_xy = f"q{qc}_xy"
qt_xy = f"q{qt}_xy"
qubits = [f"q{i}_xy" for i in [qc, qt]]
resonators = [f"q{i}_rr" for i in [qc, qt]]
num_resonators = len(resonators)

# Assertion
assert len(t_delays) <= 76_000, "check your delays"

# Data to save
save_data_dict = {
    "qubits": qubits,
    "resonators": resonators,
    "n_reps": n_reps,
    "n_avg": n_avg,
    "t_delays": t_delays,
    "config": config,
}


###################
#   QUA Program   #
###################

with program() as PROGRAM:
    m = declare(int)
    m_st = declare_stream()

    with for_(m, 0, m < n_reps + 1, m + 1):
        pause()  # This waits until it is resumed from python

        I, I_st, Q, Q_st, n, n_st = qua_declaration(resonators)
        t = declare(int)  # QUA variable for the idle time

        with for_(n, 0, n < n_avg, n + 1):
            with for_(*from_array(t, t_delays)):
                for qb in qubits:
                    play('x180', qb)
                    wait(t, qb)

                # Align the elements to measure after having waited a time "tau" after the qubit pulses.
                align()

                # Measure the state of the resonators
                multiplexed_readout(I, I_st, Q, Q_st, None, None, resonators=resonators, weights=weights)            

                # Wait for the qubit to decay to the ground state
                wait(qb_reset_time >> 2)

            # Save the averaging iteration to get the progress bar
            save(n, n_st)
        # Save the averaging iteration to get the progress bar
        save(m, m_st)

    with stream_processing():
        m_st.save("repetition")
        n_st.save("iteration")
        for ind, rr in enumerate(resonators):
            I_st[ind].buffer(len(t_delays)).average().save(f"I_{rr}")
            Q_st[ind].buffer(len(t_delays)).average().save(f"Q_{rr}")


if __name__ == "__main__":
    #####################################
    #  Open Communication with the QOP  #
    #####################################
    qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config)

    ###########################
    # Run or Simulate Program #
    ###########################

    simulate = False

    def wait_until_job_is_paused(current_job):
        """
        Waits until the OPX FPGA reaches the pause statement.
        Used when the OPX sequence needs to be synchronized with an external parameter sweep.

        :param current_job: the job object.
        """
        while not current_job.is_paused():
            time.sleep(0.1)
            pass
        return True

    if simulate:
        # Simulates the QUA program for the specified duration
        simulation_config = SimulationConfig(duration=1_000)  # In clock cycles = 4ns
        job = qmm.simulate(config, PROGRAM, simulation_config)
        job.get_simulated_samples().con1.plot()
        plt.show(block=False)
    else:
        try:
            # Open the quantum machine
            qm = qmm.open_qm(config)
            # Send the QUA program to the OPX, which compiles and executes it
            job = qm.execute(PROGRAM)

            # Save results
            data_handler = DataHandler(root_data_folder=save_dir)
            fetch_names = ["iteration"]
            for rr in resonators:
                I_name, Q_name = f"I_{rr}", f"Q_{rr}"
                fetch_names.append(I_name)
                fetch_names.append(Q_name)
                save_data_dict[I_name] = np.zeros((n_reps, len(t_delays)))
                save_data_dict[Q_name] = np.zeros((n_reps, len(t_delays)))
                save_data_dict[f"T1_{I_name}"] = np.zeros(n_reps)
                save_data_dict[f"T1_{Q_name}"] = np.zeros(n_reps)
            fetch_names.append("repetition")

            for n_rep in range(n_reps):
                curr_time = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
                print(f"rep {n_rep + 1:d} out of {n_reps} at {curr_time}")
                # Resume the QUA program (escape the 'pause' statement)
                job.resume()
                # Wait until the program reaches the 'pause' statement again, indicating that the QUA program is done
                wait_until_job_is_paused(job)

                # Prepare the figure for live plotting
                fig, axss = plt.subplots(2, num_resonators, figsize=(8, 2.5 * num_resonators), sharex=True)
                interrupt_on_close(fig, job)
                # # Tool to easily fetch results from the OPX (results_handle used in it)
                results = fetching_tool(job, fetch_names, mode="live")
                n_ = 0
                # Live plotting
                while n_ + 1 < n_avg:
                    # Fetch results
                    res = results.fetch_all()
                    n_ = res[0]
                    # Progress bar
                    progress_counter(n_, n_avg, start_time=results.start_time)
                    time.sleep(0.5)
                
                for ind, (qb, rr) in enumerate(zip(qubits, resonators)):
                    # Data analysis
                    I = res[2 * ind + 1]
                    Q = res[2 * ind + 2]
                    save_data_dict[fetch_names[2 * ind + 1]][n_rep, :] = I
                    save_data_dict[fetch_names[2 * ind + 2]][n_rep, :] = Q

                    # Plot
                    ax = axss[ind, 0]
                    ax.plot(t_delays * 4, I, color='r')
                    ax.set_ylabel("I [V]")
                    ax.set_title(fetch_names[2 * ind + 1])

                    ax = axss[ind, 1]
                    ax.plot(t_delays * 4, Q, color='r')
                    ax.set_ylabel("Q [V]")
                    ax.set_title(fetch_names[2 * ind + 2])

                plt.suptitle("Multiplexed T1 - I & Q")
                plt.tight_layout()
                save_data_dict.update({f"fig_live_{n_rep:04d}": fig})

                # Fit the data
                try:
                    from qualang_tools.plot.fitting import Fit
                    for ind, (qb, rr) in enumerate(zip(qubits, resonators)):
                        for i_IQ in [1, 2]:
                            V = res[2 * ind + i_IQ]
                            V_name = fetch_names[2 * ind + i_IQ]
                            fit = Fit()
                            fig_analysis = plt.figure(figsize=(6,6))
                            decay_fit = fit.T1(4 * t_delays, V, plot=True)
                            qubit_T1 = np.round(np.abs(decay_fit["T1"][0]) / 4) * 4
                            plt.xlabel("Delay [ns]")
                            plt.ylabel("Quadrature [V]")
                            print(f"Qubit decay time ({qb}, {V_name}): T1 = {qubit_T1:.0f} ns")
                            plt.legend((f"Relaxation time T1 = {qubit_T1:.0f} ns",))
                            plt.title(f"T1 measurement of {V_name}")
                            save_data_dict[f"T1_{V_name}"][n_rep] = qubit_T1
                            save_data_dict.update({f"fig_analysis_{n_rep:04d}_{V_name}": fig_analysis})
                except:
                    print(f"fitting failed at {n_rep + 1}")
                finally:
                    plt.show()

                # Save data
                script_name = Path(__file__).name
                data_handler.additional_files = {script_name: script_name, **default_additional_files}
                data_handler.save_data(data=save_data_dict, name="repeated_T1")

                # Remove the current figures from the save data 
                save_data_dict.pop(f"fig_live_{n_rep:04d}")
                for ind, (qb, rr) in enumerate(zip(qubits, resonators)):
                    for i_IQ in [1, 2]:
                        V = res[2 * ind + i_IQ]
                        V_name = fetch_names[2 * ind + i_IQ]
                        save_data_dict.pop(f"fig_analysis_{n_rep:04d}_{V_name}")

                # pause between repetition
                time.sleep(pause_repetition)

        except Exception as e:
            print(f"An exception occurred: {e}")

        finally:
            qm.close()
            print("Experiment QM is now closed")
            plt.show(block=True)

# %%
