# %%
"""
        IQ BLOBS
This sequence involves measuring the state of the resonator 'N' times, first after thermalization (with the qubit
in the |g> state) and then after applying a pi pulse to the qubit (bringing the qubit to the |e> state) successively.
The resulting IQ blobs are displayed, and the data is processed to determine:
    - The rotation angle required for the integration weights, ensuring that the separation between |g> and |e> states
      aligns with the 'I' quadrature.
    - The threshold along the 'I' quadrature for effective qubit state discrimination.
    - The readout fidelity matrix, which is also influenced by the pi pulse fidelity.

Prerequisites:
    - Having found the resonance frequency of the resonator coupled to the qubit under study (resonator_spectroscopy).
    - Having calibrated qubit pi pulse (x180) by running qubit, spectroscopy, rabi_chevron, power_rabi and updated the config.

Next steps before going to the next node:
    - Update the rotation angle (rotation_angle) in the configuration.
    - Update the g -> e threshold (ge_threshold) in the configuration.
"""

import qm.qua as qua
import qm as qm_api
from configuration import config, qop_ip, cluster_name, u, thermalization_time
from qualang_tools.analysis.discriminator import two_state_discriminator
from qualang_tools.results.data_handler import DataHandler
from qualang_tools.results import progress_counter, fetching_tool

data_handler = DataHandler(root_data_folder="./")

###################
# The QUA program #
###################

n_runs = 10_000  # Number of runs

iq_blobs_data = {
    "n_runs": n_runs,
    "config": config
}

with qua.program() as IQ_blobs:
    n = qua.declare(int)
    n_st = qua.declare_stream()
    I_g = qua.declare(qua.fixed)
    Q_g = qua.declare(qua.fixed)
    I_g_st = qua.declare_stream()
    Q_g_st = qua.declare_stream()
    I_e = qua.declare(qua.fixed)
    Q_e = qua.declare(qua.fixed)
    I_e_st = qua.declare_stream()
    Q_e_st = qua.declare_stream()

    with qua.for_(n, 0, n < n_runs, n + 1):
        qua.save(n, n_st)
        # Measure the state of the resonator
        qua.measure(
            "readout",
            "resonator",
            None,
            # qua.dual_demod.full("rotated_cos", "out1", "rotated_sin", "out2", I_g),
            # qua.dual_demod.full("rotated_minus_sin", "out1", "rotated_cos", "out2", Q_g),
            qua.dual_demod.full("opt_cos", "out1", "opt_sin", "out2", I_g),
            qua.dual_demod.full("opt_minus_sin", "out1", "opt_cos", "out2", Q_g),
        )
        # Wait for the qubit to decay to the ground state in the case of measurement induced transitions
        qua.wait(thermalization_time * u.ns, "resonator")
        # Save the 'I' & 'Q' quadratures to their respective streams for the ground state
        qua.save(I_g, I_g_st)
        qua.save(Q_g, Q_g_st)

        qua.align()  # global align
        # Play the x180 gate to put the qubit in the excited state
        qua.play("x180", "qubit")
        # Align the two elements to measure after playing the qubit pulse.
        qua.align("qubit", "resonator")
        # Measure the state of the resonator
        qua.measure(
            "readout",
            "resonator",
            None,
            # qua.dual_demod.full("rotated_cos", "out1", "rotated_sin", "out2", I_e),
            # qua.dual_demod.full("rotated_minus_sin", "out1", "rotated_cos", "out2", Q_e),
            qua.dual_demod.full("opt_cos", "out1", "opt_sin", "out2", I_e),
            qua.dual_demod.full("opt_minus_sin", "out1", "opt_cos", "out2", Q_e),
        )
        # Wait for the qubit to decay to the ground state
        qua.wait(thermalization_time * u.ns, "resonator")
        # Save the 'I' & 'Q' quadratures to their respective streams for the excited state
        qua.save(I_e, I_e_st)
        qua.save(Q_e, Q_e_st)

    with qua.stream_processing():
        n_st.save('iteration')
        # Save all streamed points for plotting the IQ blobs
        I_g_st.save_all("I_g")
        Q_g_st.save_all("Q_g")
        I_e_st.save_all("I_e")
        Q_e_st.save_all("Q_e")

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
    job = qmm.simulate(config, IQ_blobs, simulation_config)
    job.get_simulated_samples().con1.plot()

else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(IQ_blobs)

    results = fetching_tool(job, data_list=["iteration"], mode="live")

    while results.is_processing():
        # Fetch results
        iteration = results.fetch_all()
        # Progress bar
        elapsed_time = progress_counter(iteration[0], n_runs, start_time=results.get_start_time())

    # Creates a result handle to fetch data from the OPX
    res_handles = job.result_handles
    # Waits (blocks the Python console) until all results have been acquired
    res_handles.wait_for_all_values()
    # Fetch the 'I' & 'Q' points for the qubit in the ground and excited states
    Ig = res_handles.get("I_g").fetch_all()["value"]
    Qg = res_handles.get("Q_g").fetch_all()["value"]
    Ie = res_handles.get("I_e").fetch_all()["value"]
    Qe = res_handles.get("Q_e").fetch_all()["value"]
    # Plot the IQ blobs, rotate them to get the separation along the 'I' quadrature, estimate a threshold between them
    # for state discrimination and derive the fidelity matrix
    angle, threshold, fidelity, gg, ge, eg, ee = two_state_discriminator(Ig, Qg, Ie, Qe, b_print=True, b_plot=True)

    iq_blobs_data['Ig'] = Ig
    iq_blobs_data['Qg'] = Qg
    iq_blobs_data['Ie'] = Ie
    iq_blobs_data['Qe'] = Qe
    iq_blobs_data['elapsed_time'] = elapsed_time

    data_handler.save_data(data=iq_blobs_data, name="iq_blobs")

    qm.close()

# %%
