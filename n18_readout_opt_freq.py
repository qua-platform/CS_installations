# %%
"""
        READOUT OPTIMISATION: FREQUENCY
This sequence involves measuring the state of the resonator in two scenarios: first, after thermalization
(with the qubit in the |g> state) and then after applying a pi pulse to the qubit (transitioning the qubit to the
|e> state). This is done while varying the readout frequency.
The average I & Q quadratures for the qubit states |g> and |e>, along with their variances, are extracted to
determine the Signal-to-Noise Ratio (SNR). The readout frequency that yields the highest SNR is selected as the
optimal choice.

Prerequisites:
    - Having found the resonance frequency of the resonator coupled to the qubit under study (resonator_spectroscopy).
    - Having calibrated qubit pi pulse (x180) by running qubit, spectroscopy, rabi_chevron, power_rabi and updated the config.

Next steps before going to the next node:
    - Update the readout frequency (resonator_IF) in the configuration.
"""

import qm.qua as qua
import qm as qm_api
import numpy as np
from configuration import config, qop_ip, cluster_name, u, thermalization_time, resonator_IF
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
# The frequency sweep parameters
span = 1 * u.MHz
df = 50 * u.kHz
dfs = np.arange(-span, +span + 0.1, df)

ro_opt_freq_data = {
    "n_avg": n_avg,
    "dfs": dfs,
    "config": config
}

with qua.program() as ro_freq_opt:
    n = qua.declare(int)  # QUA variable for the averaging loop
    df = qua.declare(int)  # QUA variable for the readout frequency
    I_g = qua.declare(qua.fixed)  # QUA variable for the 'I' quadrature when the qubit is in |g>
    Q_g = qua.declare(qua.fixed)  # QUA variable for the 'Q' quadrature when the qubit is in |g>
    Ig_st = qua.declare_stream()
    Qg_st = qua.declare_stream()
    I_e = qua.declare(qua.fixed)  # QUA variable for the 'I' quadrature when the qubit is in |e>
    Q_e = qua.declare(qua.fixed)  # QUA variable for the 'Q' quadrature when the qubit is in |e>
    Ie_st = qua.declare_stream()
    Qe_st = qua.declare_stream()
    n_st = qua.declare_stream()

    with qua.for_(n, 0, n < n_avg, n + 1):
        with qua.for_(*from_array(df, dfs)):
            # Update the frequency of the digital oscillator linked to the resonator element
            qua.update_frequency("resonator", df + resonator_IF)
            # qua.measure the state of the resonator
            qua.measure(
                "readout",
                "resonator",
                None,
                qua.dual_demod.full("rotated_cos", "out1", "rotated_sin", "out2", I_g),
                qua.dual_demod.full("rotated_minus_sin", "out1", "rotated_cos", "out2", Q_g),
            )
            # qua.wait for the qubit to decay to the ground state
            qua.wait(thermalization_time * u.ns, "resonator")
            # Save the 'I_e' & 'Q_e' quadratures to their respective streams
            qua.save(I_g, Ig_st)
            qua.save(Q_g, Qg_st)

            qua.align()  # global align
            # Play the x180 gate to put the qubit in the excited state
            qua.play("x180", "qubit")
            # Align the two elements to qua.measure after playing the qubit pulse.
            qua.align("qubit", "resonator")
            # qua.measure the state of the resonator
            qua.measure(
                "readout",
                "resonator",
                None,
                qua.dual_demod.full("rotated_cos", "out1", "rotated_sin", "out2", I_e),
                qua.dual_demod.full("rotated_minus_sin", "out1", "rotated_cos", "out2", Q_e),
            )
            # qua.wait for the qubit to decay to the ground state
            qua.wait(thermalization_time * u.ns, "resonator")
            # Save the 'I_e' & 'Q_e' quadratures to their respective streams
            qua.save(I_e, Ie_st)
            qua.save(Q_e, Qe_st)
        # Save the averaging iteration to get the progress bar
        qua.save(n, n_st)

    with qua.stream_processing():
        n_st.save("iteration")
        # mean values
        Ig_st.buffer(len(dfs)).average().save("Ig_avg")
        Qg_st.buffer(len(dfs)).average().save("Qg_avg")
        Ie_st.buffer(len(dfs)).average().save("Ie_avg")
        Qe_st.buffer(len(dfs)).average().save("Qe_avg")
        # variances to get the SNR
        (
            ((Ig_st.buffer(len(dfs)) * Ig_st.buffer(len(dfs))).average())
            - (Ig_st.buffer(len(dfs)).average() * Ig_st.buffer(len(dfs)).average())
        ).save("Ig_var")
        (
            ((Qg_st.buffer(len(dfs)) * Qg_st.buffer(len(dfs))).average())
            - (Qg_st.buffer(len(dfs)).average() * Qg_st.buffer(len(dfs)).average())
        ).save("Qg_var")
        (
            ((Ie_st.buffer(len(dfs)) * Ie_st.buffer(len(dfs))).average())
            - (Ie_st.buffer(len(dfs)).average() * Ie_st.buffer(len(dfs)).average())
        ).save("Ie_var")
        (
            ((Qe_st.buffer(len(dfs)) * Qe_st.buffer(len(dfs))).average())
            - (Qe_st.buffer(len(dfs)).average() * Qe_st.buffer(len(dfs)).average())
        ).save("Qe_var")

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = qm_api.QuantumMachinesManager(host=qop_ip, cluster_name=cluster_name)

