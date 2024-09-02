# %%
"""
        IQ BLOBS
This sequence involves measuring the state of the resonator 'N' times, first after thermalization (with the qubit
in the |g> state) and then after applying a pi pulse to the qubit (bringing the qubit to the |e> state) successively.
The resulting IQ blobs are displayed, and the data is processed to determine:
    - The rotation angle required for the integration weights, ensuring that the separation between |g> and |e> states
      aligns with the 'I' quadrature.
    - The threshold along the 'I' quadrature for effective qubit state discrimination.
    - The readout fidelity matrix, which is also influenced by the pi pulse fidelity.

Prerequisites:
    - Having found the resonance frequency of the resonator coupled to the qubit under study (resonator_spectroscopy).
    - Having calibrated qubit pi pulse (x180) by running qubit, spectroscopy, rabi_chevron, power_rabi and updated the config.

Next steps before going to the next node:
    - Update the rotation angle (rotation_angle) in the configuration.
    - Update the g -> e threshold (ge_threshold) in the configuration.
"""

from qm import QuantumMachinesManager, SimulationConfig
from qm.qua import *
# from configuration_opxplus_with_octave import *
from configuration_opxplus_without_octave import *
import matplotlib.pyplot as plt
from qualang_tools.results import fetching_tool
from macros import qua_declaration, multiplexed_readout, active_reset
from qualang_tools.results import progress_counter
import math
from qualang_tools.results.data_handler import DataHandler
from qualang_tools.analysis import two_state_discriminator

###################
# The QUA program #
###################

qubits = ["q2_xy", "q3_xy"]
resonators = ["q2_rr", "q3_rr"]
qubits_all = list(QUBIT_CONSTANTS.keys())
resonators_all = [key for key in RR_CONSTANTS.keys()]
remaining_resonators = list(set(resonators_all) - set(resonators))
weights = "rotated_" # ["", "rotated_", "opt_"] 
reset_method = "active" # can also be "active"
readout_operation = "readout" # "readout" or "midcircuit_readout"

n_runs = 1_000  # Number of runs

assert len(qubits_all) == len(resonators_all), "qubits and resonators don't have the same length"
assert len(qubits) == len(resonators), "qubits and resonators under study don't have the same length"
assert all([qb.replace("_xy", "") == rr.replace("_rr", "") for qb, rr in zip(qubits, resonators)]), "qubits and resonators don't correspond"
assert weights in ["", "rotated_", "opt_"], 'weight_type must be one of ["", "rotated_", "opt_"]'
assert reset_method in ["wait", "active"], "Invalid reset_method, use either wait or active"
assert readout_operation in ["readout", "midcircuit_readout"], "Invalid readout_operation, use either readout or midcircuit_readout"
assert n_runs < 20_000, "check the number of shots"

save_data_dict = {
    "qubits_all": qubits_all,
    "resonators_all": resonators_all,
    "qubits": qubits,
    "resonators": resonators,
    "shots": n_runs,
    "config": config,
    "readout_operation": readout_operation,
}


