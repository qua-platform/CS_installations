# %%
"""
        ECHO MEASUREMENT
The program consists in playing a Ramsey sequence with an echo pulse in the middle to compensate for dephasing and
enhance the coherence time (x90 - idle_time - x180 - idle_time - x90 - measurement) for different idle times.
Here the gates are on resonance so no oscillation is expected.

From the results, one can fit the exponential decay and extract T2.

Prerequisites:
    - Having found the resonance frequency of the resonator coupled to the qubit under study (resonator_spectroscopy).
    - Having calibrated qubit pi pulse (x180) by running qubit, spectroscopy, rabi_chevron, power_rabi and updated the config.
    - Having the qubit frequency perfectly calibrated (ramsey).
    - (optional) Having calibrated the readout (readout_frequency, amplitude, duration_optimization IQ_blobs) for better SNR.
"""


import qm.qua as qua
import qm as qm_api
import numpy as np
from configuration import config, qop_ip, cluster_name, u, thermalization_time, readout_len, ge_threshold
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.loops import from_array, get_equivalent_log_array
import matplotlib.pyplot as plt
from qualang_tools.results.data_handler import DataHandler

data_handler = DataHandler(root_data_folder="./")

###################
# The QUA program #
###################
n_avg = 100
# Dephasing time sweep (in clock cycles = 4ns) - minimum is 4 clock cycles
tau_min = 4
tau_max = 800_000 // 4
d_tau = 1000 // 4
taus = np.arange(tau_min, tau_max + 0.1, d_tau)  # Linear sweep
# taus = np.logspace(np.log10(tau_min), np.log10(tau_max), 21)  # Log sweep

echo_data = {
    "n_avg": n_avg,
    "taus": taus,
    "config": config
}

with qua.program() as echo:
    n = qua.declare(int)
    n_st = qua.declare_stream()
    I = qua.declare(qua.fixed)
    I_st = qua.declare_stream()
    Q = qua.declare(qua.fixed)
    Q_st = qua.declare_stream()
    tau = qua.declare(int)
    state = qua.declare(bool)
    state_st = qua.declare_stream()

    with qua.for_(n, 0, n < n_avg, n + 1):
        # Save the averaging iteration to get the progress bar
        qua.save(n, n_st)
        with qua.for_(*from_array(tau, taus)):
            # 1st x90 pulse
            qua.play("x90", "qubit")
            # Wait the varying idle time
            qua.wait(tau, "qubit")
            # Echo pulse
            qua.play("x180", "qubit")
            # Wait the varying idle time
            qua.wait(tau, "qubit")
            # 2nd x90 pulse
            qua.play("x90", "qubit")
            # Align the two elements to measure after playing the qubit pulse.
            qua.align("qubit", "resonator")
            # Measure the state of the resonator
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
            qua.assign(state, I > ge_threshold)
            qua.wait(thermalization_time * u.ns, "resonator")
            # Save the 'I' & 'Q' quadratures to their respective streams
            qua.save(I, I_st)
            qua.save(Q, Q_st)
            qua.save(state, state_st)

    with qua.stream_processing():
        # Cast the data into a 1D vector, average the 1D vectors together and store the results on the OPX processor
        # If log sweep, then the swept values will be slightly different from np.logspace because of integer rounding in QUA.
        # get_equivalent_log_array() is used to get the exact values used in the QUA program.
        if np.isclose(np.std(taus[1:] / taus[:-1]), 0, atol=1e-3):
            taus = get_equivalent_log_array(taus)
            I_st.buffer(len(taus)).average().save("I")
            Q_st.buffer(len(taus)).average().save("Q")
            state_st.boolean_to_int().buffer(len(taus)).average().save("state")
        else:
            I_st.buffer(len(taus)).average().save("I")
            Q_st.buffer(len(taus)).average().save("Q")
            state_st.boolean_to_int().buffer(len(taus)).average().save("state")
        n_st.save("iteration")

######################################
#  Open Communication with the QOP  #
######################################
qmm = qm_api.QuantumMachinesManager(host=qop_ip, cluster_name=cluster_name)

###########################
# Run or Simulate Program #
###########################
simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = qm_api.SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, echo, simulation_config)
    job.get_simulated_samples().con1.plot()

else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(echo)
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
        elapsed_time = progress_counter(iteration, n_avg, start_time=results.get_start_time())
        # Plot results
        plt.suptitle(f"Echo measurement")
        plt.subplot(211)
        plt.cla()
        plt.plot(8 * taus, I)
        plt.ylabel("I quadrature [V]")
        plt.subplot(212)
        plt.cla()
        plt.plot(8 * taus, state)
        plt.xlabel("Idle time [ns]")
        plt.ylabel("Q quadrature [V]")
        plt.tight_layout()
        plt.pause(1)
        
    # Save the results
    echo_data["I"] = I
    echo_data["Q"] = Q
    echo_data["state"] = state
    echo_data['elapsed_time'] = elapsed_time
    
    data_handler.save_data(data=echo_data, name="echo")

    # Fit the results to extract the qubit coherence time T2
    try:
        from qualang_tools.plot.fitting import Fit

        fit = Fit()
        plt.figure()
        T2_fit = fit.T1(8 * taus, I, plot=True)
        qubit_T2 = np.abs(T2_fit["T1"][0])
        plt.xlabel("Delay [ns]")
        plt.ylabel("I quadrature [V]")
        print(f"Qubit coherence time T2 = {qubit_T2:.0f} ns")
        plt.legend((f"Coherence time T2 = {qubit_T2:.0f} ns",))
        plt.title("Echo measurement")
    except (Exception,):
        pass
# %%
