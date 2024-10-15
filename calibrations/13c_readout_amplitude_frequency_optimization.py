# %%
"""
READOUT OPTIMIZATION: AMPLITUDE VS FREQUENCY
The sequence consists of measuring the state of the resonator after thermalization (qubits in |g>) and after
playing a pi pulse to the qubits (qubits in |e>) successively while sweeping the readout amplitude and frequency.
The 'I' & 'Q' quadratures when the qubits are in |g> and |e> are extracted to derive the readout fidelity.
The optimal readout amplitude is chosen to maximize the readout fidelity.

This version can be particularly useful when the resonator is driven in a regime where its frequency depends on the readout amplitude.

Prerequisites:
    - Having found the resonance frequency of the resonator coupled to the qubits under study (resonator_spectroscopy).
    - Having calibrated qubit pi pulse (x180) by running qubit, spectroscopy, rabi_chevron, power_rabi and updated the config.

Next steps before going to the next node:
    - Update the readout amplitude and frequency in the state.
    - Update the readout fidelity in the state.
    - Save the current state by calling machine.save("quam")
"""

from pathlib import Path

from qm.qua import *
from qm import SimulationConfig
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.loops import from_array
from qualang_tools.units import unit
from qualang_tools.analysis.discriminator import two_state_discriminator

from quam_libs.components import QuAM
from quam_libs.macros import qua_declaration, multiplexed_readout, node_save

import matplotlib.pyplot as plt
import numpy as np

import matplotlib

matplotlib.use("TKAgg")


###################################################
#  Load QuAM and open Communication with the QOP  #
###################################################
# Class containing tools to help handle units and conversions.
u = unit(coerce_to_integer=True)
# Instantiate the QuAM class from the state file
machine = QuAM.load()
# Generate the OPX and Octave configurations
config = machine.generate_config()
# Open Communication with the QOP
qmm = machine.connect()

# Get the relevant QuAM components
qubits = machine.active_qubits
num_qubits = len(qubits)

###################
# The QUA program #
###################
n_runs = 100  # The number of averages

# The readout amplitude sweep (as a pre-factor of the readout amplitude) - must be within [-2; 2)
amplitudes = np.linspace(0.5, 1.5, 51)
# The frequency sweep parameters with respect to the resonators' resonance frequencies
dfs = np.linspace(-5e6, 5e6, 51)

with program() as ro_amp_freq_opt:
    I_g, I_g_st, Q_g, Q_g_st, n, n_st = qua_declaration(num_qubits=num_qubits)
    I_e, I_e_st, Q_e, Q_e_st, _, _ = qua_declaration(num_qubits=num_qubits)
    a = declare(fixed)  # QUA variable for the readout amplitude
    df = declare(int)  # QUA variable for the readout frequency detuning
    counter = declare(int, value=0)  # Counter for the progress bar

    # Bring the active qubits to the minimum frequency point
    machine.apply_all_flux_to_min()

    with for_(*from_array(df, dfs)):
        save(counter, n_st)
        # Update the resonators' frequencies
        for qubit in qubits:
            update_frequency(
                qubit.resonator.name, df + qubit.resonator.intermediate_frequency
            )
        with for_(*from_array(a, amplitudes)):
            with for_(n, 0, n < n_runs, n + 1):
                # ground iq blobs for all qubits
                wait(machine.thermalization_time * u.ns)
                align()
                multiplexed_readout(qubits, I_g, I_g_st, Q_g, Q_g_st, amplitude=a)

                # excited iq blobs for all qubits
                align()
                # Wait for thermalization again in case of measurement-induced transitions
                wait(machine.thermalization_time * u.ns)
                for qubit in qubits:
                    qubit.xy.play("x180")
                align()
                multiplexed_readout(qubits, I_e, I_e_st, Q_e, Q_e_st, amplitude=a)
        # Save the counter to get the progress bar
        assign(counter, counter + 1)

    with stream_processing():
        # Save all streamed points for plotting the IQ blobs
        for i in range(num_qubits):
            I_g_st[i].buffer(n_runs).buffer(len(amplitudes)).buffer(len(dfs)).save(
                f"I_g_q{i}"
            )
            Q_g_st[i].buffer(n_runs).buffer(len(amplitudes)).buffer(len(dfs)).save(
                f"Q_g_q{i}"
            )
            I_e_st[i].buffer(n_runs).buffer(len(amplitudes)).buffer(len(dfs)).save(
                f"I_e_q{i}"
            )
            Q_e_st[i].buffer(n_runs).buffer(len(amplitudes)).buffer(len(dfs)).save(
                f"Q_e_q{i}"
            )
        n_st.save("n")