with program() as iq_blobs:
    I_g, I_g_st, Q_g, Q_g_st, n, n_st = qua_declaration(resonators)
    I_e, I_e_st, Q_e, Q_e_st, _, _ = qua_declaration(resonators)
    state = [declare(bool) for _ in range(len(resonators))]
    global_state = declare(int)

    with for_(n, 0, n < n_runs, n + 1):
        save(n, n_st)
        # GROUND iq blobs for both qubits
        # qubit reset
        if reset_method == "wait":
            wait(qb_reset_time >> 2)
        elif reset_method == "active":
            global_state = active_reset(
                I_g, None, Q_g, None, state, None,
                resonators, qubits, state_to="ground",
                weights=weights,
            )
        align()
        # Measure the state of the resonators
        multiplexed_readout(I_g, I_g_st, Q_g, Q_g_st, None, None, resonators, weights=weights)

        align()

        # EXCITED iq blobs for both qubits
        if reset_method == "wait":
            wait(qb_reset_time >> 2)
            # Play the qubit pi pulses
            for qb in qubits:
                play("x180", qb)
        elif reset_method == "active":
            global_state = active_reset(
                I_g, None, Q_g, None, state, None,
                resonators, qubits, state_to="excited",
                weights=weights,
            )
        align()
        # Measure the state of the resonators
        multiplexed_readout(I_e, I_e_st, Q_e, Q_e_st, None, None, resonators, weights=weights)

    with stream_processing():
        n_st.save('iteration')
        # Save all streamed points for plotting the IQ blobs
        for ind, rr in enumerate(resonators):
            I_g_st[ind].save_all(f"I_g_{rr}")
            Q_g_st[ind].save_all(f"Q_g_{rr}")
            I_e_st[ind].save_all(f"I_e_{rr}")
            Q_e_st[ind].save_all(f"Q_e_{rr}")


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
        job = qmm.simulate(config, iq_blobs, simulation_config)
        job.get_simulated_samples().con1.plot()
        plt.show(block=False)
    else:
        try:
            # Open the quantum machine
            qm = qmm.open_qm(config)
            # Send the QUA program to the OPX, which compiles and executes it
            job = qm.execute(iq_blobs)

            fetch_names = ["iteration"]
            results = fetching_tool(job, fetch_names, mode="live")
            while results.is_processing():
                # Fetch results
                res = results.fetch_all()
                # Progress bar
                progress_counter(res[0], n_runs, start_time=results.start_time)

            for rr in resonators:
                fetch_names.append(f"I_g_{rr}")
                fetch_names.append(f"Q_g_{rr}")
                fetch_names.append(f"I_e_{rr}")
                fetch_names.append(f"Q_e_{rr}")

            # Tool to easily fetch results from the OPX (results_handle used in it)
            results = fetching_tool(job, fetch_names)

            res = results.fetch_all()

            # Plotting
            num_resonators = len(resonators)
            num_rows = math.ceil(math.sqrt(num_resonators))
            num_cols = math.ceil(num_resonators / num_rows)

            for ind, (qb, rr) in enumerate(zip(qubits, resonators)):

                rr_qubit_match = False

                angle_val, threshold_val, fidelity_val, _, _, _, _ = two_state_discriminator(res[4*ind + 1], res[4*ind + 2], res[4*ind + 3], res[4*ind + 4], b_print=False, b_plot=False)
                save_data_dict[rr+"_angle"] = angle_val * 180 / np.pi
                save_data_dict[rr+"_threshold"] = threshold_val
                save_data_dict[rr+"_fidelity"] = fidelity_val

                save_data_dict[rr+"_Ig"] = res[4*ind + 1]
                save_data_dict[rr+"_Qg"] = res[4*ind + 2]
                save_data_dict[rr+"_Ie"] = res[4*ind + 3]
                save_data_dict[rr+"_Qe"] = res[4*ind + 4]

                plt.subplot(num_rows, num_cols, ind + 1)
                plt.plot(res[4*ind + 1], res[4*ind + 2], ".", alpha=0.1, markersize=2)
                plt.plot(res[4*ind + 3], res[4*ind + 4], ".", alpha=0.1, markersize=2)
                plt.axis('equal')
                plt.axvline(x=0, linestyle='--', color='k')
                plt.axhline(y=0, linestyle='--', color='k')
                plt.title(f"Qb - {qb}")

            plt.tight_layout()
            fig = plt.gcf()

            fig2 = plt.figure()
            for ind, (qb, rr) in enumerate(zip(qubits, resonators)):
                plt.subplot(num_rows, num_cols, ind + 1)
                plt.hist(res[4*ind + 1], bins= 1 + int(np.log2(len(res[4*ind + 1]))), alpha=0.6)
                plt.hist(res[4*ind + 3], bins= 1 + int(np.log2(len(res[4*ind + 3]))), alpha=0.6)
                # plt.yscale('log')

            plt.tight_layout()

            suffixes = ["_angle", "_threshold", "_fidelity"]
            for key in save_data_dict.keys():
                for suffix in suffixes:
                    if key.endswith(suffix):
                        print(f"{key}: {save_data_dict[key]}")
                        if suffix == "_fidelity":
                            print("------------------------")

            # Save results
            script_name = Path(__file__).name
            data_handler = DataHandler(root_data_folder=save_dir)
            save_data_dict.update({"fig_live": fig, "fig_analysis": fig2})
            data_handler.additional_files = {script_name: script_name, **default_additional_files}
            data_handler.save_data(data=save_data_dict, name="iq_blobs")

        except Exception as e:
            print(f"An exception occurred: {e}")

        finally:
            qm.close()
            print("Experiment QM is now closed")
            plt.show(block=True)

# %%
