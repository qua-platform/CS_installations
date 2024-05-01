"""
        READOUT OPTIMISATION: AMPLITUDE
The sequence consists in measuring the state of the resonator after thermalization (qubit in |g>) and after
playing a pi pulse to the qubit (qubit in |e>) successively while sweeping the readout amplitude.
The 'I' & 'Q' quadratures when the qubit is in |g> and |e> are extracted to derive the readout fidelity.
The optimal readout amplitude is chosen as to maximize the readout fidelity.

Prerequisites:
    - Having found the resonance frequency of the resonator coupled to the qubit under study (resonator_spectroscopy).
    - Having calibrated qubit pi pulse (x180) by running qubit, spectroscopy, rabi_chevron, power_rabi and updated the config.
    - Having calibrated the readout frequency and updated the configuration.

Next steps before going to the next node:
    - Update the readout amplitude (readout_amp) in the configuration.
"""


import qm.qua as qua
import qm as qm_api
import numpy as np
from configuration import config, qop_ip, cluster_name, u, thermalization_time, readout_amp
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.analysis import two_state_discriminator
from qualang_tools.loops import from_array
import matplotlib.pyplot as plt
from qualang_tools.results.data_handler import DataHandler

data_handler = DataHandler(root_data_folder="./")

###################
# The QUA program #
###################
n_runs = 1000
# The readout amplitude sweep (as a pre-factor of the readout amplitude) - must be within [-2; 2)
a_min = 0.5
a_max = 1.5
da = 0.01
amplitudes = np.arange(a_min, a_max + da / 2, da)  # The amplitude vector +da/2 to add a_max to the scan

ro_opt_amp_data = {
    "n_runs": n_runs,
    "amplitudes": amplitudes,
    "config": config,
}

with qua.program() as ro_amp_opt:
    n = qua.declare(int)  # QUA variable for the number of runs
    counter = qua.declare(int, value=0)  # Counter for the progress bar
    a = qua.declare(qua.fixed)  # QUA variable for the readout amplitude
    I_g = qua.declare(qua.fixed)  # QUA variable for the 'I' quadrature when the qubit is in |g>
    Q_g = qua.declare(qua.fixed)  # QUA variable for the 'Q' quadrature when the qubit is in |g>
    I_g_st = qua.declare_stream()
    Q_g_st = qua.declare_stream()
    I_e = qua.declare(qua.fixed)  # QUA variable for the 'I' quadrature when the qubit is in |e>
    Q_e = qua.declare(qua.fixed)  # QUA variable for the 'Q' quadrature when the qubit is in |e>
    I_e_st = qua.declare_stream()
    Q_e_st = qua.declare_stream()
    n_st = qua.declare_stream()

    with qua.for_(*from_array(a, amplitudes)):
        qua.save(counter, n_st)
        with qua.for_(n, 0, n < n_runs, n + 1):
            qua.measure(
                "readout" * qua.amp(a),
                "resonator",
                None,
                qua.dual_demod.full("rotated_cos", "out1", "rotated_sin", "out2", I_g),
                qua.dual_demod.full("rotated_minus_sin", "out1", "rotated_cos", "out2", Q_g),
            )
            # Wait for the qubit to decay to the ground state
            qua.wait(thermalization_time * u.ns, "resonator")
            # Save the 'I_e' & 'Q_e' quadratures to their respective streams
            qua.save(I_g, I_g_st)
            qua.save(Q_g, Q_g_st)

            qua.align()  # global align
            # Play the x180 gate to put the qubit in the excited state
            qua.play("x180", "qubit")
            # Align the two elements to measure after playing the qubit pulse.
            qua.align("qubit", "resonator")
            # Measure the state of the resonator
            qua.measure(
                "readout" * qua.amp(a),
                "resonator",
                None,
                qua.dual_demod.full("rotated_cos", "out1", "rotated_sin", "out2", I_e),
                qua.dual_demod.full("rotated_minus_sin", "out1", "rotated_cos", "out2", Q_e),
            )
            # Wait for the qubit to decay to the ground state
            qua.wait(thermalization_time * u.ns, "resonator")
            # Save the 'I_e' & 'Q_e' quadratures to their respective streams
            qua.save(I_e, I_e_st)
            qua.save(Q_e, Q_e_st)
        # Save the counter to get the progress bar
        qua.assign(counter, counter + 1)

    with qua.stream_processing():
        # mean values
        I_g_st.buffer(n_runs).buffer(len(amplitudes)).save("I_g")
        Q_g_st.buffer(n_runs).buffer(len(amplitudes)).save("Q_g")
        I_e_st.buffer(n_runs).buffer(len(amplitudes)).save("I_e")
        Q_e_st.buffer(n_runs).buffer(len(amplitudes)).save("Q_e")
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
    job = qmm.simulate(config, ro_amp_opt, simulation_config)
    job.get_simulated_samples().con1.plot()

else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(ro_amp_opt)  # execute QUA program
    # Get results from QUA program
    results = fetching_tool(job, data_list=["iteration"], mode="live")
    # Get progress counter to monitor runtime of the program
    while results.is_processing():
        # Fetch results
        iteration = results.fetch_all()
        # Progress bar
        progress_counter(iteration[0], len(amplitudes), start_time=results.get_start_time())

    # Fetch the results at the end
    results = fetching_tool(job, data_list=["I_g", "Q_g", "I_e", "Q_e"])
    I_g, Q_g, I_e, Q_e = results.fetch_all()

    # Process the data
    fidelity_vec = []
    ground_fidelity_vec = []
    for i in range(len(amplitudes)):
        angle, threshold, fidelity, gg, ge, eg, ee = two_state_discriminator(
            I_g[i], Q_g[i], I_e[i], Q_e[i], b_print=False, b_plot=False
        )
        fidelity_vec.append(fidelity)
        ground_fidelity_vec.append(gg)


    # Save the data
    ro_opt_amp_data['I_g'] = I_g
    ro_opt_amp_data['Q_g'] = Q_g
    ro_opt_amp_data['I_e'] = I_e
    ro_opt_amp_data['Q_e'] = Q_e
    ro_opt_amp_data["fidelity_vec"] = fidelity_vec
    ro_opt_amp_data["ground_fidelity_vec"] = ground_fidelity_vec
    data_handler.save(ro_opt_amp_data, "ro_opt_amp_data")

    # Plot the data
    plt.figure()
    plt.plot(amplitudes * readout_amp, fidelity_vec, "b.-", label="averaged fidelity")
    plt.plot(amplitudes * readout_amp, ground_fidelity_vec, "r.-", label="ground fidelity")
    plt.title("Readout amplitude optimization")
    plt.xlabel("Readout amplitude [V]")
    plt.ylabel("Readout fidelity [%]")
    plt.legend(
        (
            f"readout_amp = {readout_amp * amplitudes[np.argmax(fidelity_vec)] / u.mV:.3f} mV, for {max(fidelity_vec):.1f}% averaged fidelity",
            f"readout_amp = {readout_amp * amplitudes[np.argmax(ground_fidelity_vec)] / u.mV:.3f} mV, for {max(ground_fidelity_vec):.1f}% ground fidelity",
        )
    )
    print(
        f"The optimal readout amplitude is {readout_amp * amplitudes[np.argmax(fidelity_vec)] / u.mV:.3f} mV (Averaged fidelity={max(fidelity_vec):.1f}%)"
    )
    print(
        f"The optimal readout amplitude is {readout_amp * amplitudes[np.argmax(ground_fidelity_vec)] / u.mV:.3f} mV (Ground fidelity={max(ground_fidelity_vec):.1f}%)"
    )