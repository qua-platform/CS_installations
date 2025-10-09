"""
        READOUT OPTIMISATION: DURATION
This sequence involves measuring the state of the resonator in two scenarios: first, after thermalization
(with the qubit in the |g> state) and then after applying a pi pulse to the qubit (transitioning the qubit to the
|e> state). The "demod.accumulated" method is employed to assess the state of the resonator over varying durations.
Reference: (https://docs.quantum-machines.co/0.1/qm-qua-sdk/docs/Guides/features/?h=accumulated#accumulated-demodulation)
The average I & Q quadratures for the qubit states |g> and |e>, along with their variances, are extracted to determine
the Signal-to-Noise Ratio (SNR). The readout duration that offers the highest SNR is identified as the optimal choice.
Note: To observe the resonator's behavior during ringdown, the integration weights length should exceed the readout_pulse length.

Prerequisites:
    - Determination of the resonator's resonance frequency when coupled to the qubit in focus (referred to as "resonator_spectroscopy").
    - Calibration of the qubit pi pulse (x180) using methods like qubit spectroscopy, rabi_chevron, and power_rabi,
      followed by an update to the configuration.
    - Calibration of both the readout frequency and amplitude, with subsequent configuration updates.

Before proceeding to the next node:
    - Adjust the readout duration setting, labeled as "readout_len", in the configuration.
"""
import numpy as np
from qm.qua import *
from qm import QuantumMachinesManager
from qualang_tools.loops import from_array
from qualang_tools.results import fetching_tool, progress_counter
from qualang_tools.analysis import two_state_discriminator
from qualang_tools.plot import interrupt_on_close
from qm_saas import QmSaas, QOPVersion
from qm import SimulationConfig
import matplotlib.pyplot as plt
from pathlib import Path
from scipy.signal import savgol_filter
from qualang_tools.units import unit
u = unit(coerce_to_integer=True)
from scipy import signal
from qualang_tools.results.data_handler import DataHandler
from macros import multiplexed_parser, mp_result_names, mp_fetch_all

if False:
    from configurations.DA_5Q.OPX1000config import *
else:
    from configurations.DB_6Q.OPX1000config import *

####################
# Helper functions #
####################
def update_readout_length(res_key_subset, new_readout_length, ringdown_length):
    for rk in res_key_subset:
        ri = int(rk.strip("r"))
        config["pulses"][f"readout_pulse_{ri}"]["length"] = new_readout_length
        config["integration_weights"][f"cosine_weights_{ri}"] = {
            "cosine": [(1.0, new_readout_length + ringdown_length)],
            "sine": [(0.0, new_readout_length + ringdown_length)],
        }
        config["integration_weights"][f"sine_weights_{ri}"] = {
            "cosine": [(0.0, new_readout_length + ringdown_length)],
            "sine": [(1.0, new_readout_length + ringdown_length)],
        }
        config["integration_weights"][f"minus_sine_weights_{ri}"] = {
            "cosine": [(0.0, new_readout_length + ringdown_length)],
            "sine": [(-1.0, new_readout_length + ringdown_length)],
        }


##################
#   Parameters   #
##################
# Parameters Definition
# ---- Multiplexed program parameters ---- #
n_avg = 1000
multiplexed = True
qubit_keys = ["q0", "q1"] # Almost certainly will run into resource issues if you try to do more than 2 at once.
required_parameters = ["qubit_key", "qubit_relaxation", "resonator_key", "resonator_relaxation", "resonator_IF", "readout_amp"]
qub_key_subset, qubit_relaxation, res_key_subset, resonator_relaxation, resonator_IF, readout_amp = multiplexed_parser(qubit_keys, multiplexed_parameters.copy(), required_parameters)

qub_relaxation = qubit_relaxation//4  # ns to clock cycles
res_relaxation = resonator_relaxation//4  # ns to clock cycles

# Set maximum readout duration for this scan and update the configuration accordingly
readout_length = 5 * u.us  # Readout pulse duration
ringdown_length = 0 * u.us  # integration time after readout pulse to observe the ringdown of the resonator
update_readout_length(res_key_subset, readout_length, ringdown_length)
# Set the accumulated demod parameters
division_length = 10  # Size of each demodulation slice in clock cycles
number_of_divisions = int((readout_length + ringdown_length) / (4 * division_length))
print("Integration weights chunk-size length in clock cycles:", division_length)
print("The readout has been sliced in the following number of divisions", number_of_divisions)

# Time axis for the plots at the end
x_plot = np.arange(division_length * 4, readout_length + ringdown_length + 1, division_length * 4)

# Data to save
save_data_dict = {
    "n_avg": n_avg,
    "resonator_keys": res_key_subset,
    "qubit_keys": qub_key_subset,
    "readout_len": readout_length,
    "ringdown_len": ringdown_length,
    "division_length": division_length,
    "number_of_divisions": number_of_divisions,
    "config": config,
}
save_dir = Path(__file__).resolve().parent / "data"

