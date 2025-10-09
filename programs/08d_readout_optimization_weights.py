"""
        READOUT OPTIMISATION: INTEGRATION WEIGHTS
This sequence involves assessing the state of the resonator in two distinct scenarios: first, after thermalization
(with the qubit in the |g> state) and then following the application of a pi pulse to the qubit (transitioning the
qubit to the |e> state).
The "demod.sliced" method is employed to capture the time trace of the demodulated data, providing insight into the
resonator's response.
Reference: https://docs.quantum-machines.co/0.1/qm-qua-sdk/docs/Guides/features/?h=accumulated#sliced-demodulation

From the average I & Q quadratures for the qubit states |g> and |e>, along with their variances,
the Signal-to-Noise Ratio (SNR) is determined. The readout duration that yields the highest SNR is selected as
the optimal choice.
It's important to note that if you aim to observe the resonator's behavior during its ringdown phase,
the length of the integration weights should surpass that of the readout_pulse.

Prerequisites:
    - Having found the resonance frequency of the resonator coupled to the qubit under study (resonator_spectroscopy).
    - Having calibrated qubit pi pulse (x180) by running qubit, spectroscopy, rabi_chevron, power_rabi and updated the config.
    - Having calibrated the readout frequency, amplitude and duration and updated the configuration.

Next steps before going to the next node:
    - Update the integration weights in the configuration by following the steps at the end of the script.
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
def divide_array_in_half(arr):
    split_index = len(arr) // 2
    arr1 = arr[:split_index]
    arr2 = arr[split_index:]
    return arr1, arr2


def normalize_complex_array(arr):
    # Calculate the simple norm of the complex array
    norm = np.sqrt(np.sum(np.abs(arr) ** 2))

    # Normalize the complex array by dividing it by the norm
    normalized_arr = arr / norm

    # Rescale the normalized array so that the maximum value is 1
    max_val = np.max(np.abs(normalized_arr))
    rescaled_arr = normalized_arr / max_val

    return rescaled_arr


def plot_three_complex_arrays(x, arr1, arr2, arr3):
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))
    ax1.plot(x, arr1.real, label="real")
    ax1.plot(x, arr1.imag, label="imag")
    ax1.set_title("ground state")
    ax1.set_xlabel("Readout time [ns]")
    ax1.set_ylabel("demod traces [a.u.]")
    ax1.legend()
    ax2.plot(x, arr2.real, label="real")
    ax2.plot(x, arr2.imag, label="imag")
    ax2.set_title("excited state")
    ax2.set_xlabel("Readout time [ns]")
    ax2.set_ylabel("demod traces [a.u.]")
    ax2.legend()
    ax3.plot(x, arr3.real, label="real")
    ax3.plot(x, arr3.imag, label="imag")
    ax3.set_title("SNR")
    ax3.set_xlabel("Readout time [ns]")
    ax3.set_ylabel("subtracted traces [a.u.]")
    ax3.legend()
    plt.tight_layout()
    plt.show()


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
with program() as opt_weights:
    n = declare(int)
    ind = [declare(int) for _ in range(len(qub_key_subset))]
    II = [declare(fixed, size=number_of_divisions) for _ in range(len(qub_key_subset))]
    IQ = [declare(fixed, size=number_of_divisions) for _ in range(len(qub_key_subset))]
    QI = [declare(fixed, size=number_of_divisions) for _ in range(len(qub_key_subset))]
    QQ = [declare(fixed, size=number_of_divisions) for _ in range(len(qub_key_subset))]

    n_st = declare_stream()
    II_g_st = [declare_stream() for _ in range(len(qub_key_subset))]
    IQ_g_st = [declare_stream() for _ in range(len(qub_key_subset))]
    QI_g_st = [declare_stream() for _ in range(len(qub_key_subset))]
    QQ_g_st = [declare_stream() for _ in range(len(qub_key_subset))]
    II_e_st = [declare_stream() for _ in range(len(qub_key_subset))]
    IQ_e_st = [declare_stream() for _ in range(len(qub_key_subset))]
    QI_e_st = [declare_stream() for _ in range(len(qub_key_subset))]
    QQ_e_st = [declare_stream() for _ in range(len(qub_key_subset))]

    with for_(n, 0, n < n_avg, n + 1):
        for j in range(len(qub_key_subset)):  # A Python for loop so it unravels and executes in parallel, not sequentially
            # Measure the ground state
            measure(
                "readout",
                res_key_subset[j],
                demod.sliced("cos", II[j], division_length, "out1"),
                demod.sliced("sin", IQ[j], division_length, "out2"),
                demod.sliced("minus_sin", QI[j], division_length, "out1"),
                demod.sliced("cos", QQ[j], division_length, "out2"),
            )
            # Save the sliced data (time trace of the demodulated data with a resolution equals to the division length)
            with for_(ind[j], 0, ind[j] < number_of_divisions, ind[j] + 1):
                save(II[j][ind[j]], II_g_st[j])
                save(IQ[j][ind[j]], IQ_g_st[j])
                save(QI[j][ind[j]], QI_g_st[j])
                save(QQ[j][ind[j]], QQ_g_st[j])
            # Wait for the qubit and resonator to relax
            align(qub_key_subset[j], res_key_subset[j])
            wait(qub_relaxation[j], qub_key_subset[j])
            wait(res_relaxation[j], res_key_subset[j])
            align(qub_key_subset[j], res_key_subset[j])
            # Measure the excited state
            play("x180", qub_key_subset[j])
            align(qub_key_subset[j], res_key_subset[j])  # Make sure the readout occurs after the pulse to qubit
            measure(
                "readout",
                res_key_subset[j],
                demod.sliced("cos", II[j], division_length, "out1"),
                demod.sliced("sin", IQ[j], division_length, "out2"),
                demod.sliced("minus_sin", QI[j], division_length, "out1"),
                demod.sliced("cos", QQ[j], division_length, "out2"),
            )
            # Save the sliced data (time trace of the demodulated data with a resolution equals to the division length)
            with for_(ind[j], 0, ind[j] < number_of_divisions, ind[j] + 1):
                save(II[j][ind[j]], II_e_st[j])
                save(IQ[j][ind[j]], IQ_e_st[j])
                save(QI[j][ind[j]], QI_e_st[j])
                save(QQ[j][ind[j]], QQ_e_st[j])
            if multiplexed:
                wait(qub_relaxation[j], qub_key_subset[j])
                wait(res_relaxation[j], res_key_subset[j])
            else:
                align() # When python unravels, this makes sure the readouts are sequential
                if j == len(res_key_subset)-1:
                    wait(np.max(res_relaxation), *res_key_subset)
                    wait(np.max(qub_relaxation), *qub_key_subset)
        save(n, n_st)

    with stream_processing():
        n_st.save("iteration")
        for j in range(len(qub_key_subset)):
            II_g_st[j].buffer(number_of_divisions).average().save("II_g_"+str(j))
            IQ_g_st[j].buffer(number_of_divisions).average().save("IQ_g_"+str(j))
            QI_g_st[j].buffer(number_of_divisions).average().save("QI_g_"+str(j))
            QQ_g_st[j].buffer(number_of_divisions).average().save("QQ_g_"+str(j))
            II_e_st[j].buffer(number_of_divisions).average().save("II_e_"+str(j))
            IQ_e_st[j].buffer(number_of_divisions).average().save("IQ_e_"+str(j))
            QI_e_st[j].buffer(number_of_divisions).average().save("QI_e_"+str(j))
            QQ_e_st[j].buffer(number_of_divisions).average().save("QQ_e_"+str(j))

#####################################
#  Open Communication with the QOP  #
#####################################
#qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config)
prog = opt_weights
# ---- Open communication with the OPX ---- #
from warsh_credentials import host_ip, cluster
qmm = QuantumMachinesManager(host = host_ip, cluster_name = cluster)

###########################
# Run or Simulate Program #
###########################
simulate = False
if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, opt_weights, simulation_config)
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
    job = qm.execute(opt_weights)
    # Get results from QUA program
    result_names = mp_result_names(qub_key_subset, single_tags = ["iteration"], mp_tags=["II_g", "IQ_g", "QI_g", "QQ_g", "II_e", "IQ_e", "QI_e", "QQ_e"])
    res_handles = fetching_tool(job, data_list=result_names, mode="live")
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  #  Interrupts the job when closing the figure
    while res_handles.is_processing():
        # Fetch results
        iteration, II_g, IQ_g, QI_g, QQ_g, II_e, IQ_e, QI_e, QQ_e = mp_fetch_all(res_handles, qub_key_subset, num_single_tags=1)
        # Progress bar
        progress_counter(iteration, n_avg, start_time=res_handles.get_start_time())

    # Sum the quadrature to fully demodulate the traces
    Ie = II_e + IQ_e
    Ig = II_g + IQ_g
    Qe = QI_e + QQ_e
    Qg = QI_g + QQ_g
    # Derive and normalize the ground and excited traces
    ground_trace = Ig + 1j * Qg
    excited_trace = Ie + 1j * Qe
    subtracted_trace = excited_trace - ground_trace
    for j in range(len(qub_key_subset)):
        norm_subtracted_trace = normalize_complex_array(subtracted_trace[j])  # <- these are the optimal weights :)
        # Plot the results
        plot_three_complex_arrays(x_plot, ground_trace[j], excited_trace[j], norm_subtracted_trace)
        # Reshape the optimal integration weights to match the configuration
        weights_real = norm_subtracted_trace.real
        weights_minus_imag = -norm_subtracted_trace.imag
        weights_imag = norm_subtracted_trace.imag
        weights_minus_real = -norm_subtracted_trace.real
        # Save the weights for later use in the config
        np.savez(
            "optimal_weights_" + res_key_subset[j],
            weights_real=weights_real,
            weights_minus_imag=weights_minus_imag,
            weights_imag=weights_imag,
            weights_minus_real=weights_minus_real,
            division_length=division_length,
        )
    # After obtaining the optimal weights, you need to load them to the 'integration_weights' dictionary in the config.
    # For this, you can just copy and paste the following lines into the "integration_weights" section:
    # "opt_cosine_weights": {
    #     "cosine": opt_weights_real,
    #     "sine": opt_weights_minus_imag,
    # },
    # "opt_sine_weights": {
    #     "cosine": opt_weights_imag,
    #     "sine": opt_weights_real,
    # },
    # "opt_minus_sine_weights": {
    #     "cosine": opt_weights_minus_imag,
    #     "sine": opt_weights_minus_real,
    # },

    # also need to add the new weights to readout_pulse under the "integration_weights" section:
    # "opt_cos": "opt_cosine_weights",
    # "opt_sin": "opt_sine_weights",
    # "opt_minus_sin": "opt_minus_sine_weights",

    # And finally extract the weights from the saved file and reformat them using the integration_weights_tools.
    # For this you just need to copy and paste the following lines at the beginning of the config, where the readout
    # parameters are defined as Python variables:
    # opt_weights = True
    # if opt_weights:
    #     from qualang_tools.config.integration_weights_tools import convert_integration_weights
    #
    #     weights = np.load("opt_weights.npz")
    #     opt_weights_real = convert_integration_weights(weights["weights_real"])
    #     opt_weights_minus_imag = convert_integration_weights(weights["weights_minus_imag"])
    #     opt_weights_imag = convert_integration_weights(weights["weights_imag"])
    #     opt_weights_minus_real = convert_integration_weights(weights["weights_minus_real"])
    # else:
    #     opt_weights_real = [(1.0, readout_len)]
    #     opt_weights_minus_imag = [(1.0, readout_len)]
    #     opt_weights_imag = [(1.0, readout_len)]
    #     opt_weights_minus_real = [(1.0, readout_len)]
    # Save results
    script_name = Path(__file__).name
    data_handler = DataHandler(root_data_folder=save_dir)
    save_data_dict.update({"Ig_data": Ig})
    save_data_dict.update({"Qg_data": Qg})
    save_data_dict.update({"Ie_data": Ie})
    save_data_dict.update({"Qe_data": Qe})
    data_handler.additional_files = {script_name: script_name, **default_additional_files}
    data_handler.save_data(data=save_data_dict, name="_".join(script_name.split("_")[1:]).split(".")[0])