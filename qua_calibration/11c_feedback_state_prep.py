# %%
"""

"""

from qm import QuantumMachinesManager, SimulationConfig
from qm.qua import *
from configuration_mw_fem import *
import matplotlib.pyplot as plt
from qualang_tools.results import fetching_tool
from macros import qua_declaration, multiplexed_readout
from qualang_tools.results import progress_counter
from qualang_tools.results.data_handler import DataHandler
from qualang_tools.analysis import two_state_discriminator
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')



##################
#   Parameters   #
##################

midcircuit_ge_threshold = {
    "rr1": ge_threshold_q1,
    "rr2": ge_threshold_q2,
}

midcircuit_ge_threshold_g = {
    "rr1": -1.5e-5,
    "rr2": -1.3e-5,
}

midcircuit_ge_threshold_e = {
    "rr1": 0.0,
    "rr2": 0.0,
}

def active_reset(
        I, I_st, Q, Q_st, state, state_st,\
        resonators, qubits,
        state_to, delay=None,
        amplitude=1.0, readout_pulse="readout", weights="rotated_"):

    global_state = declare(int)

    if type(resonators) is not list:
        resonators = [resonators]

    assign(global_state, 0)
    
    for ind, rr in enumerate(resonators):
        # reset_if_phase(rr)
        measure(
            readout_pulse * amp(amplitude),
            rr,
            None,
            dual_demod.full(weights + "cos", weights + "minus_sin", I[ind]),
            dual_demod.full(weights + "sin", weights + "cos", Q[ind]),
        )

        if I_st is not None:
            save(I[ind], I_st[ind])
        if Q_st is not None:
            save(Q[ind], Q_st[ind])

        ###################################################################################
        # NOTE: Ig is promised to be smaller than Ie ONLY if rotation angle is calibrated #
        ###################################################################################

        assign(state[ind], I[ind] > midcircuit_ge_threshold[rr])
        assign(global_state, (Cast.to_int(state[ind]) << ind) + global_state)

        if state_st is not None:
            save(state[ind], state_st[ind])

    align()

    for ind, qb in enumerate(qubits):

        if delay is None:
            pass
        else:
            wait(delay, qb)
        if state_to == "ground":
            play("x180", qb, condition=state[ind])
        elif state_to == "excited":
            play("x180", qb, condition=~state[ind])
        elif state_to == "none":
            pass

    return global_state



##################
#   Parameters   #
##################
qubits = ["q1_xy", "q2_xy"]
resonators = ["rr1", "rr2"]
idx = 1


#########################
# Parameters Definition #
#########################

n_runs = 10_000  # Number of runs
reset_method = "wait"
weights = "rotated_"
qb_reset_time = 10_000

# Data to save
save_data_dict = {
    "qubits": qubits,
    "shots": n_runs,
    "config": config,
}


###################
#   QUA Program   #
###################

with program() as PROGRAM:
    I_g, I_g_st, Q_g, Q_g_st, n, n_st = qua_declaration(nb_of_qubits=2)
    I_e, I_e_st, Q_e, Q_e_st, _, _ = qua_declaration(nb_of_qubits=2)
    state = [declare(bool) for _ in range(2)]
    global_state = declare(int)

    with for_(n, 0, n < n_runs, n + 1):
        save(n, n_st)
        # GROUND iq blobs for both qubits
        # qubit reset
        if reset_method == "wait":
            wait(qb_reset_time // 4)
        elif reset_method == "active":
            global_state = active_reset(
                I_g, None, Q_g, None, state, None,
                resonators, qubits, state_to="ground",
                weights=weights,
            )
        align()

        multiplexed_readout(I_g, None, Q_g, None, resonators=[1, 2], weights=weights)

        with while_(I_g[idx] > midcircuit_ge_threshold_g[resonators[idx]]):

            multiplexed_readout(I_g, None, Q_g, None, resonators=[1, 2], weights=weights)
            
            wait(readout_len // 4, *resonators, qubits[idx])
        
            with port_condition(I_g[idx] > midcircuit_ge_threshold[resonators[idx]]):
                
                play("x180", qubits[idx])

        align()

        # Measure the state of the resonators
        multiplexed_readout(I_g, I_g_st, Q_g, Q_g_st, resonators=[1, 2], weights=weights)


        # EXCITED iq blobs for both qubits
        # qubit reset
        if reset_method == "wait":
            wait(qb_reset_time // 4)
            # Play the qubit pi pulses
            for qb in qubits:
                play("x180", qb)
        elif reset_method == "active":
            global_state = active_reset(
                I_e, None, Q_e, None, state, None,
                resonators, qubits, state_to="excited",
                weights=weights,
            )
        align()

        multiplexed_readout(I_e, None, Q_e, None, resonators=[1, 2], weights=weights)

        with while_(I_g[idx] < midcircuit_ge_threshold_e[resonators[idx]]):

            multiplexed_readout(I_e, None, Q_e, None, resonators=[1, 2], weights=weights)
            
            wait(readout_len // 4, *resonators, qubits[idx])
        
            with port_condition(I_e[idx] < midcircuit_ge_threshold[resonators[idx]]):
                
                play("x180", qubits[idx])

        align()

        # Measure the state of the resonators
        multiplexed_readout(I_e, I_e_st, Q_e, Q_e_st, resonators=[1, 2], weights=weights)

        # wait(qb_reset_time // 4)

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
        job = qmm.simulate(config, PROGRAM, simulation_config)
        job.get_simulated_samples().con1.plot()
        plt.show(block=False)
    else:
        try:
            # Open the quantum machine
            qm = qmm.open_qm(config)
            # Send the QUA program to the OPX, which compiles and executes it
            job = qm.execute(PROGRAM)

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
            import math
            num_resonators = len(resonators)
            num_rows = math.ceil(math.sqrt(num_resonators))
            num_cols = math.ceil(num_resonators / num_rows)

            for ind, (qb, rr) in enumerate(zip(qubits, resonators)):

                rr_qubit_match = False

                angle_val, threshold_val, fidelity_val, gg, ge, eg, ee = two_state_discriminator(res[4*ind + 1], res[4*ind + 2], res[4*ind + 3], res[4*ind + 4], b_print=False, b_plot=True)
                save_data_dict[rr+"_gg"] = gg
                save_data_dict[rr+"_ge"] = ge
                save_data_dict[rr+"_eg"] = eg
                save_data_dict[rr+"_ee"] = ee
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
            data_handler.save_data(data=save_data_dict, name="feedback_state_prep")

        except Exception as e:
            print(f"An exception occurred: {e}")

        finally:
            qm.close()
            print("Experiment QM is now closed")
            plt.show(block=True)

# %%