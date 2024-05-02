# %%
"""
        POWER RABI WITH ERROR AMPLIFICATION
This sequence involves repeatedly executing the qubit pulse (such as x180, square_pi, or similar) 'N' times and
measuring the state of the resonator across different qubit pulse amplitudes and number of pulses.
By doing so, the effect of amplitude inaccuracies is amplified, enabling a more precise measurement of the pi pulse
amplitude. The results are then analyzed to determine the qubit pulse amplitude suitable for the selected duration.

Prerequisites:
    - Having found the resonance frequency of the resonator coupled to the qubit under study (resonator_spectroscopy).
    - Having calibrated the IQ mixer connected to the qubit drive line (external mixer or Octave port)
    - Having found the rough qubit frequency and pi pulse duration (rabi_chevron_duration or time_rabi).
    - Having found the pi pulse amplitude (power_rabi).
    - Set the qubit frequency, desired pi pulse duration and rough pi pulse amplitude in the configuration.

Next steps before going to the next node:
    - Update the qubit pulse amplitude (x180_amp) in the configuration.
"""

import qm.qua as qua
import qm as qm_api
import numpy as np
from configuration import config, qop_ip, cluster_name, u, readout_len, thermalization_time, x180_amp
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.loops import from_array
import matplotlib.pyplot as plt
from qualang_tools.results.data_handler import DataHandler

data_handler = DataHandler(root_data_folder="./")

###################
# The QUA program #
###################
n_avg = 10  # The number of averages
# Pulse amplitude sweep (as a pre-factor of the qubit pulse amplitude) - must be within [-2; 2)
a_min = 0.5
a_max = 1.5
n_a = 51
amplitudes = np.linspace(a_min, a_max, n_a)
# Number of applied Rabi pulses sweep
max_nb_of_pulses = 80  # Maximum number of qubit pulses
nb_of_pulses = np.arange(0, max_nb_of_pulses, 2)  # Always play an odd/even number of pulses to end up in the same state

error_amplification_power_rabi_data = {
    "n_avg": n_avg,
    "amplitudes": amplitudes,
    "nb_of_pulses": nb_of_pulses,
    "config": config
}

with qua.program() as power_rabi_err:
    n = qua.declare(int)  # QUA variable for the averaging loop
    a = qua.declare(qua.fixed)  # QUA variable for the qubit drive amplitude pre-factor
    n_rabi = qua.declare(int)  # QUA variable for the number of qubit pulses
    n2 = qua.declare(int)  # QUA variable for counting the qubit pulses
    I = qua.declare(qua.fixed)  # QUA variable for the measured 'I' quadrature
    Q = qua.declare(qua.fixed)  # QUA variable for the measured 'Q' quadrature
    I_st = qua.declare_stream()  # Stream for the 'I' quadrature
    Q_st = qua.declare_stream()  # Stream for the 'Q' quadrature
    n_st = qua.declare_stream()  # Stream for the averaging iteration 'n'

    with qua.for_(n, 0, n < n_avg, n + 1):  # QUA for_ loop for averaging
        # Save the averaging iteration to get the progress bar
        qua.save(n, n_st)
        with qua.for_(*from_array(n_rabi, nb_of_pulses)):  # QUA for_ loop for sweeping the number of pulses
            with qua.for_(*from_array(a, amplitudes)):  # QUA for_ loop for sweeping the pulse amplitude
                # Loop for error amplification (perform many qubit pulses with varying amplitudes)
                with qua.for_(n2, 0, n2 < n_rabi, n2 + 1):
                    qua.play("x180" * qua.amp(a), "qubit")
                # Align the two elements to measure after playing the qubit pulses.
                qua.align("qubit", "resonator")
                # Measure the state of the resonator
                # The integration weights have changed to maximize the SNR after having calibrated the IQ blobs.
                qua.measure(
                    "readout",
                    "resonator",
                    None,
                    # qua.dual_demod.full("rotated_cos", "out1", "rotated_sin", "out2", I),
                    # qua.dual_demod.full("rotated_minus_sin", "out1", "rotated_cos", "out2", Q),
                    qua.dual_demod.full("opt_cos", "out1", "opt_sin", "out2", I),
                    qua.dual_demod.full("opt_minus_sin", "out1", "opt_cos", "out2", Q),
                )
                # Wait for the qubit to decay to the ground state
                qua.wait(thermalization_time * u.ns, "resonator")
                # Save the 'I' & 'Q' quadratures to their respective streams
                qua.save(I, I_st)
                qua.save(Q, Q_st)

    with qua.stream_processing():
        # Cast the data into a 2D matrix, average the 2D matrices together and store the results on the OPX processor
        I_st.buffer(len(amplitudes)).buffer(len(nb_of_pulses)).average().save("I")
        Q_st.buffer(len(amplitudes)).buffer(len(nb_of_pulses)).average().save("Q")
        n_st.save("iteration")

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = qm_api.QuantumMachinesManager(host=qop_ip, cluster_name=cluster_name)

###########################
# Run or Simulate Program #
###########################
simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = qm_api.SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, power_rabi_err, simulation_config)
    job.get_simulated_samples().con1.plot()

else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(power_rabi_err)
    # Get results from QUA program
    results = fetching_tool(job, data_list=["I", "Q", "iteration"], mode="live")
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    while results.is_processing():
        # Fetch results
        I, Q, iteration = results.fetch_all()
        # Convert the results into Volts
        I, Q = u.demod2volts(I, readout_len), u.demod2volts(Q, readout_len)
        # Progress bar
        elapsed_time = progress_counter(iteration, n_avg, start_time=results.get_start_time())
        # Plot results
        # plt.suptitle(f"Power Rabi with error amplification, {elapsed_time:.3f} secs")
        plt.suptitle(f"Power Rabi with error amplification")
        plt.subplot(221)
        plt.cla()
        plt.pcolor(amplitudes * x180_amp, nb_of_pulses, I)
        plt.xlabel("Rabi pulse amplitude [V]")
        plt.ylabel("# of Rabi pulses")
        plt.title("I quadrature [V]")
        plt.subplot(222)
        plt.cla()
        plt.pcolor(amplitudes * x180_amp, nb_of_pulses, Q)
        plt.xlabel("Rabi pulse amplitude [V]")
        plt.title("Q quadrature [V]")
        plt.subplot(212)
        plt.cla()
        plt.plot(amplitudes * x180_amp, np.sum(I, axis=0))
        plt.ylim(0, 0.008)
        plt.xlabel("Rabi pulse amplitude [V]")
        plt.ylabel("Sum along the # of Rabi pulses")
        plt.tight_layout()
        plt.pause(1)
        
    print(f"Optimal x180_amp = {amplitudes[np.argmin(np.sum(I, axis=0))] * x180_amp:.4f} V")

    error_amplification_power_rabi_data["I"] = I
    error_amplification_power_rabi_data["Q"] = Q
    error_amplification_power_rabi_data["elapsed_time"] = elapsed_time

    data_handler.save_data(data=error_amplification_power_rabi_data, name="error_amplification_power_rabi")
# %%
