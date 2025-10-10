"""
        ALL-XY MEASUREMENT
The program consists in playing a random sequence of predefined gates after which the theoretical qubit state is known.
See [Reed's Thesis](https://rsl.yale.edu/sites/default/files/files/RSL_Theses/reed.pdf) for more details.

The sequence of gates defined below is based on https://rsl.yale.edu/sites/default/files/physreva.82.pdf-optimized_driving_0.pdf
This protocol checks that the single qubit gates (x180, x90, y180 and y90) are properly defined and calibrated and can
thus be used as a preliminary step before randomized benchmarking.

Prerequisites:
    - Having found the resonance frequency of the resonator coupled to the qubit under study (resonator_spectroscopy).
    - Having calibrated qubit pi pulse (x180) by running qubit, spectroscopy, rabi_chevron, power_rabi and updated the config.
    - Having the qubit frequency perfectly calibrated (ramsey).
    - (optional) Having calibrated the readout (readout_frequency, amplitude, duration_optimization IQ_blobs) for better SNR.
"""
import numpy as np
from qm.qua import *
from qm import QuantumMachinesManager
from qualang_tools.loops import from_array
from qualang_tools.results import fetching_tool, progress_counter
from qualang_tools.plot import interrupt_on_close
from qm_saas import QmSaas, QOPVersion
from qm import SimulationConfig
import matplotlib.pyplot as plt
from pathlib import Path
from scipy.signal import savgol_filter
from qualang_tools.units import unit
u = unit(coerce_to_integer=True)
from scipy import signal
from qualang_tools.bakery.randomized_benchmark_c1 import c1_table
from scipy.optimize import curve_fit
from qualang_tools.results.data_handler import DataHandler
from macros import multiplexed_parser, mp_result_names, mp_fetch_all, readout_macro

if False:
    from configurations.DA_5Q.OPX1000config import *
else:
    from configurations.DB_6Q.OPX1000config import *

##################
#   Parameters   #
##################
# Parameters Definition
# ---- Multiplexed program parameters ---- #
multiplexed = True
qubit_keys = ["q0", "q1", "q2", "q3"]
required_parameters = ["qubit_key", "qubit_frequency", "qubit_relaxation", "resonator_key", "readout_len", "resonator_relaxation", "ge_threshold", "x180_len"]
qub_key_subset, qub_frequency, qubit_relaxation, res_key_subset, readout_len, resonator_relaxation, ge_threshold, x180_len = multiplexed_parser(qubit_keys, multiplexed_parameters.copy(), required_parameters)


# ---- RB program parameters ---- #
n_avg = 1000  # Number of averaging loops
qub_relaxation = qubit_relaxation//4 # From ns to clock cycles
res_relaxation = resonator_relaxation//4 # From ns to clock cycles

# Data to save
# ---- Data to save ---- #
save_data_dict = {
    "qubit_keys": qub_key_subset,
    "n_avg": n_avg,
    "config": config,
}
save_dir = Path(__file__).resolve().parent / "data"

###################################
# Helper functions and QUA macros #
###################################
# All-XY sequences. The sequence names must match corresponding operation in the config
sequence = [
    ("I", "I"),
    ("x180", "x180"),
    ("y180", "y180"),
    ("x180", "y180"),
    ("y180", "x180"),
    ("x90", "I"),
    ("y90", "I"),
    ("x90", "y90"),
    ("y90", "x90"),
    ("x90", "y180"),
    ("y90", "x180"),
    ("x180", "y90"),
    ("y180", "x90"),
    ("x90", "x180"),
    ("x180", "x90"),
    ("y90", "y180"),
    ("y180", "y90"),
    ("x180", "I"),
    ("y180", "I"),
    ("x90", "x90"),
    ("y90", "y90"),
]


