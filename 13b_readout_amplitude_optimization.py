# %%
"""
        READOUT OPTIMISATION: AMPLITUDE
The sequence consists in measuring the state of the resonator after thermalization (qubit in |g>) and after
playing a pi pulse to the qubit (qubit in |e>) successively while sweeping the readout amplitude.
The 'I' & 'Q' quadratures when the qubit is in |g> and |e> are extracted to derive the readout fidelity.
The optimal readout amplitude is chosen as to maximize the readout fidelity.

Prerequisites:
    - Having found the resonance frequency of the resonator coupled to the qubit under study (resonator_spectroscopy).
    - Having calibrated qubit pi pulse (x180) by running qubit, spectroscopy, rabi_chevron, power_rabi and updated the config.
    - Having calibrated the readout frequency and updated the configuration.

Next steps before going to the next node:
    - Update the readout amplitude (readout_amp_q) in the configuration.
"""

from qm.QuantumMachinesManager import QuantumMachinesManager
from qm.qua import *
from qm import SimulationConfig

from configuration import *
# from configuration_with_octave import *
import matplotlib.pyplot as plt
from qualang_tools.loops import from_array
from qualang_tools.results import fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.analysis import two_state_discriminator
from qualang_tools.results import progress_counter
from macros import qua_declaration, multiplexed_readout
import warnings
import matplotlib
from qualang_tools.results.data_handler import DataHandler
import time

matplotlib.use("TKAgg")
warnings.filterwarnings("ignore")

###################
# The QUA program #
###################

n_runs = 100
# The readout amplitude sweep (as a pre-factor of the readout amplitude)
a_min = 0.9
a_max = 1.1
da = 0.01
a_vec = np.arange(a_min, a_max + da / 2, da)  # The amplitude vector +da/2 to add a_max to the scan


with program() as ro_amp_opt:
    I_g, I_g_st, Q_g, Q_g_st, n, _ = qua_declaration(nb_of_qubits=2)
    I_e, I_e_st, Q_e, Q_e_st, _, _ = qua_declaration(nb_of_qubits=2)
    counter = declare(int, value=0)  # Counter for the progress bar
    counter_st = declare_stream()  # Stream for the counter variable
    a = declare(fixed)  # QUA variable for the readout amplitude

    with for_(*from_array(a, a_vec)):
        # Save the counter to get the progress bar
        save(counter, counter_st)
        with for_(n, 0, n < n_runs, n + 1):
            # Reset both qubits to ground
            wait(thermalization_time * u.ns)
            # Measure the ground IQ blobs
            multiplexed_readout(I_g, I_g_st, Q_g, Q_g_st, resonators=[1, 2], weights="rotated_", amplitude=a)

            align()
            # Reset both qubits to ground
            wait(thermalization_time * u.ns)
            # Measure the excited IQ blobs
            play("x180", "q1_xy")
            play("x180", "q2_xy")
            align()
            multiplexed_readout(I_e, I_e_st, Q_e, Q_e_st, resonators=[1, 2], weights="rotated_", amplitude=a)
        # Increment the counter
        assign(counter, counter + 1)

    with stream_processing():
        # Save all streamed points for plotting the IQ blobs
        for i in range(2):
            I_g_st[i].buffer(n_runs).buffer(len(a_vec)).save(f"I_g_q{i}")
            Q_g_st[i].buffer(n_runs).buffer(len(a_vec)).save(f"Q_g_q{i}")
            I_e_st[i].buffer(n_runs).buffer(len(a_vec)).save(f"I_e_q{i}")
            Q_e_st[i].buffer(n_runs).buffer(len(a_vec)).save(f"Q_e_q{i}")
        counter_st.save("iteration")

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
    job = qmm.simulate(config, ro_amp_opt, simulation_config)
    job.get_simulated_samples().con1.plot()

else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(ro_amp_opt)  # execute QUA program
    # Prepare the figure for live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)
    # Get results from QUA program
    results = fetching_tool(job, data_list=["iteration"], mode="live")
    # Get progress counter to monitor runtime of the program
    while results.is_processing():
        start_time = results.get_start_time()
        # Fetch results
        iteration = results.fetch_all()
        # Progress bar
        progress_counter(iteration[0], len(a_vec), start_time=results.get_start_time())
        # calculate the elapsed time
        elapsed_time = time.time() - start_time

    # Fetch the results at the end
    results = fetching_tool(job, ["I_g_q0", "Q_g_q0", "I_e_q0", "Q_e_q0", "I_g_q1", "Q_g_q1", "I_e_q1", "Q_e_q1"])
    I_g_q1, Q_g_q1, I_e_q1, Q_e_q1, I_g_q2, Q_g_q2, I_e_q2, Q_e_q2 = results.fetch_all()
    # Process the data
    fidelity_vec = [[], []]
    for i in range(len(a_vec)):
        _, _, fidelity_q1, _, _, _, _ = two_state_discriminator(
            I_g_q1[i], Q_g_q1[i], I_e_q1[i], Q_e_q1[i], b_print=False, b_plot=False
        )
        _, _, fidelity_q2, _, _, _, _ = two_state_discriminator(
            I_g_q2[i], Q_g_q2[i], I_e_q2[i], Q_e_q2[i], b_print=False, b_plot=False
        )
        fidelity_vec[0].append(fidelity_q1)
        fidelity_vec[1].append(fidelity_q2)

    # Plot the data
    plt.suptitle("Readout amplitude optimization")
    plt.subplot(121)
    plt.plot(a_vec * readout_amp_q1, fidelity_vec[0], ".-")
    plt.title("Qubit 1")
    plt.xlabel("Readout amplitude [V]")
    plt.ylabel("Fidelity [%]")
    plt.subplot(122)
    plt.title("Qubit 2")
    plt.plot(a_vec * readout_amp_q2, fidelity_vec[1], ".-")
    plt.xlabel("Readout amplitude [V]")
    plt.ylabel("Fidelity [%]")
    plt.tight_layout()

    plt.show()

    # Close the quantum machines at the end
    qm.close()

    if save_data:
        # Arrange data to save
        data = {
            "fig_live": fig,
            "a_vec": a_vec,
            "I_g_q1":I_g_q1,
            "Q_g_q1":Q_g_q1,
            "I_e_q1":I_e_q1,
            "Q_e_q1":Q_e_q1,
            "I_g_q2":I_g_q2,
            "Q_g_q2":Q_g_q2,
            "I_e_q2":I_e_q2,
            "Q_e_q2":Q_e_q2,
            "iteration": np.array([n]),  # convert int to np.array of int
            "elapsed_time": np.array([elapsed_time]),  # convert float to np.array of float
        }
        # Save Data
        script_name = Path(__file__).name
        data_handler = DataHandler(root_data_folder=save_dir)
        data_handler.create_data_folder(name=Path(__file__).stem)
        data_handler.additional_files = {script_name: script_name, **default_additional_files}
        data_folder = data_handler.save_data(data=data)


# %%
