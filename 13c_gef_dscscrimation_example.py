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
from macros import qua_declaration, multiplexed_readout, gef_state_discriminator_blob_mean
from qualang_tools.results.data_handler import DataHandler

###################
# The QUA program #
###################

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

blob_mean = {
    "q1": {
        "g": [1e-4, 0.0],
        "e": [0.0, 0.0],
        "f": [-1e-4, 0.0],
    },
    "q2": {
        "g": [0.0, 1e-4],
        "e": [0.0, 0.0],
        "f": [0.0, -1e-4],
    },
}


###################
#   QUA Program   #
###################

with program() as PROGRAM:
    I, I_st, Q, Q_st, n, _ = qua_declaration(resonators)
    state = [declare(bool, size=3) for _ in range(len(resonators))]
    state_st = [declare_stream() for _ in range(len(resonators))]
    
    with for_(n, 0, n < n_runs, n + 1):
        # ground iq blobs for both qubits
        wait(qb_reset_time >> 2)
        multiplexed_readout(I, I_st, Q, Q_st, None, None, resonators, weights="")
        for i, q in enumerate([1, 2]):
            gef_state_discriminator_blob_mean(I[i], Q[i], state[i], state_st[i], blob_mean[f"q{q}"])

    with stream_processing():
        # Save all streamed points for plotting the IQ blobs
        for i in range(2):
            I_st[i].average().save(f"I_q{i + 1}")
            Q_st[i].average().save(f"Q_q{i + 1}")
            state_st[i].boolean_to_int().buffer(3).average().save(f"state_q{i + 1}")


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
                "I_q1", "Q_q1", "state_q1", "I_q2", "Q_q2", "state_q2",
                ]
            )
            I_q1, Q_q1, state_q1, I_q2, Q_q2, state_q2 = results.fetch_all()

            print("state_q1 (g, e, f) :", state_q1)
            print("state_q2 (g, e, f) :", state_q2)

            # Save Data
            script_name = Path(__file__).name
            data_handler = DataHandler(root_data_folder=save_dir)
            data_handler.create_data_folder(name=Path(__file__).stem)
            data_handler.additional_files = {script_name: script_name, **default_additional_files}
            data_handler.save_data(data=save_data_dict, name="iq_blobs_gef")

        except Exception as e:
            print(f"An exception occurred: {e}")

        finally:
            qm.close()
            print("Experiment QM is now closed")
            plt.show(block=True)



# %%