# All-XY macro generating the pulse sequences from a python list.
def allXY(pulses, qubit_key, resonator_key, I_xy, Q_xy, x180_length):
    """
    Generate a QUA sequence based on the two operations written in pulses. Used to generate the all XY program.
    **Example:** I, Q = allXY(['I', 'y90'])

    :param pulses: tuple containing a particular set of operations to play. The pulse names must match corresponding
        operations in the config except for the identity operation that must be called 'I'.
    :param qubit_key: The qubit key to perform the gates on. Should be a string corresponding to a qubit defined in the configuration.
    :param resonator_key: The resonator key to perform the readout on. Should be a string corresponding to a resonator defined in the configuration.
    :param I_xy: A QUA variable for the information in the `I` quadrature. Should be of type `Fixed`.
    :param Q_xy: A QUA variable for the information in the `Q` quadrature. Should be of type `Fixed`.
    :return: two QUA variables for the 'I' and 'Q' quadratures measured after the sequence.
    """
    # Play the 1st gate or wait if the gate is identity
    if pulses[0] != "I":
        play(pulses[0], qubit_key)  # Either play the sequence
    else:
        wait(x180_length // 4, qubit_key)  # or wait if sequence is identity
    # Play the 2nd gate or wait if the gate is identity
    if pulses[1] != "I":
        play(pulses[1], qubit_key)  # Either play the sequence
    else:
        wait(x180_length // 4, qubit_key)  # or wait if sequence is identity
    # Align the two elements to measure after playing the qubit gates.
    align(qubit_key, resonator_key)
    # Measure the state of the resonator and return the two quadratures
    measure(
        "readout",
        resonator_key,
        dual_demod.full("opt_cos", "opt_sin", I_xy),
        dual_demod.full("opt_minus_sin", "opt_cos", Q_xy),
    )
    return I_xy, Q_xy


###################
# The QUA program #
###################
with program() as ALL_XY:
    n = declare(int)
    r = Random()  # Pseudo random number generator
    r_ = declare(int)  # Index of the sequence to play
    # The result of each set of gates is saved in its own stream
    I = [declare(fixed) for _ in range(len(sequence))]
    Q = [declare(fixed) for _ in range(len(sequence))]
    I_st = [[declare_stream() for _ in range(len(sequence))] for _ in range(len(qub_key_subset))]
    Q_st = [[declare_stream() for _ in range(len(sequence))] for _ in range(len(qub_key_subset))]
    n_st = declare_stream()

    with for_(n, 0, n < n_avg, n + 1):
        assign(r_, r.rand_int(len(sequence)))
        for j in range(len(qub_key_subset)):  # A Python for loop so it unravels and executes in parallel, not sequentially
            # Get a value from the pseudo-random number generator on the OPX FPGA
            # Wait for the qubit to decay to the ground state - Can be replaced by active reset
            wait(qub_relaxation[j], qub_key_subset[j])
            # Plays a random XY sequence
            # The switch/case method allows to map a python index (here "i") to a QUA number (here "r_") in order to switch
            # between elements in a python list (here "sequence") that cannot be converted into a QUA array (here because it
            # contains strings).
            with switch_(r_):
                for i in range(len(sequence)):
                    with case_(i):
                        # Play the all-XY sequence corresponding to the drawn random number
                        I[j], Q[j] = allXY(sequence[i], qub_key_subset[j], res_key_subset[j], I[j], Q[j], x180_len[j])
                        # Save the 'I' & 'Q' quadratures to their respective streams
                        save(I[j], I_st[j][i])
                        save(Q[j], Q_st[j][i])
        save(n, n_st)

    with stream_processing():
        n_st.save("iteration")
        for j in range(len(qub_key_subset)):
            for i in range(len(sequence)):
                I_st[j][i].average().save(f"I{i}_{j}")
                Q_st[j][i].average().save(f"Q{i}_{j}")

#####################################
#  Open Communication with the QOP  #
#####################################
#qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config)
prog = ALL_XY
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
    #data_list = ["iteration"] + list(np.concatenate([[f"I{i}", f"Q{i}"] for i in range(len(sequence))]))
    result_names = mp_result_names( qub_key_subset, single_tags = ["iteration"], mp_tags = list( np.concatenate([[f"I{i}", f"Q{i}"] for i in range(len(sequence))]) ) )
    res_handles = fetching_tool(job, data_list = result_names, mode = "live")
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    while res_handles.is_processing():
        # Fetch results
        iteration, *IQ_data = mp_fetch_all(res_handles, qub_key_subset, num_single_tags=1)
        IQ_data = np.array(IQ_data)
        I = IQ_data[::2]
        Q = IQ_data[1::2]
        I = I.reshape(len(qub_key_subset), len(sequence))
        Q = Q.reshape(len(qub_key_subset), len(sequence))
        I = -I
        Q = -Q
        n = iteration
        # Progress bar
        progress_counter(n, n_avg, start_time=res_handles.start_time)
        # Plot results
        plt.suptitle("All XY")
        plt.subplot(211)
        plt.cla()
        for j in range(len(qub_key_subset)):
            plt.plot(I[j], "bx", label="Experimental data, Qubit " + str(qub_key_subset[j]) )
            plt.plot([np.max(I[j])] * 5 + [np.mean(I[j])] * 12 + [np.min(I[j])] * 4, "r-", label="Expected value, Qubit " + str(qub_key_subset[j]))
        plt.ylabel("I quadrature [a.u.]")
        plt.xticks(ticks=range(len(sequence)), labels=["" for _ in sequence], rotation=45)
        plt.legend()
        plt.subplot(212)
        plt.cla()
        for j in range(len(qub_key_subset)):
             plt.plot(Q[j], "bx", label="Experimental data, Qubit " + str(qub_key_subset[j]) )
             plt.plot([np.max(Q[j])] * 5 + [np.mean(Q[j])] * 12 + [np.min(Q[j])] * 4, "r-", label="Expected value, Qubit " + str(qub_key_subset[j]))
        plt.ylabel("Q quadrature [a.u.]")
        plt.xticks(ticks=range(len(sequence)), labels=[str(el) for el in sequence], rotation=45)
        plt.legend()
        plt.tight_layout()
        plt.pause(0.1)
    # Save results
    script_name = Path(__file__).name
    data_handler = DataHandler(root_data_folder=save_dir)
    save_data_dict.update({"I_data": I})
    save_data_dict.update({"Q_data": Q})
    save_data_dict.update({"fig_live": fig})
    data_handler.additional_files = {script_name: script_name, **default_additional_files}
    data_handler.save_data(data=save_data_dict, name="_".join(script_name.split("_")[1:]).split(".")[0])