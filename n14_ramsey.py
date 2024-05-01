"""
        RAMSEY WITH VIRTUAL Z ROTATIONS
The program consists in playing a Ramsey sequence (x90 - idle_time - x90 - measurement) for different idle times.
Instead of detuning the qubit gates, the frame of the second x90 pulse is rotated (de-phased) to mimic an accumulated
phase acquired for a given detuning after the idle time.
This method has the advantage of playing resonant gates.

From the results, one can fit the Ramsey oscillations and precisely measure the qubit resonance frequency and T2*.

Prerequisites:
    - Having found the resonance frequency of the resonator coupled to the qubit under study (resonator_spectroscopy).
    - Having calibrated qubit pi pulse (x180) by running qubit, spectroscopy, rabi_chevron, power_rabi and updated the config.
    - (optional) Having calibrated the readout (readout_frequency, amplitude, duration_optimization IQ_blobs) for better SNR.

Next steps before going to the next node:
    - Update the qubit frequency (qubit_IF) in the configuration.
"""

import qm.qua as qua
import qm as qm_api
import numpy as np
from configuration import config, qop_ip, cluster_name, u, thermalization_time, readout_len, ge_threshold
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.loops import from_array
import matplotlib.pyplot as plt
from qualang_tools.results.data_handler import DataHandler

data_handler = DataHandler(root_data_folder="./")

###################
# The QUA program #
###################
n_avg = 1000
# Dephasing time sweep (in clock cycles = 4ns) - minimum is 4 clock cycles
tau_min = 4
tau_max = 2000 // 4
d_tau = 40 // 4
taus = np.arange(tau_min, tau_max + 0.1, d_tau)  # + 0.1 to add tau_max to taus
# Detuning converted into virtual Z-rotations to observe Ramsey oscillation and get the qubit frequency
detuning = 1 * u.MHz  # in Hz
delta_phase = 4e-09 * detuning * d_tau # 4*tau because tau was in clock cycles and 1e-9 because tau is ns
phase_init = 4e-09 * detuning * tau_min

ramsey_data = {
    "n_avg": n_avg,
    "taus": taus,
    "detuning": detuning,
    "config": config
}

with qua.program() as ramsey:
    n = qua.declare(int)  # QUA variable for the averaging loop
    tau = qua.declare(int)  # QUA variable for the idle time
    phase = qua.declare(qua.fixed)  # QUA variable for dephasing the second pi/2 pulse (virtual Z-rotation)
    I = qua.declare(qua.fixed)  # QUA variable for the measured 'I' quadrature
    Q = qua.declare(qua.fixed)  # QUA variable for the measured 'Q' quadrature
    state = qua.declare(bool)  # QUA variable for the qubit state
    I_st = qua.declare_stream()  # Stream for the 'I' quadrature
    Q_st = qua.declare_stream()  # Stream for the 'Q' quadrature
    state_st = qua.declare_stream()  # Stream for the qubit state
    n_st = qua.declare_stream()  # Stream for the averaging iteration 'n'

    with qua.for_(n, 0, n < n_avg, n + 1):
        # Save the averaging iteration to get the progress bar
        qua.save(n, n_st)
        qua.assign(phase, phase_init)
        with qua.for_(*from_array(tau, taus)):

            # 1st x90 gate
            qua.play("x90", "qubit")
            # Wait a varying idle time
            qua.wait(tau, "qubit")
            # Rotate the frame of the second x90 gate to implement a virtual Z-rotation
            qua.frame_rotation_2pi(phase, "qubit")
            # 2nd x90 gate
            qua.play("x90", "qubit")

            # Align the two elements to measure after playing the qubit pulse.
            qua.align("qubit", "resonator")
            # Measure the state of the resonator
            qua.measure(
                "readout",
                "resonator",
                None,
                qua.dual_demod.full("rotated_cos", "out1", "rotated_sin", "out2", I),
                qua.dual_demod.full("rotated_minus_sin", "out1", "rotated_cos", "out2", Q),
            )
            # Wait for the qubit to decay to the ground state
            qua.wait(thermalization_time * u.ns, "resonator")
            # State discrimination
            qua.assign(state, I > ge_threshold)
            # Save the 'I', 'Q' and 'state' to their respective streams
            qua.save(I, I_st)
            qua.save(Q, Q_st)
            qua.save(state, state_st)

            # Reset the frame of the qubit in order not to accumulate rotations
            qua.reset_frame("qubit")

            qua.assign(phase, phase + delta_phase)

    with qua.stream_processing():
        # Cast the data into a 1D vector, average the 1D vectors together and store the results on the OPX processor
        I_st.buffer(len(taus)).average().save("I")
        Q_st.buffer(len(taus)).average().save("Q")
        state_st.boolean_to_int().buffer(len(taus)).average().save("state")
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
    job = qmm.simulate(config, ramsey, simulation_config)
    job.get_simulated_samples().con1.plot()
else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(ramsey)
    # Get results from QUA program
    results = fetching_tool(job, data_list=["I", "Q", "state", "iteration"], mode="live")
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    while results.is_processing():
        # Fetch results
        I, Q, state, iteration = results.fetch_all()
        # Convert the results into Volts
        I, Q = u.demod2volts(I, readout_len), u.demod2volts(Q, readout_len)
        # Progress bar
        progress_counter(iteration, n_avg, start_time=results.get_start_time())
        # Plot results
        plt.suptitle(f"Ramsey with frame rotation (detuning={detuning / u.MHz} MHz)")
        plt.subplot(311)
        plt.cla()
        plt.plot(4 * taus, I, ".")
        plt.ylabel("I quadrature [V]")
        plt.subplot(312)
        plt.cla()
        plt.plot(4 * taus, Q, ".")
        plt.ylabel("Q quadrature [V]")
        plt.subplot(313)
        plt.cla()
        plt.plot(4 * taus, state, ".")
        plt.ylim((0, 1))
        plt.xlabel("Idle time [ns]")
        plt.ylabel("State")
        plt.tight_layout()
        plt.pause(1)

    # Save the results
    ramsey_data["I"] = I
    ramsey_data["Q"] = Q
    ramsey_data["state"] = state
    data_handler.save_data(data=ramsey_data, name="ramsey")

    # Fit the results to extract the qubit frequency and T2*
    try:
        from qualang_tools.plot.fitting import Fit

        fit = Fit()
        plt.figure()
        ramsey_fit = fit.ramsey(4 * taus, I, plot=True)
        qubit_T2 = np.abs(ramsey_fit["T2"][0])
        qubit_detuning = ramsey_fit["f"][0] * u.GHz - detuning
        plt.xlabel("Idle time [ns]")
        plt.ylabel("I quadrature [V]")
        print(f"Qubit detuning to update in the config: qubit_IF += {-qubit_detuning:.0f} Hz")
        print(f"T2* = {qubit_T2:.0f} ns")
        plt.legend((f"detuning = {-qubit_detuning / u.kHz:.3f} kHz", f"T2* = {qubit_T2:.0f} ns"))
        plt.title("Ramsey measurement with virtual Z rotations")
        print(f"Detuning to add: {-qubit_detuning / u.kHz:.3f} kHz")
    except (Exception,):
        pass