###########################
# Run or Simulate qua.program #
###########################
simulate = False

if simulate:
    # Simulates the QUA qua.program for the specified duration
    simulation_config = qm_api.SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, ro_freq_opt, simulation_config)
    job.get_simulated_samples().con1.plot()

else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA qua.program to the OPX, which compiles and executes it
    job = qm.execute(ro_freq_opt)  # execute QUA qua.program
    # Get results from QUA qua.program
    results = fetching_tool(
        job,
        data_list=["Ig_avg", "Qg_avg", "Ie_avg", "Qe_avg", "Ig_var", "Qg_var", "Ie_var", "Qe_var", "iteration"],
        mode="live",
    )
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    while results.is_processing():
        # Fetch results
        Ig_avg, Qg_avg, Ie_avg, Qe_avg, Ig_var, Qg_var, Ie_var, Qe_var, iteration = results.fetch_all()
        # Progress bar
        elapses_time = progress_counter(iteration, n_avg, start_time=results.get_start_time())
        # Derive the SNR
        Z = (Ie_avg - Ig_avg) + 1j * (Qe_avg - Qg_avg)
        var = (Ig_var + Qg_var + Ie_var + Qe_var) / 4
        SNR = ((np.abs(Z)) ** 2) / (2 * var)
        # Plot results
        plt.cla()
        plt.plot(dfs / u.MHz, SNR, ".-")
        plt.title(f"Readout frequency optimization around {resonator_IF / u.MHz} MHz")
        plt.xlabel("Readout frequency detuning [MHz]")
        plt.ylabel("SNR")
        plt.grid("on")
        plt.pause(1)

    print(f"The optimal readout frequency is {dfs[np.argmax(SNR)] + resonator_IF} Hz (SNR={max(SNR)})")

    ro_opt_freq_data['Ig_avg'] = Ig_avg
    ro_opt_freq_data['Qg_avg'] = Qg_avg
    ro_opt_freq_data['Ie_avg'] = Ie_avg
    ro_opt_freq_data['Qe_avg'] = Qe_avg
    ro_opt_freq_data['Ig_var'] = Ig_var
    ro_opt_freq_data['Qg_var'] = Qg_var
    ro_opt_freq_data['Ie_var'] = Ie_var
    ro_opt_freq_data['Qe_var'] = Qe_var

    data_handler.save_data(data=ro_opt_freq_data, name="ro_opt_freq")
# %%
