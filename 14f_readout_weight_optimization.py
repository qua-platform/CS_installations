# %%
"""
        READOUT OPTIMISATION: INTEGRATION WEIGHTS
"""

from qm import QuantumMachinesManager, SimulationConfig
from qm.qua import *
# from configuration_opxplus_with_octave import *
from configuration_opxplus_without_octave import *
import matplotlib.pyplot as plt
from qualang_tools.results import fetching_tool, progress_counter
import math
from qualang_tools.plot import interrupt_on_close
from qualang_tools.results.data_handler import DataHandler

###########
# Helpers #
###########

def normalize_complex_array(arr):
    # Calculate the simple norm of the complex array
    norm = np.sqrt(np.sum(np.abs(arr) ** 2))

    # Normalize the complex array by dividing it by the norm
    normalized_arr = arr / norm

    # Rescale the normalized array so that the maximum value is 1
    max_val = np.max(np.abs(normalized_arr))
    rescaled_arr = normalized_arr / max_val

    return rescaled_arr


def plot_three_complex_arrays(x, aq1_rr, aq2_rr, aq3_rr, axs):
    (ax1, ax2, ax3) = axs
    ax1.plot(x, aq1_rr.real, label="real")
    ax1.plot(x, aq1_rr.imag, label="imag")
    ax1.set_title("ground state")
    ax1.set_xlabel("Readout time [ns]")
    ax1.set_ylabel("demod traces [a.u.]")
    ax1.legend()
    ax2.plot(x, aq2_rr.real, label="real")
    ax2.plot(x, aq2_rr.imag, label="imag")
    ax2.set_title("excited state")
    ax2.set_xlabel("Readout time [ns]")
    ax2.set_ylabel("demod traces [a.u.]")
    ax2.legend()
    ax3.plot(x, aq3_rr.real, label="real")
    ax3.plot(x, aq3_rr.imag, label="imag")
    ax3.set_title("OPT WEIGHTS")
    ax3.set_xlabel("Readout time [ns]")
    ax3.set_ylabel("subtracted traces [a.u.]")
    ax3.legend()


###################
# The QUA program #
###################

qubits = ["q1_xy"]
resonators = ["q1_rr"]
qubits_all = list(QUBIT_CONSTANTS.keys())
resonators_all = [key for key in RR_CONSTANTS.keys()]
remaining_resonators = list(set(resonators_all) - set(resonators))
weights = "rotated_" # ["", "rotated_", "opt_"] 
reset_method = "wait" # can also be "active"

n_avg = 1e3  # number of averages
# Set the sliced demod parameters
division_length = 1  # Size of each demodulation slice in clock cycles
number_of_divisions = int((readout_len) / (4 * division_length))

# Time axis for the plots at the end
x_plot = np.arange(division_length * 4, readout_len + 1, division_length * 4)

assert len(qubits_all) == len(resonators_all), "qubits and resonators don't have the same length"
assert len(qubits) == len(resonators), "qubits and resonators under study don't have the same length"
assert all([qb.replace("_xy", "") == rr.replace("_rr", "") for qb, rr in zip(qubits, resonators)]), "qubits and resonators don't correspond"
assert len(resonators) == 1, "resonators must be one resonator"
assert reset_method in ["wait", "active"], "Invalid reset_method, use either wait or active"
assert number_of_divisions <= 4_000, "check the number of divisions"

print("Integration weights chunk-size length in clock cycles:", division_length)
print("The readout has been sliced in the following number of divisions", number_of_divisions)

save_data_dict = {
    "qubits_all": qubits_all,
    "resonators_all": resonators_all,
    "qubits": qubits,
    "resonators": resonators,
    "remaining_resonators": remaining_resonators,
    "n_avg": n_avg,
    "division_length": division_length,
    "number_of_divisions": number_of_divisions,
    "x_plot": x_plot,
    "config": config,
}


