# Taken from github but still being editted for multiplex
"""
        ACTIVE RESET
This script is used to benchmark different types of qubit initialization including active reset protocols.
the different methods are written in macros for better readability.

Each protocol is detailed in the corresponding docstring, but the idea behind active reset is to first measure one
quadrature of the resonator ("I") and compare it to one or two threshold in order to decide whether to apply a pi-pulse
(qubit in |e>), do nothing (qubit in |g>) or measure again if the qubit state is undetermined (active_reset_two_thresholds).

Then, after qubit initialization, the IQ blobs for |g> and |e> are measured again and the readout fidelity is derived
similarly to what is done in IQ_blobs.py.

Prerequisites:
    - Having found the resonance frequency of the resonator coupled to the qubit under study (resonator_spectroscopy).
    - Having calibrated qubit pi pulse (x180) by running qubit, spectroscopy, rabi_chevron, power_rabi and updated the config.
    - Having calibrated the IQ blobs (rotation_angle and ge_threshold).
    - (optional) Having calibrated the readout (readout_frequency_, _amplitude_, _duration_optimization).
    - Having updated the rotation angle (rotation_angle) and g -> e threshold (ge_threshold) in the configuration (IQ_blobs.py).
"""

import numpy as np
from qm.qua import *
from qm import QuantumMachinesManager
from qualang_tools.loops import from_array
from qualang_tools.results import fetching_tool, progress_counter
from qualang_tools.analysis.discriminator import two_state_discriminator
from qualang_tools.plot import interrupt_on_close
from qualang_tools.results.data_handler import DataHandler
from qm_saas import QmSaas, QOPVersion
from qm import SimulationConfig, LoopbackInterface
import matplotlib.pyplot as plt
from pathlib import Path
from scipy.signal import savgol_filter
from qualang_tools.units import unit
u = unit(coerce_to_integer=True)
from scipy import signal
from macros import multiplexed_parser, mp_result_names, mp_fetch_all

if False:
    from configurations.DA_5Q.OPX1000config import *
else:
    from configurations.DB_6Q.OPX1000config import *

##################
#   Parameters   #
##################
# ---- Multiplexed program parameters ---- #
n_avg = 1000
multiplexed = True
qubit_keys = ["q0", "q1", "q2", "q3"]
required_parameters = ["qubit_key", "qubit_relaxation", "resonator_key", "readout_len", "resonator_relaxation", "ge_threshold"]
qub_key_subset, qubit_relaxation, res_key_subset, readout_len, resonator_relaxation, ge_threshold = multiplexed_parser(qubit_keys, multiplexed_parameters.copy(), required_parameters)

# Parameters Definition
initialization_method = "active_reset_one_threshold"  # "thermalization", "active_reset_one_threshold", "active_reset_two_thresholds", "active_reset_fast"
n_shot = 10000  # Number of acquired shots
# The thresholds ar calibrated with the IQ_blobs.py script:
# If I > threshold_e, then the qubit is assumed to be in |e> and a pi pulse is played to reset it.
# If I < threshold_g, then the qubit is assumed to be in |g>.
# else, the qubit state is not determined accurately enough, so we just measure again.
threshold_g_cof = 0.5
threshold_e_cof = 1.0
# Maximum number of tries for active reset
max_tries = 2

qub_relaxation = qubit_relaxation//4 # ns to clock cycles
res_relaxation = resonator_relaxation//4 # ns to clock cycles

# Data to save
save_data_dict = {
    "n_shot": n_shot,
    "config": config,
}
save_dir = Path(__file__).resolve().parent / "data"

