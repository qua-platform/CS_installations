"""
        QUBIT SPECTROSCOPY
This sequence involves sending a saturation pulse to the qubit, placing it in a mixed state,
and then measuring the state of the resonator across various qubit drive intermediate dfs.
In order to facilitate the qubit search, the qubit pulse duration and amplitude can be changed manually in the QUA
program directly without having to modify the configuration.

The data is post-processed to determine the qubit resonance frequency, which can then be used to adjust
the qubit intermediate frequency in the configuration under "qubit_IF".

Note that it can happen that the qubit is excited by the image sideband or LO leakage instead of the desired sideband.
This is why calibrating the qubit mixer is highly recommended.

This step can be repeated using the "x180" operation instead of "saturation" to adjust the pulse parameters (amplitude,
duration, frequency) before performing the next calibration steps.

Prerequisites:
    - Identification of the resonator's resonance frequency when coupled to the qubit in question (referred to as "resonator_spectroscopy").
    - Calibration of the IQ mixer connected to the qubit drive line (whether it's an external mixer or an Octave port).
    - Configuration of the saturation pulse amplitude and duration to transition the qubit into a mixed state.
    - Specification of the expected qubit T1 in the configuration.

Before proceeding to the next node:
    - Update the qubit frequency, labeled as "qubit_IF", in the configuration.
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
from qualang_tools.results.data_handler import DataHandler
from macros import multiplexed_parser, mp_result_names, mp_fetch_all

# ---- Choose which device configuration ---- #
if True:
    from configurations.DA_5Q.OPX1000config import *
else:
    from configurations.DB_6Q.OPX1000config import *

# ---- Multiplexed program parameters ---- #
n_avg = 1000
multiplexed = True
qubit_keys = ["q0", "q1", "q2", "q3"]
required_parameters = ["qubit_key", "qubit_frequency", "qubit_relaxation", "qubit_LO", "resonator_key", "readout_len", "resonator_relaxation"]
qub_key_subset, qub_frequency, qubit_relaxation, qubit_LO, res_key_subset, readout_len, resonator_relaxation = multiplexed_parser(qubit_keys, multiplexed_parameters.copy(), required_parameters)

# ---- Qubit Spectroscopy ---- #
res_relaxation = resonator_relaxation//4 # From ns to clock cycles
qub_relaxation = qubit_relaxation//4 # From ns to clock cycles

qub_IF_guesses = qub_frequency - qubit_LO
qub_spec_span = 10 * u.MHz
qub_spec_df = 100 * u.kHz
qub_spec_sweep_dfs = np.arange(-qub_spec_span, qub_spec_span + qub_spec_df, qub_spec_df) # Sweep detunings actually used in the program
qub_spec_IF_frequencies = np.array([qub_spec_sweep_dfs + guess for guess in qub_IF_guesses]) # IF frequencies swept in the program, used for plotting
qub_spec_frequencies = np.array([qub_spec_sweep_dfs + guess for guess in qub_frequency]) # Absolute frequencies

# ---- Data to save ---- #
save_data_dict = {
    "qubit_keys": qub_key_subset,
    "n_avg": n_avg,
    "IF_frequencies": qub_spec_IF_frequencies,
    "absolute_frequencies": qub_spec_frequencies,
    "config": config,
}
save_dir = Path(__file__).resolve().parent / "data"

# ---- Qubit spectroscopy QUA program ---- #
with program() as qubit_spec_multiplexed:
    n = declare(int) # QUA variable for the averaging loop
    n_st = declare_stream() # Stream for the averaging iteration 'n'
    df = declare(int) # QUA variable for the sweep of the qubit IF frequency
    I = [declare(fixed) for _ in range(len(qub_key_subset))] # QUA variable for the measured 'I' quadrature
    Q = [declare(fixed) for _ in range(len(qub_key_subset))] # QUA variable for the measured 'Q' quadrature
    I_st = [declare_stream() for _ in range(len(qub_key_subset))] # Stream for the 'I' quadrature
    Q_st = [declare_stream() for _ in range(len(qub_key_subset))] # Stream for the 'Q' quadrature

    with for_(n, 0, n < n_avg, n + 1): # Averaging loop
        with for_(*from_array(df, qub_spec_sweep_dfs)): # Loop over the qubit frequency detunings
            for j in range(len(qub_key_subset)): # A Python for loop so it unravels and executes in parallel, not sequentially
                update_frequency(qub_key_subset[j], df + qub_IF_guesses[j]) # Update the qubit IF frequency
                play("saturation", qub_key_subset[j]) # Excite the qubit with a long pulse to saturate it
                align(qub_key_subset[j], res_key_subset[j]) # Make sure the readout occurs after the pulse to qubit
                measure(
                    "readout",
                    res_key_subset[j],
                    dual_demod.full("cos", "sin", I[j]),
                    dual_demod.full("minus_sin", "cos", Q[j])
                ) 
                save(I[j], I_st[j])
                save(Q[j], Q_st[j])
                if multiplexed:
                    wait(res_relaxation[j], res_key_subset[j])
                    wait(qub_relaxation[j], qub_key_subset[j]) 
                else:
                    align() # When python unravels, this makes sure the readouts are sequential if desired
                    if j == len(res_key_subset)-1:
                        wait(np.max(res_relaxation), *res_key_subset) 
                        wait(np.max(qub_relaxation), *qub_key_subset)
        save(n, n_st)
    with stream_processing():
        n_st.save("iteration")
        for j in range(len(qub_key_subset)):
            I_st[j].buffer(len(qub_spec_sweep_dfs)).average().save("I_"+str(j))
            Q_st[j].buffer(len(qub_spec_sweep_dfs)).average().save("Q_"+str(j))

prog = qubit_spec_multiplexed
# ---- Open communication with the OPX ---- #
from opx_credentials import qop_ip, cluster
qmm = QuantumMachinesManager(host=qop_ip, cluster_name=cluster)

simulate = False
if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=2_000)  # In clock cycles = 4ns
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
    qm = qmm.open_qm(config, close_other_machines=True)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(prog)
    # Creates a result handle to fetch data from the OPX
    result_names = mp_result_names(qub_key_subset, single_tags = ["iteration"], mp_tags = ["I", "Q"])
    res_handles = fetching_tool(job, data_list = result_names, mode = "live")
    # Waits (blocks the Python console) until all results have been acquired
    fig = plt.figure()
    interrupt_on_close(fig, job)  #  Interrupts the job when closing the figure
    while res_handles.is_processing():
        # Fetch results
        iteration, I, Q = mp_fetch_all(res_handles, qub_key_subset, num_single_tags=1)
        # Convert results into Volts
        for j in range(len(qub_key_subset)):
            I[j] = u.demod2volts(I[j], readout_len[j])
            Q[j] = u.demod2volts(Q[j], readout_len[j])
        S = I + 1j * Q
        R = np.abs(S)  # Amplitude
        phase = np.angle(S)  # Phase
        # Progress bar
        progress_counter(iteration, n_avg, start_time=res_handles.get_start_time())
        # Plot results
        plt.suptitle(f"Qubit spectroscopy - LO = {qubit_LO[j] / u.GHz} GHz")
        ax1 = plt.subplot(211)
        plt.cla()
        for j in range(len(qub_key_subset)):
            plt.plot((qub_spec_frequencies[j] - qubit_LO[j]) / u.MHz, R[j], label=f"Qubit {qub_key_subset[j]} at {qub_frequency[j]/u.GHz:.3f} GHz")
        plt.ylabel(r"$R=\sqrt{I^2 + Q^2}$ (V)")
        plt.subplot(212, sharex=ax1)
        plt.cla()
        for j in range(len(qub_key_subset)):
            plt.plot((qub_spec_frequencies[j] - qubit_LO[j]) / u.MHz, signal.detrend(np.unwrap(phase[j])), label=f"Qubit {qub_key_subset[j]} at {qub_frequency[j]/u.GHz:.3f} GHz")
        plt.xlabel("Intermediate frequency (MHz)")
        plt.ylabel("Phase (rad)")
        plt.pause(0.1)
        plt.tight_layout()
    
    from qualang_tools.plot.fitting import Fit

    for j in range(len(qub_key_subset)):
        try:
            # Fit the data
            fit = Fit()
            plt.figure()
            spec_fit = fit.reflection_resonator_spectroscopy( (qub_spec_frequencies[j] - qubit_LO[j]) / u.MHz, R[j], plot=True) # I am using the opposite of what I used for resonator fit as a rough estimate for the qubit spectroscopy
            plt.title(f"Qubit {qub_key_subset[j]}, Qubit spectroscopy - LO = {qubit_LO / u.GHz} GHz")
            plt.xlabel("Intermediate frequency (MHz)")
            plt.ylabel(r"R=$\sqrt{I^2 + Q^2}$ (V)")
            print(f"Update qubit {qub_key_subset[j]} IF to {spec_fit['f'][0]:.6f} MHz")
        except (Exception,):
            print("Unable to fit qubit " + str(qub_key_subset[j]))
            plt.figure()
            plt.plot((qub_spec_frequencies[j] - qubit_LO[j]) / u.MHz, R[j])
            plt.title(f"Qubit {qub_key_subset[j]}, Qubit spectroscopy - LO = {qubit_LO / u.GHz} GHz")
            plt.xlabel("Intermediate frequency (MHz)")
            plt.ylabel(r"R=$\sqrt{I^2 + Q^2}$ (V)")

    # Save results
    script_name = Path(__file__).name
    data_handler = DataHandler(root_data_folder=save_dir)
    save_data_dict.update({"I_data": I})
    save_data_dict.update({"Q_data": Q})
    save_data_dict.update({"fig_live": fig})
    data_handler.additional_files = {script_name: script_name, **default_additional_files}
    data_handler.save_data(data=save_data_dict, name="_".join(script_name.split("_")[1:]).split(".")[0])
    
    qm.close()