with program() as opt_weights:
    II = declare(fixed, size=number_of_divisions)
    IQ = declare(fixed, size=number_of_divisions)
    QI = declare(fixed, size=number_of_divisions)
    QQ = declare(fixed, size=number_of_divisions)
    I = declare(fixed, size=number_of_divisions)
    Q = declare(fixed, size=number_of_divisions)
    ind = declare(int)

    n_st = declare_stream()
    Ig_st = declare_stream()
    Qg_st = declare_stream()
    Ie_st = declare_stream()
    Qe_st = declare_stream()
    n = declare(int)
    n_st = declare_stream()   

    with for_(n, 0, n < n_avg, n + 1):
        save(n, n_st)
        # Reset both qubits to ground
        wait(qb_reset_time >> 2)

        measure(
            "readout",
            resonators,
            None,
            demod.sliced("cos", II, division_length, "out1"),
            demod.sliced("minus_sin", IQ, division_length, "out2"),
            demod.sliced("sin", QI, division_length, "out1"),
            demod.sliced("cos", QQ, division_length, "out2"),
        )

        # Save the QUA vectors to their corresponding streams
        with for_(ind, 0, ind < number_of_divisions, ind + 1):
            assign(I[ind], II[ind] + IQ[ind])
            save(I[ind], Ig_st)
            assign(Q[ind], QQ[ind] + QI[ind])
            save(Q[ind], Qg_st)
            wait(2_000 >> 2)

        # Measure the excited IQ blobs
        align()

        # Reset both qubits to ground
        wait(qb_reset_time >> 2)

        # Measure the excited IQ blobs
        for qb in qubits:
            play("x180", qb)
        align()
        # Loop over the two resonators
        measure(
            "readout",
            resonators,
            None,
            demod.sliced("cos", II, division_length, "out1"),
            demod.sliced("minus_sin", IQ, division_length, "out2"),
            demod.sliced("sin", QI, division_length, "out1"),
            demod.sliced("cos", QQ, division_length, "out2"),
        )

        # Save the QUA vectors to their corresponding streams
        with for_(ind, 0, ind < number_of_divisions, ind + 1):
            assign(I[ind], II[ind] + IQ[ind])
            save(I[ind], Ie_st)
            assign(Q[ind], QQ[ind] + QI[ind])
            save(Q[ind], Qe_st)
            wait(2_000 >> 2)

    with stream_processing():
        n_st.save("iteration")
        for rr in resonators:
            Ig_st.buffer(number_of_divisions).average().save(f"I_g_{rr}")
            Qg_st.buffer(number_of_divisions).average().save(f"Q_g_{rr}")
            Ie_st.buffer(number_of_divisions).average().save(f"I_e_{rr}")
            Qe_st.buffer(number_of_divisions).average().save(f"Q_e_{rr}")


if __name__ == "__main__":
    #####################################
    #  Open Communication with the QOP  #
    #####################################
    qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config)

    ###########################
    # Run or Simulate Program #
    ###########################

    simulate = False

    if simulate:
        # Simulates the QUA program for the specified duration
        simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
        job = qmm.simulate(config, opt_weights, simulation_config)
        job.get_simulated_samples().con1.plot()
        plt.show(block=False)
    else:
        try:
            # Open the quantum machine
            qm = qmm.open_qm(config)
            # Send the QUA program to the OPX, which compiles and executes it
            job = qm.execute(opt_weights)
            fetch_names = ["iteration"]
            for rr in resonators:
                fetch_names.append(f"I_g_{rr}")
                fetch_names.append(f"Q_g_{rr}")
                fetch_names.append(f"I_e_{rr}")
                fetch_names.append(f"Q_e_{rr}")
            # Tool to easily fetch results from the OPX (results_handle used in it)
            results = fetching_tool(job, fetch_names, mode="live")
            # Prepare the figure for live plotting
            fig, axs = plt.subplots(1, 3, figsize=(15, 5))
            interrupt_on_close(fig, job)
            # Live plotting
            while results.is_processing():
                # Fetch results
                res = results.fetch_all()
                # Progress bar
                progress_counter(res[0], n_avg, start_time=results.start_time)

                for ind, rr in enumerate(resonators):
                    save_data_dict[rr+"_I_g"] = res[4*ind + 1]
                    save_data_dict[rr+"_Q_g"] = res[4*ind + 2]
                    save_data_dict[rr+"_I_e"] = res[4*ind + 3]
                    save_data_dict[rr+"_Q_e"] = res[4*ind + 4]

                    max_len = len(res[4*ind + 1])

                    ground_trace = res[4*ind + 1][: max_len] + 1j*res[4*ind + 2][: max_len]
                    excited_trace = res[4*ind + 3][: max_len] + 1j*res[4*ind + 4][: max_len]
                    subtracted_trace = excited_trace - ground_trace
                    normalized_subtracted_trace = normalize_complex_array(subtracted_trace)  # <- these are the optimal weights :)

                    # Plot the results
                    plt.cla()
                    plot_three_complex_arrays(x_plot, ground_trace, excited_trace, normalized_subtracted_trace, axs)
                    plt.suptitle(f"Integration weight optimization for qubit {rr[0:3]}_xy")

                plt.tight_layout()
                plt.pause(0.1)

            # Save results
            script_name = Path(__file__).name
            data_handler = DataHandler(root_data_folder=save_dir)
            save_data_dict.update({"fig_live": fig})
            data_handler.additional_files = {script_name: script_name, **default_additional_files}
            data_handler.save_data(data=save_data_dict, name="ro_opt_weights")

            # Reshape the optimal integration weights to match the configuration
            weights_real = normalized_subtracted_trace.real
            weights_minus_imag = - normalized_subtracted_trace.imag
            weights_imag = normalized_subtracted_trace.imag
            weights_minus_real = - normalized_subtracted_trace.real

            for rr in resonators:
                # Save the weights for later use in the config
                np.savez(
                    f"optimal_weights_{rr}",
                    weights_real=weights_real,
                    weights_minus_imag=weights_minus_imag,
                    weights_imag=weights_imag,
                    weights_minus_real=weights_minus_real,
                    division_length=division_length
                )

        except Exception as e:
            print(f"An exception occurred: {e}")

        finally:
            qm.close()
            print("Experiment QM is now closed")
            plt.show(block=True)

    # %%