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
from macros import qua_declaration, multiplexed_readout, active_reset, gef_discriminator_mean_points
from qualang_tools.results import progress_counter
import math
from qualang_tools.results.data_handler import DataHandler
from qualang_tools.analysis import two_state_discriminator

##################
#   Parameters   #
##################

# Qubits and resonators 
qc = 2 # index of control qubit
qt = 3 # index of target qubit

# Parameters Definition
n_runs = 1_000  # Number of runs

# Readout Parameters
weights = "rotated_" # ["", "rotated_", "opt_"]
reset_method = "active" #["wait", "active"]
readout_operation = "readout" # ["readout", "midcircuit_readout"]

# Derived parameters
qc_xy = f"q{qc}_xy"
qt_xy = f"q{qt}_xy"
qubits = [f"q{i}_xy" for i in [qc, qt]]
resonators = [f"q{i}_rr" for i in [qc, qt]]

# Assertion
assert n_runs < 20_000, "check the number of shots"

# Data to save
save_data_dict = {
    "qubits": qubits,
    "resonators": resonators,
    "shots": n_runs,
    "config": config,
    "readout_operation": readout_operation,
}


###################
#   QUA Program   #
###################

with program() as PROGRAM:
    # I_g, I_g_st, Q_g, Q_g_st, n, _ = qua_declaration(nb_of_qubits=2)
    # I_e, I_e_st, Q_e, Q_e_st, _, _ = qua_declaration(nb_of_qubits=2)
    # I_f, I_f_st, Q_f, Q_f_st, _, _ = qua_declaration(nb_of_qubits=2)

    I_g, I_g_st, Q_g, Q_g_st, n, _ = qua_declaration(resonators)
    I_e, I_e_st, Q_e, Q_e_st, _, _ = qua_declaration(resonators)
    I_f, I_f_st, Q_f, Q_f_st, _, _ = qua_declaration(resonators)

    with for_(n, 0, n < n_runs, n + 1):
        # ground iq blobs for both qubits
        wait(qb_reset_time >> 2)
        align()
        # play("x180", "q2_xy")
        # multiplexed_readout(I_g, I_g_st, Q_g, Q_g_st, resonators=[1, 2], weights="")
        multiplexed_readout(I_g, I_g_st, Q_g, Q_g_st, None, None, resonators, weights=weights)

        # excited iq blobs for both qubits
        align()
        # Wait for the qubit to decay to the ground state in the case of measurement induced transitions
        wait(qb_reset_time >> 2)
        # Play the qubit pi pulses
        play("x180", "q1_xy")
        play("x180", "q2_xy")
        align()
        # multiplexed_readout(I_e, I_e_st, Q_e, Q_e_st, resonators=[1, 2], weights="")
        multiplexed_readout(I_e, I_e_st, Q_e, Q_e_st, None, None, resonators, weights=weights)

        # excited iq blobs for both qubits
        align()
        # Wait for the qubit to decay to the ground state in the case of measurement induced transitions
        wait(qb_reset_time >> 2)
        # Play the qubit pi pulses
        play("x180", "q1_xy")
        play("x180", "q1_xy")
        play("x180", "q2_xy")
        play("x180", "q2_xy")
        align()
        # multiplexed_readout(I_f, I_f_st, Q_f, Q_f_st, resonators=[1, 2], weights="")
        multiplexed_readout(I_f, I_f_st, Q_f, Q_f_st, None, None, resonators, weights=weights)

    with stream_processing():
        # Save all streamed points for plotting the IQ blobs
        for i in range(2):
            I_g_st[i].save_all(f"I_g_q{i + 1}")
            Q_g_st[i].save_all(f"Q_g_q{i + 1}")
            I_e_st[i].save_all(f"I_e_q{i + 1}")
            Q_e_st[i].save_all(f"Q_e_q{i + 1}")
            I_f_st[i].save_all(f"I_f_q{i + 1}")
            Q_f_st[i].save_all(f"Q_f_q{i + 1}")


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
            # fetch data
            results = fetching_tool(job, [
                "I_g_q1", "Q_g_q1", "I_e_q1", "Q_e_q1", "I_f_q1", "Q_f_q1",
                "I_g_q2", "Q_g_q2", "I_e_q2", "Q_e_q2", "I_f_q2", "Q_f_q2",
                ]
            )
            I_g_q1, Q_g_q1, I_e_q1, Q_e_q1, I_f_q1, Q_f_q1, \
                I_g_q2, Q_g_q2, I_e_q2, Q_e_q2, I_f_q2, Q_f_q2 = results.fetch_all()
            
            delta = 1e-5
            I_g_q1 += 1 * delta
            Q_g_q1 += 1 * delta
            I_e_q1 += 0 * delta 
            Q_e_q1 += 0 * delta 
            I_f_q1 += -1 * delta 
            Q_f_q1 += -1 * delta 
            I_g_q2 += 1 * delta 
            Q_g_q2 += 1 * delta 
            I_e_q2 += 0 * delta 
            Q_e_q2 += 0 * delta 
            I_f_q2 += -1 * delta 
            Q_f_q2 += -1 * delta 
            
            # Plot the IQ blobs, rotate them to get the separation along the 'I' quadrature, estimate a threshold between them
            # for state discrimination and derive the fidelity matrix
            fig1, IQ_g_mean_q1, IQ_e_mean_q1, IQ_f_mean_q1, fidelity_q1, *_ \
                = gef_discriminator_mean_points(I_g_q1, Q_g_q1, I_e_q1, Q_e_q1, I_f_q1, Q_f_q1, suptitle="qubit1")
            print(f"Overall fidelity of q1: {100 * fidelity_q1:3.1f}%")

            fig2, IQ_g_mean_q2, IQ_e_mean_q2, IQ_f_mean_q2, fidelity_q2, *_ \
                = gef_discriminator_mean_points(I_g_q2, Q_g_q2, I_e_q2, Q_e_q2, I_f_q2, Q_f_q2, suptitle="qubit2")
            print(f"Overall fidelity of q2: {100 * fidelity_q2:3.1f}%")

            print(f"""
            Update the configuration: (change the keys "q1", "q2" as needed)

            blob_mean = {{
                "q1": {{
                    "g": {IQ_g_mean_q1},
                    "e": {IQ_e_mean_q1},
                    "f": {IQ_f_mean_q1},
                }},
                "q2": {{
                    "g": {IQ_g_mean_q2},
                    "e": {IQ_e_mean_q2},
                    "f": {IQ_f_mean_q2},
                }},
            }}
            """)
            
            # Arrange data to save
            data = {
                "fig1": fig1,
                "fig2": fig2,
                "I_g_q1":I_g_q1,
                "Q_g_q1":Q_g_q1,
                "I_e_q1":I_e_q1,
                "Q_e_q1":Q_e_q1,
                "I_f_q1":I_e_q1,
                "Q_f_q1":Q_e_q1,
                "I_g_q2":I_g_q2,
                "Q_g_q2":Q_g_q2,
                "I_e_q2":I_e_q2,
                "Q_e_q2":Q_e_q2,
                "I_f_q2":I_e_q2,
                "Q_f_q2":Q_e_q2,
            }

            # Save Data
            script_name = Path(__file__).name
            data_handler = DataHandler(root_data_folder=save_dir)
            data_handler.create_data_folder(name=Path(__file__).stem)
            data_handler.additional_files = {script_name: script_name, **default_additional_files}
            data_handler.save_data(data=save_data_dict, name="iq_blobs_gef_example")

        except Exception as e:
            print(f"An exception occurred: {e}")

        finally:
            qm.close()
            print("Experiment QM is now closed")
            plt.show(block=True)

# %%
