"""
        POWER RABI
The sequence consists in playing the qubit pulse (x180 or square_pi or else) and measuring the state of the resonator
for different qubit pulse amplitudes.
The experimental results are then analyzed to find the qubit pulse amplitude for the chosen duration.

Prerequisites:
    - Having found the resonance frequency of the resonator coupled to the qubit under study (resonator_spectroscopy).
    - Having calibrated the IQ mixer connected to the qubit drive line (external mixer or Octave port)
    - Having found the rough qubit frequency and pi pulse duration (rabi_chevron_duration or time_rabi).
    - Set the qubit frequency and desired pi pulse duration (x180_len) in the configuration.

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

n_avg = 1000  # The number of averages
# Pulse amplitude sweep (as a pre-factor of the qubit pulse amplitude) - must be within [-2; 2)
a_min = 0
a_max = 1.0
n_a = 101
amplitudes = np.linspace(a_min, a_max, n_a)

power_rabi_data = {
    "n_avg": n_avg,
    "amplitudes": amplitudes,
    "config": config
}

with qua.program() as power_rabi:
    n = qua.declare(int)  # QUA variable for the averaging loop
    a = qua.declare(qua.fixed)  # QUA variable for the qubit drive amplitude pre-factor
    I = qua.declare(qua.fixed)  # QUA variable for the measured 'I' quadrature
    Q = qua.declare(qua.fixed)  # QUA variable for the measured 'Q' quadrature
    I_st = qua.declare_stream()  # Stream for the 'I' quadrature
    Q_st = qua.declare_stream()  # Stream for the 'Q' quadrature
    n_st = qua.declare_stream()  # Stream for the averaging iteration 'n'

    with qua.for_(n, 0, n < n_avg, n + 1):  # QUA for_ loop for averaging
        with qua.for_(*from_array(a, amplitudes)):  # QUA for_ loop for sweeping the pulse amplitude pre-factor
            # Play the qubit pulse with a variable amplitude (pre-factor to the pulse amplitude defined in the config)
            qua.play("x180" * qua.amp(a), "qubit")
            # Align the two elements to measure after playing the qubit pulse.
            qua.align("qubit", "resonator")
            # Measure the state of the resonator
            # The integration weights have changed to maximize the SNR after having calibrated the IQ blobs.
            qua.measure(
                "readout",
                "resonator",
                None,
                qua.dual_demod.full("rotated_cos", "out1", "rotated_sin", "out2", I),
                qua.dual_demod.full("rotated_minus_sin", "out1", "rotated_cos", "out2", Q),
            )
            # Wait for the qubit to decay to the ground state
            qua.wait(thermalization_time * u.ns, "resonator")
            # Save the 'I' & 'Q' quadratures to their respective streams
            qua.save(I, I_st)
            qua.save(Q, Q_st)
        # Save the averaging iteration to get the progress bar
        qua.save(n, n_st)

    with qua.stream_processing():
        # Cast the data into a 1D vector, average the 1D vectors together and store the results on the OPX processor
        I_st.buffer(len(amplitudes)).average().save("I")
        Q_st.buffer(len(amplitudes)).average().save("Q")
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
    job = qmm.simulate(config, power_rabi, simulation_config)
    job.get_simulated_samples().con1.plot()

else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(power_rabi)
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
        progress_counter(iteration, n_avg, start_time=results.get_start_time())
        # Plot results
        plt.suptitle("Power Rabi")
        plt.subplot(211)
        plt.cla()
        plt.plot(amplitudes * x180_amp, I, ".")
        plt.ylabel("I quadrature [V]")
        plt.subplot(212)
        plt.cla()
        plt.plot(amplitudes * x180_amp, Q, ".")
        plt.xlabel("Rabi pulse amplitude [V]")
        plt.ylabel("Q quadrature [V]")
        plt.pause(1)
        plt.tight_layout()

    power_rabi_data["I"] = I
    power_rabi_data["Q"] = Q
    power_rabi_data["x180_amp"] = x180_amp

    # Save the data
    data_handler.save_data(power_rabi_data, "power_rabi")