###################################
# Helper functions and QUA macros #
###################################
def qubit_initialization(I_reset, count, method, qubit_key, resonator_key, threshold, thermalization_time=None, depletion_time=None):
    """
    Allows to switch between several initialization methods.
    
    :param I_reset: QUA variable to store the 'I' quadrature of the resonator measurement.
    :param count: QUA variable to count the number of tries to reset the qubit
    :param method: the desired initialization method among "thermalization", "active_reset_one_threshold", "active_reset_two_thresholds", "active_reset_fast".
    :param qubit_key: key of qubit to reset.
    :param threshold: ge_threshold to use for the active reset protocols.
    :param thermalization_time: time to wait for the qubit to thermalize (in clock cycles).
    :param depletion_time: time to wait for the resonator to deplete (in clock cycles).
    :return: the number of tries to reset the qubit.
    """
    if depletion_time is None:
        depletion_time = np.max(resonator_relaxation)//4
    if thermalization_time is None:
        thermalization_time = np.max(qubit_relaxation)//4
    if method == "thermalization":
        wait(thermalization_time, qubit_key)
        return 1
    elif method == "active_reset_fast":
        return active_reset_fast(I_reset, qubit_key, resonator_key, threshold, depletion_time)
    elif method == "active_reset_one_threshold":
        return active_reset_one_threshold(I_reset, count, qubit_key, resonator_key, threshold, max_tries, depletion_time)
    elif method == "active_reset_two_thresholds":
        return active_reset_two_thresholds(I_reset, count, qubit_key, resonator_key, threshold, max_tries, depletion_time)
    else:
        raise ValueError(f"method {method} is not implemented.")


def active_reset_one_threshold(I_reset, count, qubit_key: str, resonator_key: str, threshold: float, max_tries: int, depletion_time: int):
    """
    Active reset protocol where the outcome of the measurement is compared to a pre-calibrated threshold (IQ_blobs.py).
    If the qubit is in |e> (I>threshold), then play a pi pulse and measure again, else (qubit in |g>) return the number
    of pi-pulses needed to reset the qubit.
    The program waits for the resonator to deplete before playing the conditional pi-pulse so that the calibrated
    pi-pulse parameters are still valid.

    :param qubit_key: key of qubit to reset.
    :param resonator_key: key of resonator used for the readout.
    :param threshold: threshold between the |g> and |e> blobs - calibrated in IQ_blobs.py
    :param max_tries: maximum number of iterations needed to reset the qubit before exiting the loop anyway.
    :param depletion_time: time to wait for the resonator to deplete (in clock cycles).
    :return: the number of tries to reset the qubit.
    """
    assign(count, 0)
    align(resonator_key, qubit_key)
    with while_((I_reset > threshold) & (count < max_tries)):
        # Measure the state of the resonator
        measure("readout", resonator_key, None, dual_demod.full("opt_cos", "opt_sin", I_reset))
        align(resonator_key, qubit_key)
        # Wait for the resonator to deplete
        wait(depletion_time, qubit_key)
        # Play a conditional pi-pulse to actively reset the qubit
        play("x180", qubit_key, condition=(I_reset > threshold))
        # Update the counter for benchmarking purposes
        assign(count, count + 1)
    return count


def active_reset_two_thresholds(I_reset, count, qubit_key: str, resonator_key: str, threshold: float, max_tries: int, depletion_time: int):
    """
    Active reset protocol where the outcome of the measurement is compared to two pre-calibrated thresholds (IQ_blobs.py).
    If I > threshold_e, then the qubit is assumed to be in |e> and a pi pulse is played to reset it.
    If I < threshold_g, then the qubit is assumed to be in |g> and the loop can be exited.
    else, the qubit state is not determined accurately enough, so we just repeat the process.
    The program waits for the resonator to deplete before playing the conditional pi-pulse so that the calibrated
    pi-pulse parameters are still valid.

    :param threshold_g: threshold "inside" the |g> blob, below which the qubit is in |g> with great certainty.
    :param threshold_e: threshold between the |g> and |e> blobs - calibrated in IQ_blobs.py
    :param max_tries: maximum number of iterations needed to reset the qubit before exiting the loop anyway.
    :return: the number of tries to reset the qubit.
    """
    assign(count, 0)
    align(resonator_key, qubit_key)
    with while_((I_reset > threshold * threshold_g_cof) & (count < max_tries)):
        # Measure the state of the resonator
        measure("readout", resonator_key, None, dual_demod.full("opt_cos", "opt_sin", I_reset))
        align(resonator_key, qubit_key)
        # Wait for the resonator to deplete
        wait(depletion_time, qubit_key)
        # Play a conditional pi-pulse to actively reset the qubit
        play("x180", qubit_key, condition=(I_reset > threshold * threshold_e_cof))
        # Update the counter for benchmarking purposes
        assign(count, count + 1)
    return count