###################
# The QUA program #
###################
with program() as ro_duration_opt:
    n = declare(int)
    II = [declare(fixed, size=number_of_divisions) for _ in range(len(qub_key_subset))]
    IQ = [declare(fixed, size=number_of_divisions) for _ in range(len(qub_key_subset))]
    QI = [declare(fixed, size=number_of_divisions) for _ in range(len(qub_key_subset))]
    QQ = [declare(fixed, size=number_of_divisions) for _ in range(len(qub_key_subset))]
    I = [declare(fixed, size=number_of_divisions) for _ in range(len(qub_key_subset))]
    Q = [declare(fixed, size=number_of_divisions) for _ in range(len(qub_key_subset))]
    ind = [declare(int) for _ in range(len(qub_key_subset))]

    n_st = declare_stream()
    I_g_st = [declare_stream() for _ in range(len(res_key_subset))]
    Q_g_st = [declare_stream() for _ in range(len(res_key_subset))]
    I_e_st = [declare_stream() for _ in range(len(res_key_subset))]
    Q_e_st = [declare_stream() for _ in range(len(res_key_subset))]

    with for_(n, 0, n < n_avg, n + 1):
        for j in range(len(qub_key_subset)):  # A Python for loop so it unravels and executes in parallel, not sequentially
            # Measure the ground state.
            # With demod.accumulated, the results are QUA vectors with 1 point for each accumulated chunk
            measure(
                "readout",
                res_key_subset[j],
                demod.accumulated("cos", II[j], division_length, "out1"),
                demod.accumulated("sin", IQ[j], division_length, "out2"),
                demod.accumulated("minus_sin", QI[j], division_length, "out1"),
                demod.accumulated("cos", QQ[j], division_length, "out2"),
            )
            # Save the QUA vectors to their corresponding streams
            with for_(ind[j], 0, ind[j] < number_of_divisions, ind[j] + 1):
                assign(I[j][ind[j]], II[j][ind[j]] + IQ[j][ind[j]])
                save(I[j][ind[j]], I_g_st[j])
                assign(Q[j][ind[j]], QQ[j][ind[j]] + QI[j][ind[j]])
                save(Q[j][ind[j]], Q_g_st[j])
            # Wait for the qubit to decay to the ground state
            align(qub_key_subset[j], res_key_subset[j])
            wait(qub_relaxation[j], qub_key_subset[j])
            wait(res_relaxation[j], res_key_subset[j])
            align(qub_key_subset[j], res_key_subset[j])
            # Measure the excited state.
            # With demod.accumulated, the results are QUA vectors with 1 point for each accumulated chunk
            play("x180", qub_key_subset[j])
            align(qub_key_subset[j], res_key_subset[j])  # Make sure the readout occurs after the pulse to qubit
            measure(
                "readout",
                res_key_subset[j],
                demod.accumulated("cos", II[j], division_length, "out1"),
                demod.accumulated("sin", IQ[j], division_length, "out2"),
                demod.accumulated("minus_sin", QI[j], division_length, "out1"),
                demod.accumulated("cos", QQ[j], division_length, "out2"),
            )
            # Save the QUA vectors to their corresponding streams
            with for_(ind[j], 0, ind[j] < number_of_divisions, ind[j] + 1):
                assign(I[j][ind[j]], II[j][ind[j]] + IQ[j][ind[j]])
                save(I[j][ind[j]], I_e_st[j])
                assign(Q[j][ind[j]], QQ[j][ind[j]] + QI[j][ind[j]])
                save(Q[j][ind[j]], Q_e_st[j])

            if multiplexed:
                wait(qub_relaxation[j], qub_key_subset[j])
                wait(res_relaxation[j], res_key_subset[j])
            else:
                align() # When python unravels, this makes sure the readouts are sequential
                if j == len(res_key_subset)-1:
                    wait(np.max(res_relaxation), *res_key_subset)
                    wait(np.max(qub_relaxation), *qub_key_subset)
        # Save the averaging iteration to get the progress bar
        save(n, n_st)

    with stream_processing():
        n_st.save("iteration")
        for j in range(len(qub_key_subset)):
            # Save all streamed points for plotting the IQ blobs
            I_g_st[j].buffer(number_of_divisions).average().save("I_g_"+str(j))
            Q_g_st[j].buffer(number_of_divisions).average().save("Q_g_"+str(j))
            I_e_st[j].buffer(number_of_divisions).average().save("I_e_"+str(j))
            Q_e_st[j].buffer(number_of_divisions).average().save("Q_e_"+str(j))
            # Variances to get the SNR
            (
                ((I_g_st[j].buffer(number_of_divisions) * I_g_st[j].buffer(number_of_divisions)).average())
                - (I_g_st[j].buffer(number_of_divisions).average() * I_g_st[j].buffer(number_of_divisions).average())
            ).save("I_g_var_"+str(j))
            (
                ((Q_g_st[j].buffer(number_of_divisions) * Q_g_st[j].buffer(number_of_divisions)).average())
                - (Q_g_st[j].buffer(number_of_divisions).average() * Q_g_st[j].buffer(number_of_divisions).average())
            ).save("Q_g_var_"+str(j))
            (
                ((I_e_st[j].buffer(number_of_divisions) * I_e_st[j].buffer(number_of_divisions)).average())
                - (I_e_st[j].buffer(number_of_divisions).average() * I_e_st[j].buffer(number_of_divisions).average())
            ).save("I_e_var_"+str(j))
            (
                ((Q_e_st[j].buffer(number_of_divisions) * Q_e_st[j].buffer(number_of_divisions)).average())
                - (Q_e_st[j].buffer(number_of_divisions).average() * Q_e_st[j].buffer(number_of_divisions).average())
            ).save("Q_e_var_"+str(j))

