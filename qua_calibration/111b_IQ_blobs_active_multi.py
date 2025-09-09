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
from configuration_mw_fem import *
import matplotlib.pyplot as plt
from qualang_tools.results import fetching_tool
from macros import qua_declaration, multiplexed_readout, active_reset
from qualang_tools.results import progress_counter
from qualang_tools.results.data_handler import DataHandler
from qualang_tools.analysis import two_state_discriminator
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')

##################
#   Parameters   #
qubits = ["q1_xy", "q2_xy"]
resonators = ["rr1", "rr2"]
Qubit1 = 1
Qubit2 = 2
idx = 0
##################
# Parameters Definition
n_runs = 10_000  # Number of runs
reset_method = "active_reset"  # "active_reset" or "thermalization"
max_tries = 1000


midcircuit_ge_threshold = {
    "rr1": -5.809e-06,
    "rr2": -8.206e-06,
}

midcircuit_ge_threshold_g = {
    "rr1": -1.37e-5, #-1.8e-5,
    "rr2": -1.2e-5,
}

midcircuit_ge_threshold_e = {
    "rr1": 8e-7, # 3e-6,
    "rr2": -4e-6,
}



# Data to save
save_data_dict = {
    "qubits": qubits,
    "shots": n_runs,
    "config": config,
}

###################
# The QUA program #
###################
with program() as PROGRAM:
    I_g, I_g_st, Q_g, Q_g_st, n, n_st = qua_declaration(nb_of_qubits=2)
    I_e, I_e_st, Q_e, Q_e_st, _, _ = qua_declaration(nb_of_qubits=2)

    with for_(n, 0, n < n_runs, n + 1):
        save(n, n_st)
        # GROUND iq blobs for both qubits
        if reset_method == "thermalization":
            wait(thermalization_time * u.ns)
        else:
            # Active reset of the qubit to the |g> state
            active_reset(
                threshold=midcircuit_ge_threshold_e[resonators[idx]],
                qubit=qubits[idx],
                resonator=resonators[idx],
                max_tries=max_tries,
            )

        align()
        # Measure the state of the resonators
        multiplexed_readout(I_g, I_g_st, Q_g, Q_g_st, resonators=[1, 2], weights="rotated_")

        align()

        # EXCITED iq blobs for both qubits
        if reset_method == "thermalization":
            wait(thermalization_time * u.ns)
        else:
            # Active reset of the qubit to the |g> state
            active_reset(
                threshold=midcircuit_ge_threshold_e[resonators[idx]],
                qubit=qubits[idx],
                resonator=resonators[idx],
                max_tries=max_tries,
            )
        # # Play the qubit pi pulses
        play("x180", qubits[idx])

        align()
        # Measure the state of the resonators
        multiplexed_readout(I_e, I_e_st, Q_e, Q_e_st, resonators=[1, 2], weights="rotated_")

    with stream_processing():
        n_st.save("iteration")
        # Save all streamed points for plotting the IQ blobs
        for i in range(2):
            I_g_st[i].save_all(f"I_g_q{i}")
            Q_g_st[i].save_all(f"Q_g_q{i}")
            I_e_st[i].save_all(f"I_e_q{i}")
            Q_e_st[i].save_all(f"Q_e_q{i}")

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
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, PROGRAM, simulation_config)
    # Get the simulated samples
    samples = job.get_simulated_samples()
    # Plot the simulated samples
    samples.con1.plot()
    # Get the waveform report object
    waveform_report = job.get_simulated_waveform_report()
    # Cast the waveform report to a python dictionary
    waveform_dict = waveform_report.to_dict()
    # Visualize and save the waveform report
    waveform_report.create_plot(samples, plot=True, save_path=str(Path(__file__).resolve()))
else:
    try:
        # Open the quantum machine
        qm = qmm.open_qm(config)
        # Send the QUA program to the OPX, which compiles and executes it
        job = qm.execute(PROGRAM)
        results = fetching_tool(job, ["iteration"], mode="live")

        while results.is_processing():
            iteration = results.fetch_all()
            progress_counter(iteration[0], n_runs, start_time=results.start_time)

        # fetch data
        results = fetching_tool(job, ["I_g_q0", "Q_g_q0", "I_e_q0", "Q_e_q0", "I_g_q1", "Q_g_q1", "I_e_q1", "Q_e_q1"])
        I_g_q1, Q_g_q1, I_e_q1, Q_e_q1, I_g_q2, Q_g_q2, I_e_q2, Q_e_q2 = results.fetch_all()
        # Plot the IQ blobs, rotate them to get the separation along the 'I' quadrature, estimate a threshold between them
        # for state discrimination and derive the fidelity matrix
        two_state_discriminator(I_g_q1, Q_g_q1, I_e_q1, Q_e_q1, True, True)
        plt.suptitle(f"qubit {Qubit1}")
        fig1 = plt.gcf()
        two_state_discriminator(I_g_q2, Q_g_q2, I_e_q2, Q_e_q2, True, True)
        plt.suptitle(f"qubit {Qubit2}")
        fig2 = plt.gcf()

        # Save results
        script_name = Path(__file__).name
        data_handler = DataHandler(root_data_folder=save_dir)
        save_data_dict.update({"I_g_q1_data": I_g_q1})
        save_data_dict.update({"Q_g_q1_data": Q_g_q1})
        save_data_dict.update({"I_e_q1_data": I_e_q1})
        save_data_dict.update({"Q_e_q1_data": Q_e_q1})
        save_data_dict.update({"I_g_q2_data": I_g_q2})
        save_data_dict.update({"Q_g_q2_data": Q_g_q2})
        save_data_dict.update({"I_e_q2_data": I_e_q2})
        save_data_dict.update({"Q_e_q2_data": Q_e_q2})
        save_data_dict.update({"fig_g": fig1, "fig_e": fig2})
        data_handler.additional_files = {script_name: script_name, **default_additional_files}
        data_handler.save_data(data=save_data_dict, name="_".join(script_name.split("_")[1:]).split(".")[0])

    except Exception as e:
        print(f"An exception occurred: {e}")

    finally:
        qm.close()
        print("Experiment QM is now closed")
        plt.show(block=False)

# %%