###########################
# Run or Simulate Program #
###########################
simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, ro_amp_freq_opt, simulation_config)
    job.get_simulated_samples().con1.plot()

else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Calibrate the active qubits
    # machine.calibrate_octave_ports(qm)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(ro_amp_freq_opt)
    # Get results from QUA program
    results = fetching_tool(job, data_list=["n"], mode="live")
    # Get progress counter to monitor runtime of the program
    while results.is_processing():
        # Fetch results
        iteration = results.fetch_all()
        # Progress bar
        progress_counter(iteration[0], len(dfs), start_time=results.get_start_time())

    # Fetch data
    data_list = sum(
        [
            [f"I_g_q{i}", f"Q_g_q{i}", f"I_e_q{i}", f"Q_e_q{i}"]
            for i in range(num_qubits)
        ],
        [],
    )
    results = fetching_tool(job, data_list)
    fetched_data = results.fetch_all()
    I_g_data = fetched_data[1::2]
    Q_g_data = fetched_data[2::2]
    I_e_data = fetched_data[3::2]
    Q_e_data = fetched_data[4::2]

    # Process the data
    fidelity_vec = [np.zeros((len(amplitudes), len(dfs))) for _ in range(num_qubits)]
    for j in range(len(dfs)):
        for i in range(len(amplitudes)):
            for k in range(num_qubits):
                _, _, fidelity, _, _, _, _ = two_state_discriminator(
                    I_g_data[k][j][i],
                    Q_g_data[k][j][i],
                    I_e_data[k][j][i],
                    Q_e_data[k][j][i],
                    b_print=False,
                    b_plot=False,
                )
                fidelity_vec[k][i][j] = fidelity

    # Plot the data
    fig, axes = plt.subplots(1, num_qubits, figsize=(15, 5))
    plt.suptitle("Readout amplitude optimization")
    for i, qubit in enumerate(qubits):
        ax = axes[i] if num_qubits > 1 else axes
        pcm = ax.pcolor(
            (dfs + qubit.resonator.intermediate_frequency) / u.MHz,
            amplitudes * qubit.resonator.operations["readout"].amplitude,
            fidelity_vec[i],
        )
        ax.set_title(f"{qubit.resonator.name}")
        fig.colorbar(pcm, ax)
        ax.set_ylabel("Readout amplitude [V]")
        ax.set_xlabel("Readout IF [MHz]")
    plt.tight_layout()

    # Update the state
    # for i, qubit in enumerate(qubits):
    #     qubit.resonator.operations["readout"].amplitude *= amplitudes[
    #         np.argmax(fidelity_vec[i]) // len(dfs)
    #     ]
    #     qubit.resonator.intermediate_frequency += dfs[
    #         np.argmax(fidelity_vec[i]) % len(dfs)
    #     ]
    #     qubit.resonator.readout_fidelity = np.max(fidelity_vec[i])

    # Close the quantum machines at the end to put all flux biases to 0 so that the fridge doesn't heat-up
    qm.close()

    # Save data from the node
    data = {"figure": fig}
    for i, qubit in enumerate(qubits):
        data[f"{qubit.resonator.name}_amplitude"] = (
            amplitudes * qubit.resonator.operations["readout"].amplitude
        )
        data[f"{qubit.resonator.name}_frequency"] = (
            dfs + qubit.resonator.intermediate_frequency
        )
        data[f"{qubit.resonator.name}_fidelity"] = fidelity_vec[i]
        data[f"{qubit.resonator.name}_amp_opt"] = qubit.resonator.operations[
            "readout"
        ].amplitude
        data[f"{qubit.resonator.name}_if_opt"] = qubit.resonator.intermediate_frequency

    node_save(machine, "readout_amplitude_frequency_optimization", data, additional_files=True)

# %%