def active_reset_fast(I_reset, qubit_key: str, resonator_key: str, threshold: float, depletion_time: int):
    """
    Active reset protocol where the outcome of the measurement is compared to a pre-calibrated threshold (IQ_blobs.py).
    If the qubit is in |e> (I>threshold), then play a pi pulse, else (qubit in |g>) do nothing and proceed to the sequence.
    The program waits for the resonator to deplete before playing the conditional pi-pulse so that the calibrated
    pi-pulse parameters are still valid.

    :param threshold_g: threshold between the |g> and |e> blobs - calibrated in IQ_blobs.py.
    :return: 1
    """
    align(resonator_key, qubit_key)
    # Measure the state of the resonator
    measure("readout", resonator_key, dual_demod.full("opt_cos", "opt_sin", I_reset))
    align(resonator_key, qubit_key)
    # Wait for the resonator to deplete
    wait(depletion_time, qubit_key)
    # Play a conditional pi-pulse to actively reset the qubit
    play("x180", qubit_key, condition=(I_reset > threshold))
    return 1


###################
# The QUA program #
###################
with program() as active_reset_prog:
    n = declare(int)  # Averaging index
    n_st = declare_stream()

    I = [declare(fixed) for _ in range(len(qub_key_subset))]
    Q = [declare(fixed) for _ in range(len(qub_key_subset))]
    I_st = [declare_stream() for _ in range(len(qub_key_subset))]
    Q_st = [declare_stream() for _ in range(len(qub_key_subset))]
    I_g = [declare(fixed) for _ in range(len(qub_key_subset))]
    Q_g = [declare(fixed) for _ in range(len(qub_key_subset))]
    I_g_st = [declare_stream() for _ in range(len(qub_key_subset))]
    Q_g_st = [declare_stream() for _ in range(len(qub_key_subset))]
    I_e = [declare(fixed) for _ in range(len(qub_key_subset))]
    Q_e = [declare(fixed) for _ in range(len(qub_key_subset))]
    I_e_st = [declare_stream() for _ in range(len(qub_key_subset))]
    Q_e_st = [declare_stream() for _ in range(len(qub_key_subset))]
    count = [declare(int) for _ in range(len(qub_key_subset))]
    I_reset = [declare(fixed) for _ in range(len(qub_key_subset))]

    cont_condition = [declare(bool) for _ in range(len(qub_key_subset))]
    tries_st = [declare_stream() for _ in range(len(qub_key_subset))]

    with for_(n, 0, n < n_shot, n + 1):
        for j in range(len(qub_key_subset)): # a real Python for loop so it unravels and executes in parallel, not sequentially
            # Active reset
            count[j] = qubit_initialization(I_reset[j], count[j], method = initialization_method, qubit_key=qub_key_subset[j], resonator_key=res_key_subset[j], threshold=ge_threshold[j], thermalization_time=qub_relaxation[j], depletion_time=res_relaxation[j])
            align(res_key_subset[j], qub_key_subset[j])
            # Measure the state of the resonator after reset, qubit should be in |g>
            measure(
                "readout",
                res_key_subset[j],
                dual_demod.full("opt_cos", "opt_sin", I_g[j]),
                dual_demod.full("opt_minus_sin", "opt_cos", Q_g[j]),
            )
            # Save the 'I' & 'Q' quadratures to their respective streams for the ground state
            save(I_g[j], I_g_st[j])
            save(Q_g[j], Q_g_st[j])
            with if_(count[j] > 0):
                save(count[j], tries_st[j])

            align(res_key_subset[j], qub_key_subset[j])  # global align
            # Active reset
            count[j] = qubit_initialization(I_reset[j], count[j], method = initialization_method, qubit_key=qub_key_subset[j], resonator_key=res_key_subset[j], threshold=ge_threshold[j], thermalization_time=qub_relaxation[j], depletion_time=res_relaxation[j])
            align(res_key_subset[j], qub_key_subset[j])
            align(res_key_subset[j], qub_key_subset[j])
            # Play the x180 gate to put the qubit in the excited state
            play("x180", qub_key_subset[j])
            # Align the two elements to measure after playing the qubit pulse.
            align(qub_key_subset[j], res_key_subset[j])
            # Measure the state of the resonator, qubit should be in |e>
            measure(
                "readout",
                res_key_subset[j],
                dual_demod.full("opt_cos", "opt_sin", I_e[j]),
                dual_demod.full("opt_minus_sin", "opt_cos", Q_e[j]),
            )
            # Save the 'I' & 'Q' quadratures to their respective streams for the excited state
            save(I_e[j], I_e_st[j])
            save(Q_e[j], Q_e_st[j])
            # Save only the count when the qubit was not directly measured in |g>
            with if_(count[j] > 0):
                save(count[j], tries_st[j])
            if multiplexed:
                wait(res_relaxation[j], res_key_subset[j])
                wait(qub_relaxation[j], qub_key_subset[j]) 
            else:
                align() # When python unravels, this makes sure the readouts are sequential
                if j == len(res_key_subset)-1:
                    wait(np.max(res_relaxation), *res_key_subset) 
                    wait(np.max(qub_relaxation), *qub_key_subset)
        save(n, n_st)

    with stream_processing():
        # Save all streamed points for plotting the IQ blobs
        n_st.save("iteration")
        for j in range(len(qub_key_subset)):
            I_g_st[j].save_all("I_g_"+str(j))
            Q_g_st[j].save_all("Q_g_"+str(j))
            I_e_st[j].save_all("I_e_"+str(j))
            Q_e_st[j].save_all("Q_e_"+str(j))
            tries_st[j].average().save("average_tries_"+str(j))

