"""
        RESONATOR DEPLETION TIME
This sequence is designed to measure the resonator depletion time.
It begins by sending a MW pulse to the resonator to fill it with photons via measure().
Subsequently, a Ramsey measurement is performed after allowing a variable waiting time (structured as:
wait(t) - x90 - idle_time - x90 - measurement). Given that the qubit frequency is influenced by the number of photons
in the resonator, an exponential decay should be evident in the measured I/Q quadratures.
This provides insight into the resonator depletion time, which can then be updated in the configuration.

Prerequisites:
    - Having found the resonance frequency of the resonator coupled to the qubit under study (resonator_spectroscopy).
    - Having calibrated qubit pi pulse (x180) by running qubit, spectroscopy, rabi_chevron, power_rabi and updated the config.
    - Having precisely measured the qubit frequency (ramsey).

Next steps before going to the next node:
    - Update the resonator depletion time (depletion_time) in the configuration.
"""

import qm.qua as qua
import qm as qm_api
import numpy as np
from configuration import config, qop_ip, cluster_name, u, thermalization_time, readout_len, resonator_LO
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.loops import from_array
import matplotlib.pyplot as plt
from qualang_tools.results.data_handler import DataHandler

data_handler = DataHandler(root_data_folder="./")

###################
# The QUA program #
###################

n_avg = 1_000
ramsey_idle_time = 1 * u.us
# Time between populating the resonator and playing a Ramsey sequence in clock-cycles (4ns)
taus = np.arange(4, 1000, 1)

res_depletion_time_data = {
    "n_avg": n_avg,
    "taus": taus,
    "config": config
}

with qua.program() as res_depletion_time:
    n = qua.declare(int)
    n_st = qua.declare_stream()
    t = qua.declare(int)
    I = qua.declare(qua.fixed)
    Q = qua.declare(qua.fixed)
    I_st = qua.declare_stream()
    Q_st = qua.declare_stream()

    with qua.for_(n, 0, n < n_avg, n + 1):
        # Save the averaging iteration to get the progress bar
        qua.save(n, n_st)
        with qua.for_(*from_array(t, taus)):
            # Fill the resonator with photons
            qua.measure(
                "readout",
                "resonator",
                None,
                qua.dual_demod.full("rotated_cos", "out1", "rotated_sin", "out2", I),
                qua.dual_demod.full("rotated_minus_sin", "out1", "rotated_cos", "out2", Q),
            )
            # Play a fixed duration Ramsey sequence after a varying time to estimate the effect of photons in the resonator
            qua.wait(t, "resonator")
            # Align the two elements to play the Ramsey sequence after having waited for a varying time "t".
            qua.align("qubit", "resonator")
            # Play the Ramsey sequence
            qua.play("x90", "qubit")
            qua.wait(ramsey_idle_time * u.ns)  # fixed time ramsey
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
            # Save the 'I' & 'Q' quadratures to their respective streams
            qua.save(I, I_st)
            qua.save(Q, Q_st)

    with qua.stream_processing():
        # Cast the data into a 1D vector, average the 1D vectors together and store the results on the OPX processor
        I_st.buffer(len(taus)).average().save("I")
        Q_st.buffer(len(taus)).average().save("Q")
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
    job = qmm.simulate(config, res_depletion_time, simulation_config)
    job.get_simulated_samples().con1.plot()

else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(res_depletion_time)
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
        plt.suptitle("Resonator depletion time")
        plt.subplot(211)
        plt.cla()
        plt.plot(4 * taus, I, ".")
        plt.ylabel("I quadrature [V]")
        plt.subplot(212)
        plt.cla()
        plt.plot(4 * taus, Q, ".")
        plt.xlabel("Delay [ns]")
        plt.ylabel("Q quadrature [V]")
        plt.tight_layout()
        plt.pause(1)

    data_handler.save_data(res_depletion_time_data, "res_depletion_time")

    # Fit the results to extract the resonator depletion time
    try:
        from qualang_tools.plot.fitting import Fit

        fit = Fit()
        plt.figure()
        decay_fit = fit.T1(4 * taus, I, plot=True)
        depletion_time = np.round(np.abs(decay_fit["T1"][0]) / 4) * 4
        plt.xlabel("Delay [ns]")
        plt.ylabel("I quadrature [V]")
        print(f"Resonator depletion time to update in the config: depletion_time = {depletion_time:.0f} ns")
        plt.legend((f"depletion time = {depletion_time:.0f} ns",))
    except (Exception,):
        pass