# %%
"""
        RESONATOR SPECTROSCOPY VERSUS FLUX
This sequence involves measuring the resonator by sending a readout pulse and demodulating the signals to
extract the 'I' and 'Q' quadratures. This is done across various readout intermediate dfs and flux biases.
The resonator frequency as a function of flux bias is then extracted and fitted so that the parameters can be stored in the configuration.

This information can then be used to adjust the readout frequency for the maximum and minimum frequency points.

Prerequisites:
    - Calibration of the time of flight, offsets, and gains (referenced as "time_of_flight").
    - Calibration of the IQ mixer connected to the readout line (be it an external mixer or an Octave port).
    - Identification of the resonator's resonance frequency (referred to as "resonator_spectroscopy").
    - Configuration of the readout pulse amplitude and duration.
    - Specification of the expected resonator depletion time in the state.

Before proceeding to the next node:
    - Adjust the flux bias to the minimum frequency point, labeled as "max_frequency_point", in the state.
    - Adjust the flux bias to the minimum frequency point, labeled as "min_frequency_point", in the state.
    - Save the current state by calling machine.save("quam")
"""

from pathlib import Path

from qm.qua import *
from qm import SimulationConfig
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.loops import from_array
from qualang_tools.units import unit
from quam_libs.components import QuAM
from quam_libs.macros import qua_declaration, multiplexed_readout, node_save

import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

import matplotlib

matplotlib.use("TKAgg")


###################################################
#  Load QuAM and open Communication with the QOP  #
###################################################
# Class containing tools to help handling units and conversions.
u = unit(coerce_to_integer=True)
# Instantiate the QuAM class from the state file
machine = QuAM.load()
# Generate the OPX and Octave configurations
config = machine.generate_config()
# Open Communication with the QOP
qmm = machine.connect()

# Get the relevant QuAM components
qubits = machine.active_qubits
resonators = [qubit.resonator for qubit in machine.active_qubits]
num_qubits = len(qubits)
num_resonators = len(resonators)


###################
# The QUA program #
###################

n_avg = 20  # Number of averaging loops
# Flux bias sweep in V
amps = np.linspace(-0.5, 0.5, 101)
# The frequency sweep around the resonator resonance frequency f_opt
dfs = np.arange(-5e6, 5e6, 0.1e6)

with program() as multi_res_spec_vs_flux:
    # Declare 'I' and 'Q' and the corresponding streams for the two resonators.
    # For instance, here 'I' is a python list containing two QUA fixed variables.
    I, I_st, Q, Q_st, n, n_st = qua_declaration(num_qubits=num_qubits)
    a = declare(fixed)  # QUA variable for the flux bias
    df = declare(int)  # QUA variable for the readout frequency

    # Bring the active qubits to the minimum frequency point
    machine.apply_all_flux_to_min()
    wait(25)

    with for_(n, 0, n < n_avg, n + 1):
        save(n, n_st)

        with for_(*from_array(a, amps)):

            with for_(*from_array(df, dfs)):

                for rr in resonators:
                    # Update the resonator frequencies for resonator
                    update_frequency(rr.name, df + rr.intermediate_frequency)
                
                align()
                
                for i, q in enumerate(qubits):
                    # play flux bias
                    # q.z.play("const", amplitude_scale=a, duration=q.resonator.operations["readout"].length * u.ns)
                    q.z.play("const", amplitude_scale=a)
                    align(q.z.name, q.resonator.name)
                    # readout the resonator
                    q.resonator.measure("readout", qua_vars=(I[i], Q[i]), amplitude_scale=a)

                    # save data
                    save(I[i], I_st[i])
                    save(Q[i], Q_st[i])

                # wait for the resonator to relax
                wait(machine.thermalization_time * u.ns)

    with stream_processing():
        n_st.save("n")
        for i in range(num_resonators):
            I_st[i].buffer(len(dfs)).buffer(len(amps)).average().save(f"I{i + 1}")
            Q_st[i].buffer(len(dfs)).buffer(len(amps)).average().save(f"Q{i + 1}")


#######################
# Simulate or execute #
#######################
simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, multi_res_spec_vs_flux, simulation_config)
    job.get_simulated_samples().con1.plot()
else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Calibrate the active qubits
    # machine.calibrate_octave_ports(qm)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(multi_res_spec_vs_flux)
    # Get results from QUA program
    data_list = ["n"] + sum(
        [[f"I{i + 1}", f"Q{i + 1}"] for i in range(num_resonators)], []
    )
    results = fetching_tool(job, data_list, mode="live")
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    while results.is_processing():
        # Fetch results
        fetched_data = results.fetch_all()
        n = fetched_data[0]
        I = fetched_data[1::2]
        Q = fetched_data[2::2]

        # Progress bar
        progress_counter(n, n_avg, start_time=results.start_time)

        plt.suptitle("Resonator spectroscopy vs flux")
        A_data = []
        for i, (qubit, rr) in enumerate(zip(qubits, resonators)):
            s = u.demod2volts(I[i] + 1j * Q[i], rr.operations["readout"].length)
            A = np.abs(s)
            A_data.append(A)
            # Plot
            plt.subplot(1, num_resonators, i + 1)
            plt.cla()
            plt.title(
                f"{rr.name} (LO: {rr.frequency_converter_up.LO_frequency / u.MHz} MHz)"
            )
            plt.xlabel("flux [V]")
            plt.ylabel(f"{rr.name} IF [MHz]")
            plt.pcolor(
                amps,
                (rr.LO_frequency + rr.intermediate_frequency) / u.MHz + dfs / u.MHz,
                A.T,
            )
            plt.plot(
                qubit.z.min_offset,
                (rr.LO_frequency + rr.intermediate_frequency) / u.MHz,
                "r*",
            )

        plt.tight_layout()
        plt.pause(0.1)

    plt.show()

    # Close the quantum machines at the end in order to put all flux biases to 0 so that the fridge doesn't heat up
    qm.close()

    # Update machine with min frequency point for both resonator and qubit
    # resonators[0].intermediate_frequency = 0
    # resonators[1].intermediate_frequency = 0
    # resonators[2].intermediate_frequency = 0
    # resonators[3].intermediate_frequency = 0
    # resonators[4].intermediate_frequency = 0
    # qubits[0].z.min_offset = 0.0
    # qubits[1].z.min_offset = 0.0
    # qubits[2].z.min_offset = 0.0
    # qubits[3].z.min_offset = 0.0
    # qubits[4].z.min_offset = 0.0

    # Save data from the node
    data = {}
    for i, (qubit, rr) in enumerate(zip(qubits, resonators)):
        data[f"{rr.name}_flux_bias"] = amps
        data[f"{rr.name}_frequency"] = qubit.resonator.intermediate_frequency + dfs
        data[f"{rr.name}_R"] = A_data[i]
        data[f"{rr.name}_min_offset"] = qubit.z.min_offset
    data["figure"] = fig
    node_save(machine, "resonator_spectroscopy_vs_flux", data, additional_files=True)

# %%