#####################################
#  Open Communication with the QOP  #
#####################################
#qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config)
prog = active_reset_prog
# ---- Open communication with the OPX ---- #
from warsh_credentials import host_ip, cluster
qmm = QuantumMachinesManager(host = host_ip, cluster_name = cluster)

simulate = True
if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
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
    qm = qmm.open_qm(config)
    job = qm.execute(prog)
    # Creates a result handle to fetch data from the OPX
    res_handles = job.result_handles
    # Waits (blocks the Python console) until all results have been acquired
    res_handles.wait_for_all_values()
    # Fetch the 'I' & 'Q' points for the qubit in the ground and excited states
    result_names = mp_result_names(qub_key_subset, single_tags = ["iteration"], mp_tags = ["I_g", "Q_g", "I_e", "Q_e", "average_tries"])
    res_handles = fetching_tool(job, data_list = result_names, mode = "wait_for_all")

    iteration, I_g, Q_g, I_e, Q_e, average_tries = mp_fetch_all(res_handles, qub_key_subset, num_single_tags=1)
    # Plot the IQ blobs, rotate them to get the separation along the 'I' quadrature, estimate a threshold between them
    # for state discrimination and derive the fidelity matrix
    for j in range(len(qub_key_subset)):
        angle, threshold, fidelity, gg, ge, eg, ee = two_state_discriminator(I_g[j], Q_g[j], I_e[j], Q_e[j], b_print=True, b_plot=True)
        plt.suptitle(f"Qubit {qub_key_subset[j]}, {average_tries[j]=}")
        print(f"Qubit {qub_key_subset[j]}, {average_tries[j]=}")

    # Save results
    script_name = Path(__file__).name
    data_handler = DataHandler()#root_data_folder=save_dir)
    save_data_dict.update({"Ig_data": I_g})
    save_data_dict.update({"Qg_data": Q_g})
    save_data_dict.update({"Ie_data": I_e})
    save_data_dict.update({"Qe_data": Q_e})
    save_data_dict.update({"two_state_discriminator": [angle, threshold, fidelity, gg, ge, eg, ee]})
    data_handler.additional_files = {script_name: script_name, **default_additional_files}
    data_handler.save_data(data=save_data_dict, name="_".join(script_name.split("_")[1:]).split(".")[0])