#####################################
#  Open Communication with the QOP  #
#####################################
#qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config)
prog = ro_duration_opt
# ---- Open communication with the OPX ---- #
from warsh_credentials import host_ip, cluster
qmm = QuantumMachinesManager(host = host_ip, cluster_name = cluster)

###########################
# Run or Simulate Program #
###########################
simulate = False
if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=30_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, prog, simulation_config)
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
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(prog)
    # Get results from QUA program
    result_names = mp_result_names(qub_key_subset, single_tags = ["iteration"], mp_tags=["I_g", "Q_g", "I_e", "Q_e", "I_g_var", "Q_g_var", "I_e_var", "Q_e_var"])
    res_handles = fetching_tool(job, data_list=result_names, mode="live")
    # Live plotting
    fig, axs = plt.subplots(len(qub_key_subset), 3, figsize=(12, 4 * len(qub_key_subset)))
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    while res_handles.is_processing():
        # Fetch results
        iteration, I_g_avg, Q_g_avg, I_e_avg, Q_e_avg, I_g_var, Q_g_var, I_e_var, Q_e_var = mp_fetch_all(res_handles, qub_key_subset, num_single_tags=1)
        # Progress bar
        progress_counter(iteration, n_avg, start_time=res_handles.get_start_time())
        # Derive the SNR
        ground_trace = I_g_avg + 1j * Q_g_avg
        excited_trace = I_e_avg + 1j * Q_e_avg
        var = (I_e_var + Q_e_var + I_g_var + Q_g_var) / 4
        SNR = (np.abs(excited_trace - ground_trace) ** 2) / (2 * var)
        # Plot results for each qubit
        for j in range(len(qub_key_subset)):
            axs[j, 0].cla()
            axs[j, 0].plot(x_plot, ground_trace[j].real, label="ground")
            axs[j, 0].plot(x_plot, excited_trace[j].real, label="excited")
            axs[j, 0].set_xlabel("Readout duration [ns]")
            axs[j, 0].set_ylabel("Real [a.u.]")
            axs[j, 0].set_title(f"{qub_key_subset[j]}: Real part")
            axs[j, 0].legend()

            axs[j, 1].cla()
            axs[j, 1].plot(x_plot, ground_trace[j].imag, label="ground")
            axs[j, 1].plot(x_plot, excited_trace[j].imag, label="excited")
            axs[j, 1].set_xlabel("Readout duration [ns]")
            axs[j, 1].set_ylabel("Imag [a.u.]")
            axs[j, 1].set_title(f"{qub_key_subset[j]}: Imaginary part")
            axs[j, 1].legend()

            axs[j, 2].cla()
            axs[j, 2].plot(x_plot, SNR[j], ".-")
            axs[j, 2].set_xlabel("Readout duration [ns]")
            axs[j, 2].set_ylabel("SNR")
            axs[j, 2].set_title(f"{qub_key_subset[j]}: SNR")
        plt.tight_layout()
        plt.pause(0.1)
    # Get the optimal readout length in ns
    for j in range(len(qub_key_subset)):
        opt_readout_length = int(np.round(np.argmax(SNR[j]) * division_length / 4) * 4 * 4)
        print(f"Resonator {qub_key_subset[j]}: The optimal readout length is {opt_readout_length} ns (SNR={max(SNR[j])})")

    # Save results
    script_name = Path(__file__).name
    data_handler = DataHandler(root_data_folder=save_dir)
    save_data_dict.update({"I_g_avg_data": I_g_avg})
    save_data_dict.update({"Q_g_avg_data": Q_g_avg})
    save_data_dict.update({"I_e_avg_data": I_e_avg})
    save_data_dict.update({"Q_e_avg_data": Q_e_avg})
    save_data_dict.update({"I_g_var_data": I_g_var})
    save_data_dict.update({"Q_g_var_data": Q_g_var})
    save_data_dict.update({"I_e_var_data": I_e_var})
    save_data_dict.update({"Q_e_var_data": Q_e_var})
    save_data_dict.update({"fig_live": fig})
    data_handler.additional_files = {script_name: script_name, **default_additional_files}
    data_handler.save_data(data=save_data_dict, name="_".join(script_name.split("_")[1:]).split(".")[0])

    qm.close()