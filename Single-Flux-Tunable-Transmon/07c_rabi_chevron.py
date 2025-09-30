"""
        RABI CHEVRON (AMPLITUDE VS FREQUENCY)
This sequence involves executing the qubit pulse and measuring the state
of the resonator across various qubit intermediate frequencies and pulse amplitudes.
By analyzing the results, one can determine the qubit and estimate the x180 pulse amplitude for a specified duration.

Prerequisites:
    - Determination of the resonator's resonance frequency when coupled to the qubit of interest (referred to as "resonator_spectroscopy").
    - Calibration of the IQ mixer connected to the qubit drive line (be it an external mixer or an Octave port).
    - Identification of the approximate qubit frequency (referred to as "qubit_spectroscopy").
    - Configuration of the qubit frequency and the desired pi pulse duration (labeled as "pi_len_q").
    - Set the desired flux bias

Before proceeding to the next node:
    - Adjust the qubit frequency setting, labeled as "qubit_IF_q", in the configuration.
    - Modify the qubit pulse amplitude setting, labeled as "pi_amp_q", in the configuration.
"""

from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from configuration import *
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.loops import from_array
import matplotlib.pyplot as plt
from qualang_tools.results.data_handler import DataHandler




###################
# The QUA program #
###################
n_avg = 1000  # The number of averages
# Qubit pulse duration sweep
times = np.arange(1, 75, 1)  # In clock cycles = 4ns
# Qubit pulse amplitude sweep (as a pre-factor of the qubit pulse amplitude) - must be within [-2; 2)
amps = np.arange(0.01, 1.99, 0.01)

save_data_dict = {
    "n_avg": n_avg,
    "durations": times,
    "amplitudes": amps,
    "config": config,
}

# Data to save
with program() as rabi_chevron:
    n = declare(int)  # QUA variable for the averaging loop
    I = declare(fixed)  # QUA variable for the measured 'I' quadrature
    Q = declare(fixed)  # QUA variable for the measured 'Q' quadrature
    I_st = declare_stream()  # Stream for the 'I' quadrature
    Q_st = declare_stream()  # Stream for the 'Q' quadrature
    n_st = declare_stream()  # Stream for the averaging iteration 'n'
    t = declare(int)  # QUA variable for the qubit detuning
    a = declare(fixed)  # QUA variable for the qubit pulse amplitude pre-factor
    # update_frequency("q1_xy", qubit_IF_q1-15e6)
    reset_global_phase()
    set_dc_offset("flux_line", "single", max_frequency_point)
    wait(flux_settle_time * u.ns)
    align()

    with for_(n, 0, n < n_avg, n + 1):
        with for_(*from_array(t, times)):
            # Update the frequency of the two qubit elements
            with for_(*from_array(a, amps)):
                # Play qubit pulses simultaneously
                # play("x180" * amp(a), "q1_xy", duration = t)
                play("x180" * amp(a), "qubit", duration = t)

                # Measure after the qubit pulses
                align()
                # Multiplexed readout, also saves the measurement outcomes
                measure(
                "readout",
                "resonator",
                None,
                dual_demod.full("rotated_cos", "rotated_sin", I),
                dual_demod.full("rotated_minus_sin", "rotated_cos", Q),
                )
                # Wait for the qubit to decay to the ground state
                wait(thermalization_time * u.ns)

                save(I, I_st)
                save(Q, Q_st)
        # Save the averaging iteration to get the progress bar
        save(n, n_st)

    with stream_processing():
        
        I_st.buffer(len(amps)).buffer(len(times)).average().save("I")
        Q_st.buffer(len(amps)).buffer(len(times)).average().save("Q")
        n_st.save("n")



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
    job = qmm.simulate(config,rabi_chevron , simulation_config)
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
    job = qm.execute(rabi_chevron)
    # Tool to easily fetch results from the OPX (results_handle used in it)
    results = fetching_tool(job, ["n", "I", "Q"], mode="live")
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)
    while results.is_processing():
        # Fetch results
        n, I, Q,= results.fetch_all()
        # Progress bar
        progress_counter(n, n_avg, start_time=results.start_time)
        # Convert the results into Volts
        I, Q = u.demod2volts(I, readout_len), u.demod2volts(Q, readout_len)       
        S= u.demod2volts(I + 1j * Q, readout_len)
        R = np.abs(S)
        phase = np.angle(S)

        # Plots
        plt.suptitle("Rabi chevron")
        plt.subplot(211)
        plt.cla()
        plt.pcolor(amps * x180_amp, 4 * times, R)
        plt.xlabel("Qubit pulse amplitude [V]")
        plt.ylabel("Qubit pulse duration [ns]")
        plt.title(f"q1 (f_res: {(qubit_LO+ qubit_IF)} MHz)")
        plt.subplot(212)
        plt.cla()
        plt.pcolor(amps * x180_amp, 4 * times, np.unwrap(phase))
        plt.xlabel("Qubit pulse amplitude [V]")
        plt.ylabel("Qubit pulse duration [ns]")
        plt.tight_layout()
        plt.pause(0.1)



# Save results
script_name = Path(__file__).name
data_handler = DataHandler(root_data_folder=save_dir)
save_data_dict.update({"I_data": I})
save_data_dict.update({"Q_data": Q})
save_data_dict.update({"fig_live": fig})
data_handler.additional_files = {script_name: script_name}
data_handler.save_data(data=save_data_dict, name=script_name.rsplit(".", 1)[0])

# Close the quantum machines at the end in order to put all flux biases to 0 so that the fridge doesn't heat-up
qm.close()
plt.show(block=True)
