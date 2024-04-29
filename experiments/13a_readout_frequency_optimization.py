# %%
"""
        READOUT OPTIMISATION: FREQUENCY
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

from qm.QuantumMachinesManager import QuantumMachinesManager
from qm.qua import *
from qm import SimulationConfig

# from configuration import *
from configuration_with_octave import *
import matplotlib.pyplot as plt
from qualang_tools.loops import from_array
from qualang_tools.results import fetching_tool, progress_counter
from macros import multiplexed_readout, qua_declaration
import warnings
import matplotlib
from qualang_tools.results.data_handler import DataHandler
import time

matplotlib.use("TKAgg")
warnings.filterwarnings("ignore")

###################
# The QUA program #
###################
n_avg = 4000
# The frequency sweep around the resonators' frequency "resonator_IF_q"
f_vec = np.arange(-10e6, 10e6, 0.1e6)

with program() as ro_freq_opt:
    Ig, Ig_st, Qg, Qg_st, n, n_st = qua_declaration(nb_of_qubits=2)
    Ie, Ie_st, Qe, Qe_st, _, _ = qua_declaration(nb_of_qubits=2)
    df = declare(int)  # QUA variable for the readout frequency

    with for_(n, 0, n < n_avg, n + 1):
        with for_(*from_array(df, f_vec)):
            # Update the frequency of the two resonator elements
            update_frequency("rr1", df + resonator_IF_q1)
            update_frequency("rr2", df + resonator_IF_q2)

            # Reset both qubits to ground
            wait(thermalization_time * u.ns)
            # Measure the ground IQ blobs
            multiplexed_readout(Ig, Ig_st, Qg, Qg_st, resonators=[1, 2], weights="rotated_")

            align()
            # Reset both qubits to ground
            wait(thermalization_time * u.ns)
            # Measure the excited IQ blobs
            play("x180", "q1_xy")
            play("x180", "q2_xy")
            align()
            multiplexed_readout(Ie, Ie_st, Qe, Qe_st, resonators=[1, 2], weights="rotated_")
        # Save the averaging iteration to get the progress bar
        save(n, n_st)

    with stream_processing():
        n_st.save("iteration")
        for i in range(2):
            # all shots
            Ig_st[i].buffer(len(f_vec)).buffer(n_avg).save(f"Ig{i}")
            Qg_st[i].buffer(len(f_vec)).buffer(n_avg).save(f"Qg{i}")
            Ie_st[i].buffer(len(f_vec)).buffer(n_avg).save(f"Ie{i}")
            Qe_st[i].buffer(len(f_vec)).buffer(n_avg).save(f"Qe{i}")
            # mean values
            Ig_st[i].buffer(len(f_vec)).average().save(f"Ig{i}_avg")
            Qg_st[i].buffer(len(f_vec)).average().save(f"Qg{i}_avg")
            Ie_st[i].buffer(len(f_vec)).average().save(f"Ie{i}_avg")
            Qe_st[i].buffer(len(f_vec)).average().save(f"Qe{i}_avg")
            # variances to get the SNR
            (
                ((Ig_st[i].buffer(len(f_vec)) * Ig_st[i].buffer(len(f_vec))).average())
                - (Ig_st[i].buffer(len(f_vec)).average() * Ig_st[i].buffer(len(f_vec)).average())
            ).save(f"Ig{i}_var")
            (
                ((Qg_st[i].buffer(len(f_vec)) * Qg_st[i].buffer(len(f_vec))).average())
                - (Qg_st[i].buffer(len(f_vec)).average() * Qg_st[i].buffer(len(f_vec)).average())
            ).save(f"Qg{i}_var")
            (
                ((Ie_st[i].buffer(len(f_vec)) * Ie_st[i].buffer(len(f_vec))).average())
                - (Ie_st[i].buffer(len(f_vec)).average() * Ie_st[i].buffer(len(f_vec)).average())
            ).save(f"Ie{i}_var")
            (
                ((Qe_st[i].buffer(len(f_vec)) * Qe_st[i].buffer(len(f_vec))).average())
                - (Qe_st[i].buffer(len(f_vec)).average() * Qe_st[i].buffer(len(f_vec)).average())
            ).save(f"Qe{i}_var")

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config)

###########################
# Run or Simulate Program #
###########################

simulate = False
save_data = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, ro_freq_opt, simulation_config)
    job.get_simulated_samples().con1.plot()

else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(ro_freq_opt)
    # Get results from QUA program
    data_list = [
        "Ig0_avg",
        "Qg0_avg",
        "Ie0_avg",
        "Qe0_avg",
        "Ig0_var",
        "Qg0_var",
        "Ie0_var",
        "Qe0_var",
        "Ig1_avg",
        "Qg1_avg",
        "Ie1_avg",
        "Qe1_avg",
        "Ig1_var",
        "Qg1_var",
        "Ie1_var",
        "Qe1_var",
        "iteration",
    ]
    results = fetching_tool(job, data_list=data_list, mode="live")
    while results.is_processing():
        start_time = results.get_start_time()
        (
            Ig0_avg,
            Qg0_avg,
            Ie0_avg,
            Qe0_avg,
            Ig0_var,
            Qg0_var,
            Ie0_var,
            Qe0_var,
            Ig1_avg,
            Qg1_avg,
            Ie1_avg,
            Qe1_avg,
            Ig1_var,
            Qg1_var,
            Ie1_var,
            Qe1_var,
            iteration,
        ) = results.fetch_all()
        # Progress bar
        progress_counter(iteration, n_avg, start_time=results.get_start_time())
        # calculate the elapsed time
        elapsed_time = time.time() - start_time
        # Derive the SNR
        Z0 = (Ie0_avg - Ig0_avg) + 1j * (Qe0_avg - Qg0_avg)
        var0 = (Ig0_var + Qg0_var + Ie0_var + Qe0_var) / 4
        SNR0 = ((np.abs(Z0)) ** 2) / (2 * var0)
        Z1 = (Ie1_avg - Ig1_avg) + 1j * (Qe1_avg - Qg1_avg)
        var1 = (Ig1_var + Qg1_var + Ie1_var + Qe1_var) / 4
        SNR1 = ((np.abs(Z1)) ** 2) / (2 * var1)
        # Plot results
        plt.suptitle("Readout frequency optimization")
        plt.subplot(121)
        plt.cla()
        plt.plot(f_vec / u.MHz, SNR0, ".-")
        plt.title(f"Qubit 1 around {resonator_IF_q1 / u.MHz} MHz")
        plt.xlabel("Readout frequency detuning [MHz]")
        plt.ylabel("SNR")
        plt.grid("on")
        plt.subplot(122)
        plt.cla()
        plt.plot(f_vec / u.MHz, SNR1, ".-")
        plt.title(f"Qubit 2 around {resonator_IF_q2 / u.MHz} MHz")
        plt.xlabel("Readout frequency detuning [MHz]")
        plt.grid("on")
        plt.pause(0.1)
        print(f"The optimal readout frequency is {f_vec[np.argmax(SNR0)] + resonator_IF_q1} Hz (SNR={max(SNR0)})")
        print(f"The optimal readout frequency is {f_vec[np.argmax(SNR1)] + resonator_IF_q2} Hz (SNR={max(SNR1)})")

    results_end = fetching_tool(
        job,
        data_list=[
            "Ig0",
            "Qg0",
            "Ie0",
            "Qe0",
            "Ig0_avg",
            "Qg0_avg",
            "Ie0_avg",
            "Qe0_avg",
            "Ig0_var",
            "Qg0_var",
            "Ie0_var",
            "Qe0_var",
            "Ig1",
            "Qg1",
            "Ie1",
            "Qe1",
            "Ig1_avg",
            "Qg1_avg",
            "Ie1_avg",
            "Qe1_avg",
            "Ig1_var",
            "Qg1_var",
            "Ie1_var",
            "Qe1_var",
            "iteration",
        ],
    )

    (
        Ig0,
        Qg0,
        Ie0,
        Qe0,
        Ig0_avg,
        Qg0_avg,
        Ie0_avg,
        Qe0_avg,
        Ig0_var,
        Qg0_var,
        Ie0_var,
        Qe0_var,
        Ig1,
        Qg1,
        Ie1,
        Qe1,
        Ig1_avg,
        Qg1_avg,
        Ie1_avg,
        Qe1_avg,
        Ig1_var,
        Qg1_var,
        Ie1_var,
        Qe1_var,
        iteration,
    ) = results_end.fetch_all()

    # swap the axes 0 & 1
    Ig0_swap = Ig0.swapaxes(0, 1)
    Qg0_swap = Qg0.swapaxes(0, 1)
    Ie0_swap = Ie0.swapaxes(0, 1)
    Qe0_swap = Qe0.swapaxes(0, 1)
    Ig1_swap = Ig1.swapaxes(0, 1)
    Qg1_swap = Qg1.swapaxes(0, 1)
    Ie1_swap = Ie1.swapaxes(0, 1)
    Qe1_swap = Qe1.swapaxes(0, 1)

    if save_data:
        # Arrange data to save
        data = {
            "fig_live": fig,
            "f_vec": f_vec,
            "Ig0_swap": Ig0_swap,
            "Qg0_swap": Qg0_swap,
            "Ie0_swap": Ie0_swap,
            "Qe0_swap": Qe0_swap,
            "Ig1_swap": Ig1_swap,
            "Qg1_swap": Qg1_swap,
            "Ie1_swap": Ie1_swap,
            "Qe1_swap": Qe1_swap,
            "Ig0_avg": Ig0_avg,
            "Qg0_avg": Qg0_avg,
            "Ie0_avg": Ie0_avg,
            "Qe0_avg": Qe0_avg,
            "Ig0_var": Ig0_var,
            "Qg0_var": Qg0_var,
            "Ie0_var": Ie0_var,
            "Qe0_var": Qe0_var,
            "Ig1_avg": Ig1_avg,
            "Qg1_avg": Qg1_avg,
            "Ie1_avg": Ie1_avg,
            "Qe1_avg": Qe1_avg,
            "Ig1_var": Ig1_var,
            "Qg1_var": Qg1_var,
            "Ie1_var": Ie1_var,
            "Qe1_var": Qe1_var,
            "iteration": np.array([n]),  # convert int to np.array of int
            "elapsed_time": np.array([elapsed_time]),  # convert float to np.array of float
        }

        # Initialize the DataHandler
        script_name = Path(__file__).name
        data_handler = DataHandler(root_data_folder=save_dir)
        data_handler.create_data_folder(name=Path(__file__).stem)
        data_handler.additional_files = {
            script_name: script_name,
            "configuration_with_octave.py": "configuration_with_octave.py",
            "calibration_db.json": "calibration_db.json",
            "optimal_weights.npz": "optimal_weights.npz",
        }
        # Save results
        data_folder = data_handler.save_data(data=data)

    # Close the quantum machines at the end
    qm.close()

# %%
