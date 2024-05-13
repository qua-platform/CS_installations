"""
        RABI CHEVRON (DURATION VS FREQUENCY)
This sequence involves executing the qubit pulse (such as x180, square_pi, or other types) and measuring the state
of the resonator across various qubit intermediate frequencies and pulse durations.
By analyzing the results, one can determine the qubit and estimate the x180 pulse duration for a specified amplitude.

Prerequisites:
    - Determination of the resonator's resonance frequency when coupled to the qubit of interest (referred to as "resonator_spectroscopy").
    - Calibration of the IQ mixer connected to the qubit drive line (be it an external mixer or an Octave port).
    - Identification of the approximate qubit frequency (referred to as "qubit_spectroscopy").
    - Configuration of the qubit frequency and the desired pi pulse amplitude (labeled as "pi_amp").
    - Set the desired flux bias

Before proceeding to the next node:
    - Adjust the qubit frequency setting, labeled as "f_01", in the state.
    - Modify the qubit pulse amplitude setting, labeled as "pi_len", in the state.
    - Save the current state by calling machine.save("quam")
"""

from qm.qua import *
from qm import SimulationConfig
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.loops import from_array
from qualang_tools.units import unit

import matplotlib.pyplot as plt
import numpy as np

from components import QuAM
from macros import qua_declaration, multiplexed_readout, node_save


###################################################
#  Load QuAM and open Communication with the QOP  #
###################################################
# Class containing tools to help handling units and conversions.
u = unit(coerce_to_integer=True)
# Instantiate the QuAM class from the state file
machine = QuAM.load("state.json")
# Generate the OPX and Octave configurations
config = machine.generate_config()
octave_config = machine.octave.get_octave_config()
# Open Communication with the QOP
qmm = machine.connect()

# Get the relevant QuAM components
q1 = machine.active_qubits[0]
q2 = machine.active_qubits[1]

###################
# The QUA program #
###################

operation = "x180"  # The qubit operation to play
n_avg = 100  # The number of averages

# The frequency sweep with respect to the qubits resonance frequencies
dfs = np.arange(-100e6, +100e6, 1e6)
# Pulse duration sweep (in clock cycles = 4ns) - must be larger than 4 clock cycles
durations = np.arange(4, 100, 2)

with program() as rabi_chevron:
    I, I_st, Q, Q_st, n, n_st = qua_declaration(nb_of_qubits=2)
    df = declare(int)  # QUA variable for the qubit detuning
    t = declare(int)  # QUA variable for the qubit pulse duration

    # Bring the active qubits to the minimum frequency point
    machine.apply_all_flux_to_min()

    with for_(n, 0, n < n_avg, n + 1):
        save(n, n_st)

        with for_(*from_array(df, dfs)):
            # Update the qubit frequencies
            update_frequency(q1.xy.name, df + q1.xy.intermediate_frequency)
            update_frequency(q2.xy.name, df + q2.xy.intermediate_frequency)

            with for_(*from_array(t, durations)):
                # Play the qubit drives
                q1.xy.play(operation, duration=t)
                q2.xy.play(operation, duration=t)
                # Align all elements to measure after playing the qubit pulse.
                align()
                # QUA macro the readout the state of the active resonators (defined in macros.py)
                multiplexed_readout(machine, I, I_st, Q, Q_st)
                # Wait for the qubit to decay to the ground state
                wait(machine.get_thermalization_time * u.ns)

    with stream_processing():
        n_st.save("n")
        # resonator 1
        I_st[0].buffer(len(durations)).buffer(len(dfs)).average().save("I1")
        Q_st[0].buffer(len(durations)).buffer(len(dfs)).average().save("Q1")
        # resonator 2
        I_st[1].buffer(len(durations)).buffer(len(dfs)).average().save("I2")
        Q_st[1].buffer(len(durations)).buffer(len(dfs)).average().save("Q2")


###########################
# Run or Simulate Program #
###########################
simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, rabi_chevron, simulation_config)
    job.get_simulated_samples().con1.plot()
else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Calibrate the active qubits
    # machine.calibrate_active_qubits(qm)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(rabi_chevron)
    # Get results from QUA program
    results = fetching_tool(job, ["n", "I1", "Q1", "I2", "Q2"], mode="live")
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  #  Interrupts the job when closing the figure
    while results.is_processing():
        # Fetch results
        n, I1, Q1, I2, Q2 = results.fetch_all()
        # Progress bar
        progress_counter(n, n_avg, start_time=results.start_time)
        # Convert results into Volts
        I1 = u.demod2volts(I1, q1.resonator.operations["readout"].length)
        Q1 = u.demod2volts(Q1, q1.resonator.operations["readout"].length)
        I2 = u.demod2volts(I2, q2.resonator.operations["readout"].length)
        Q2 = u.demod2volts(Q2, q2.resonator.operations["readout"].length)
        # Plot results
        plt.suptitle("Rabi chevron")
        plt.subplot(221)
        plt.cla()
        plt.pcolor(durations * 4, dfs / u.MHz, I1)
        plt.plot(q1.xy.operations[operation].length, 0, "r*")
        plt.xlabel("Qubit pulse duration [ns]")
        plt.ylabel("Qubit detuning [MHz]")
        plt.title(f"{q1.name} (f_01: {int(q1.f_01 / u.MHz)} MHz)")
        plt.subplot(223)
        plt.cla()
        plt.pcolor(durations * 4, dfs / u.MHz, Q1)
        plt.plot(q1.xy.operations[operation].length, 0, "r*")
        plt.xlabel("Qubit pulse duration [ns]")
        plt.ylabel("Qubit detuning [MHz]")
        plt.subplot(222)
        plt.cla()
        plt.pcolor(durations * 4, dfs / u.MHz, I2)
        plt.plot(q2.xy.operations[operation].length, 0, "r*")
        plt.title(f"{q2.name} (f_01: {int(q2.f_01 / u.MHz)} MHz)")
        plt.ylabel("Qubit detuning [MHz]")
        plt.xlabel("Qubit pulse duration [ns]")
        plt.subplot(224)
        plt.cla()
        plt.pcolor(durations * 4, dfs / u.MHz, Q2)
        plt.plot(q2.xy.operations[operation].length, 0, "r*")
        plt.xlabel("Qubit pulse duration [ns]")
        plt.ylabel("Qubit detuning [MHz]")
        plt.tight_layout()
        plt.pause(0.1)

    # Close the quantum machines at the end in order to put all flux biases to 0 so that the fridge doesn't heat-up
    qm.close()

    # Save data from the node
    data = {
        f"{q1.name}_duration": durations * 4,
        f"{q1.name}_frequency": dfs + q1.xy.intermediate_frequency,
        f"{q1.name}_I": np.abs(I1),
        f"{q1.name}_Q": np.angle(Q1),
        f"{q2.name}_duration": durations * 4,
        f"{q2.name}_frequency": dfs + q2.xy.intermediate_frequency,
        f"{q2.name}_I": np.abs(I2),
        f"{q2.name}_Q": np.angle(Q2),
        "figure": fig,
    }
    node_save("rabi_chevron_duration", data, machine)
