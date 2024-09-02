# %%
"""
        READOUT OPTIMISATION: FREQUENCY & AMP
This sequence involves measuring the state of the resonator in two scenarios: first, after thermalization
(with the qubit in the |g> state) and then after applying a pi pulse to the qubit (transitioning the qubit to the
|e> state). This is done while varying the readout frequency.
The average I & Q quadratures for the qubit states |g> and |e>, along with their variances, are extracted to
determine the Signal-to-Noise Ratio (SNR). The readout frequency that yields the highest SNR is selected as the
optimal choice.

Prerequisites:
    - Having found the resonance frequency of the resonator coupled to the qubit under study (resonator_spectroscopy).
    - Having calibrated qubit pi pulse (x180) by running qubit, spectroscopy, rabi_chevron, power_rabi and updated the config.

Next steps before going to the next node:
    - Update the readout frequency (resonator_IF_q) in the configuration.
"""

from qm import QuantumMachinesManager
from qm.qua import *
from qm import SimulationConfig
# from configuration_opxplus_with_octave import *
from configuration_opxplus_without_octave import *
import matplotlib.pyplot as plt
from qualang_tools.loops import from_array
from qualang_tools.results import fetching_tool, progress_counter
from macros import multiplexed_readout, qua_declaration, iq_blobs_analysis
import math
from qualang_tools.plot import interrupt_on_close
from qualang_tools.results.data_handler import DataHandler

###################
# The QUA program #
###################

qubits = ["q2_xy", "q3_xy"]
resonators = ["q2_rr", "q3_rr"]
qubits_all = list(QUBIT_CONSTANTS.keys())
resonators_all = [key for key in RR_CONSTANTS.keys()]
remaining_resonators = list(set(resonators_all) - set(resonators))
weights = "rotated_" # ["", "rotated_", "opt_"] 
reset_method = "wait" # can also be "active"

n_avg = 2  # Number of runs

# The frequency sweep around the resonators' frequency "resonator_IF_q"
freq_span = 30e6
freq_step = 0.03e6
dfs = np.arange(-freq_span, freq_span, freq_step)

iq_blobs_analysis_method = "snr" # "snr" "fidelity" or "overlap"

assert len(qubits_all) == len(resonators_all), "qubits and resonators don't have the same length"
assert len(qubits) == len(resonators), "qubits and resonators under study don't have the same length"
assert all([qb.replace("_xy", "") == rr.replace("_rr", "") for qb, rr in zip(qubits, resonators)]), "qubits and resonators don't correspond"
assert reset_method in ["wait", "active"], "Invalid reset_method, use either wait or active"
assert len(dfs) <= 38_000, "check your frequencies"

save_data_dict = {
    "qubits_all": qubits_all,
    "resonators_all": resonators_all,
    "qubits": qubits,
    "resonators": resonators,
    "n_avg": n_avg,
    "dfs": dfs,
    "config": config,
}


with program() as ro_opt_freq_amp:

    Ig, I_g_st, Qg, Q_g_st, n, n_st = qua_declaration(resonators)
    Ie, I_e_st, Qe, Q_e_st, _, _ = qua_declaration(resonators)
    df = declare(int)  # QUA variable for the readout frequency

    with for_(n, 0, n < n_avg, n + 1):
        # Save the averaging iteration to get the progress bar
        save(n, n_st)
        with for_(*from_array(df, dfs)):

            for rr in resonators:
                update_frequency(rr, df + RR_CONSTANTS[rr]["IF"])

            # Reset both qubits to ground
            wait(qb_reset_time >> 2)
            # Measure the ground IQ blobs
            multiplexed_readout(Ig, I_g_st, Qg, Q_g_st, None, None, resonators, weights="")

            align()

            # Reset both qubits to ground
            wait(qb_reset_time >> 2)
            # Measure the excited IQ blobs
            for qb in qubits:
                play("x180", qb)
            align()
            # Measure the state of the resonators
            multiplexed_readout(Ie, I_e_st, Qe, Q_e_st, None, None, resonators, weights="")

    with stream_processing():
        n_st.save("iteration")
        for ind, rr in enumerate(resonators):
            I_g_st[ind].buffer(len(dfs)).save_all(f"I_g_{rr}")
            Q_g_st[ind].buffer(len(dfs)).save_all(f"Q_g_{rr}")
            I_e_st[ind].buffer(len(dfs)).save_all(f"I_e_{rr}")
            Q_e_st[ind].buffer(len(dfs)).save_all(f"Q_e_{rr}")


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
        job = qmm.simulate(config, ro_opt_freq_amp, simulation_config)
        job.get_simulated_samples().con1.plot()
        plt.show(block=False)
    else:
        try:
            # Open the quantum machine
            qm = qmm.open_qm(config)
            # Send the QUA program to the OPX, which compiles and executes it
            job = qm.execute(ro_opt_freq_amp)
            fetch_names = ["iteration"]
            for rr in resonators:
                fetch_names.append(f"I_g_{rr}")
                fetch_names.append(f"Q_g_{rr}")
                fetch_names.append(f"I_e_{rr}")
                fetch_names.append(f"Q_e_{rr}")
            # Tool to easily fetch results from the OPX (results_handle used in it)
            results = fetching_tool(job, fetch_names, mode="live")
            # Prepare the figure for live plotting
            fig = plt.figure()
            interrupt_on_close(fig, job)
            # Data analysis and plotting
            num_resonators = len(resonators)
            num_rows = math.ceil(math.sqrt(num_resonators))
            num_cols = math.ceil(num_resonators / num_rows)
            # Live plotting
            while results.is_processing():
                # Fetch results
                res = results.fetch_all()
                # Progress bar
                progress_counter(res[0], n_avg, start_time=results.start_time)

                plt.suptitle("Readout Opt freq-amp")

                for ind, (qb, rr) in enumerate(zip(qubits, resonators)):

                    max_len = len(res[4*ind + 1])
                    _, _, iq_blobs_result = iq_blobs_analysis(res[4*ind + 1][:max_len], res[4*ind + 2][:max_len], res[4*ind + 3][:max_len], res[4*ind + 4][:max_len], method=iq_blobs_analysis_method)
                    save_data_dict[rr+"_I_g"] = res[4*ind + 1]
                    save_data_dict[rr+"_Q_g"] = res[4*ind + 2]
                    save_data_dict[rr+"_I_e"] = res[4*ind + 3]
                    save_data_dict[rr+"_Q_e"] = res[4*ind + 4]

                    plt.subplot(num_rows, num_cols, ind + 1)
                    plt.cla()
                    plt.plot((RR_CONSTANTS[rr]["IF"] + dfs) / u.MHz, iq_blobs_result)
                    plt.xlabel("df [MHz]")
                    plt.title(f"Qb - {qb}")

                plt.tight_layout()
                plt.pause(0.1)

            # Save results
            script_name = Path(__file__).name
            data_handler = DataHandler(root_data_folder=save_dir)
            save_data_dict.update({"fig_live": fig})
            data_handler.additional_files = {script_name: script_name, **default_additional_files}
            data_handler.save_data(data=save_data_dict, name="ro_opt_freq")

        except Exception as e:
            print(f"An exception occurred: {e}")

        finally:
            qm.close()
            print("Experiment QM is now closed")
            plt.show(block=True)

# %%