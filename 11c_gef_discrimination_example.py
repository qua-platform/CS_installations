# %%
"""
        GEF_DISCRIMINATION_EXAMPLE
This sequence demonstrates a usage example of gef_state_discriminator_blob_mean.

Prerequisites:
    - Performed IQ_blob_gef.py
    - Having found the blob means (average point of each blob) and added them in the configuration as below:
        blob_mean = {
            "q1": {
                "g": {numpy array of IQ_g_mean_q1},
                "e": {numpy array of IQ_e_mean_q1},
                "f": {numpy array of IQ_f_mean_q1},
            },
            "q2": {
                "g": {numpy array of IQ_g_mean_q2},
                "e": {numpy array of IQ_e_mean_q2},
                "f": {numpy array of IQ_f_mean_q2},
            },
        }
"""

from qm.QuantumMachinesManager import QuantumMachinesManager
from qm.qua import *
from qm.simulate import SimulationConfig

from configuration_with_octave import *
# from configuration import *
import matplotlib.pyplot as plt
from qualang_tools.results import fetching_tool
from macros import qua_declaration, multiplexed_readout
import matplotlib
from qualang_tools.results.data_handler import DataHandler
from macros import gef_state_discriminator_blob_mean

import time

matplotlib.use("TKAgg")

###################
# The QUA program #
###################
n_runs = 1000  # Number of runs

with program() as iq_blobs:
    I_g, I_g_st, Q_g, Q_g_st, n, _ = qua_declaration(nb_of_qubits=2)
    I_e, I_e_st, Q_e, Q_e_st, _, _ = qua_declaration(nb_of_qubits=2)
    I_f, I_f_st, Q_f, Q_f_st, _, _ = qua_declaration(nb_of_qubits=2)

    with for_(n, 0, n < n_runs, n + 1):
        # ground iq blobs for both qubits
        wait(thermalization_time * u.ns)
        align()
        # play("x180", "q2_xy")
        multiplexed_readout(I_g, I_g_st, Q_g, Q_g_st, resonators=[1, 2], weights="")

        # excited iq blobs for both qubits
        align()
        # Wait for the qubit to decay to the ground state in the case of measurement induced transitions
        wait(thermalization_time * u.ns)
        # Play the qubit pi pulses
        play("x180", "q1_xy")
        play("x180", "q2_xy")
        align()
        multiplexed_readout(I_e, I_e_st, Q_e, Q_e_st, resonators=[1, 2], weights="")

        # excited iq blobs for both qubits
        align()
        # Wait for the qubit to decay to the ground state in the case of measurement induced transitions
        wait(thermalization_time * u.ns)
        # Play the qubit pi pulses
        play("x180", "q1_xy")
        play("x180", "q1_xy_ef")
        play("x180", "q2_xy")
        play("x180", "q2_xy_ef")
        align()
        multiplexed_readout(I_f, I_f_st, Q_f, Q_f_st, resonators=[1, 2], weights="")

    with stream_processing():
        # Save all streamed points for plotting the IQ blobs
        for i in range(2):
            I_g_st[i].save_all(f"I_g_q{i + 1}")
            Q_g_st[i].save_all(f"Q_g_q{i + 1}")
            I_e_st[i].save_all(f"I_e_q{i + 1}")
            Q_e_st[i].save_all(f"Q_e_q{i + 1}")
            I_f_st[i].save_all(f"I_f_q{i + 1}")
            Q_f_st[i].save_all(f"Q_f_q{i + 1}")

with program() as iq_blobs:
    I, I_st, Q, Q_st, n, _ = qua_declaration(nb_of_qubits=2)
    state = [declare(bool, size=3) for _ in range(2)]
    state_st = [declare_stream() for _ in range(2)]
    
    with for_(n, 0, n < n_runs, n + 1):
        # ground iq blobs for both qubits
        multiplexed_readout(I, I_st, Q, Q_st, resonators=[1, 2], weights="")
        for i, q in enumerate([1, 2]):
            gef_state_discriminator_blob_mean(I[i], Q[i], state[i], state_st[i], blob_mean[f"q{q}"])
        
        wait(thermalization_time * u.ns)

    with stream_processing():
        # Save all streamed points for plotting the IQ blobs
        for i in range(2):
            I_st[i].average().save(f"I_q{i + 1}")
            Q_st[i].average().save(f"Q_q{i + 1}")
            state_st[i].boolean_to_int().buffer(3).average().save(f"state_q{i + 1}")


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(
    host=qop_ip,
    port=qop_port,
    cluster_name=cluster_name,
    octave=octave_config,
)

###########################
# Run or Simulate Program #
###########################

simulate = False
save_data = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, iq_blobs, simulation_config)
    job.get_simulated_samples().con1.plot()

else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(iq_blobs)
    # fetch data
    results = fetching_tool(job, [
        "I_q1", "Q_q1", "state_q1", "I_q2", "Q_q2", "state_q2",
        ]
    )
    I_q1, Q_q1, state_q1, I_q2, Q_q2, state_q2 = results.fetch_all()

    print("state_q1 (g, e, f) :", state_q1)
    print("state_q2 (g, e, f) :", state_q2)

    # Close the quantum machines at the end
    qm.close()

    if save_data:
        # Arrange data to save
        data = {
            "I_q1" : I_q1,
            "Q_q1" : Q_q1,
            "state_q1" : state_q1,
            "I_q2" : I_q2,
            "Q_q2" : Q_q2,
            "state_q2" : state_q2,
        }
        # Save Data
        script_name = Path(__file__).name
        data_handler = DataHandler(root_data_folder=save_dir)
        data_handler.create_data_folder(name=Path(__file__).stem)
        data_handler.additional_files = {script_name: script_name, **default_additional_files}
        data_folder = data_handler.save_data(data=data)

# %%