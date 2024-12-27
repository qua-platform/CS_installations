"""
        QUBIT SPECTROSCOPY
The goal of the script is to find the qubit transition by sweeping both the qubit pulse frequency and the magnetic field.
The QUA program is divided into three sections:
    1) step between the initialization point and the measurement point using sticky elements (long timescale).
    2) send the MW pulse to drive the EDSR transition (short timescale).
    3) measure the state of the qubit using either RF reflectometry or dc current sensing via PSB or Elzerman readout.
A compensation pulse can be added to the long timescale sequence in order to ensure 0 DC voltage on the fast line of
the bias-tee. Alternatively one can obtain the same result by changing the offset of the slow line of the bias-tee.

In the current implementation, the magnetic field and LO frequency are being swept using the API of the relevant
instruments in Python. For this reason the OPX program is paused at each iteration, the external parameters (B and f_LO)
are updated in Python and then the QUA program is resumed to sweep the qubit intermediate frequency and measure the
state of the dot.
Also note that the qubit pulse is played at the end of the "idle" level whose duration is fixed.

Note that providing a single magnetic field value will result in acquiring the 1D qubit spectroscopy at the specified
B-field.

Prerequisites:
    - Readout calibration (resonance frequency for RF reflectometry and sensor operating point for DC current sensing).
    - Setting the DC offsets of the external DC voltage source.
    - Connecting the OPX to the fast line of the plunger gates.
    - Having calibrated the initialization and readout point from the charge stability map and updated the configuration.

Before proceeding to the next node:
    - Identify the qubit frequency and update the configuration.
"""

import matplotlib.pyplot as plt
from qm import QuantumMachinesManager, SimulationConfig
from qm.qua import *
from qualang_tools.loops import from_array
from qualang_tools.plot import interrupt_on_close
from qualang_tools.results import (fetching_tool, progress_counter,
                                   wait_until_job_is_paused)
from qualang_tools.voltage_gates import VoltageGateSequence

from configuration_with_lffem import *
from macros import RF_reflectometry_macro

###################
# The QUA program #
###################

qubit = "qubit3"
n_avg = 100
# The frequency axis
frequencies = np.linspace(50 * u.MHz, 350 * u.MHz, 101)

# Delay in ns before stepping to the readout point after playing the qubit pulse - must be a multiple of 4ns and >= 16ns
delay_before_readout = 16

sweep_gates = ["P1_sticky", "P2_sticky"]
seq = VoltageGateSequence(config, sweep_gates)
seq.add_points("initialization", level_init, duration_init)
seq.add_points("readout", level_readout, duration_readout)
    

tank_circuits = ["tank_circuit1", "tank_circuit2"]
num_tank_circuits = len(tank_circuits)


save_data_dict = {
    "sweep_gates": sweep_gates,
    "tank_circuits": tank_circuits,
    "frequencies": frequencies,
    "n_avg": n_avg,
    "config": config,
}


with program() as qubit_spectroscopy_prog:
    n = declare(int)  # QUA integer used as an index for the averaging loop
    f = declare(int)  # QUA variable for the qubit pulse duration
    n_st = declare_stream()  # Stream for the iteration number (progress bar)
    I = [declare(fixed) for _ in range(num_tank_circuits)]
    Q = [declare(fixed) for _ in range(num_tank_circuits)]
    I_st = [declare_stream() for _ in range(num_tank_circuits)]
    Q_st = [declare_stream() for _ in range(num_tank_circuits)]

    with for_(n, 0, n < n_avg, n + 1):  # The averaging loop

        with for_(*from_array(f, frequencies)):  # Loop over the qubit pulse amplitude
            update_frequency(qubit, f)

            with strict_timing_():  # Ensure that the sequence will be played without gap
                # Navigate through the charge stability map
                seq.add_step(voltage_point_name="initialization")
                seq.add_step(voltage_point_name="readout")
                seq.add_compensation_pulse(duration=duration_compensation_pulse)

                # Drive the qubit by playing the MW pulse at the end of the manipulation step
                wait((duration_init - delay_before_readout - CONST_LEN) * u.ns, qubit)
                play("const", qubit)

                # Measure the dot right after the qubit manipulation
                wait(duration_init * u.ns, "tank_circuit")
                # Measure the dot right after the qubit manipulation
                for j, tc in enumerate(tank_circuits):
                    measure(
                        "readout",
                        tc,
                        None,
                        demod.full("cos", I[j], "out1"),
                        demod.full("sin", Q[j], "out1"),
                    )
                    save(I[j], I_st[j])
                    save(Q[j], Q_st[j])

            seq.ramp_to_zero()

        save(n, n_st)

    # Stream processing section used to process the data before saving it.
    with stream_processing():
        n_st.save("iteration")
        # RF reflectometry
        for j, tc in enumerate(tank_circuits):
            I_st[j].buffer(len(frequencies)).save_all(f"I_{tc}")
            Q_st[j].buffer(len(frequencies)).save_all(f"Q_{tc}")


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(
    host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config
)

###########################
# Run or Simulate Program #
###########################
simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, qubit_spectroscopy_prog, simulation_config)
    # Plot the simulated samples
    plt.figure()
    plt.subplot(211)
    job.get_simulated_samples().con1.plot()
    plt.axhline(level_init[0], color="k", linestyle="--")
    plt.axhline(level_readout[0], color="k", linestyle="--")
    plt.axhline(level_init[1], color="k", linestyle="--")
    plt.axhline(level_readout[1], color="k", linestyle="--")
    plt.yticks(
        [
            level_readout[1],
            level_init[1],
            0.0,
            level_init[0],
            level_readout[0],
        ],
        ["readout", "manip", "init", "0", "init", "manip", "readout"],
    )
    plt.legend("")
    from macros import get_filtered_voltage

    plt.subplot(212)
    get_filtered_voltage(
        job.get_simulated_samples().con1.analog["1"],
        1e-9,
        bias_tee_cut_off_frequency,
        True,
    )

else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(qubit_spectroscopy_prog)
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    for i in range(len(B_fields)):  # Loop over y-voltages
        # TODO Update the magnetic field
        for j in range(len(lo_frequencies)):
            # TODO update the lo frequency
            # Resume the QUA program (escape the 'pause' statement)
            job.resume()
            # Wait until the program reaches the 'pause' statement again, indicating that the QUA program is done
            wait_until_job_is_paused(job)
        if i == 0:
            # Get results from QUA program and initialize live plotting
            results = fetching_tool(
                job, data_list=["I", "Q", "dc_signal", "iteration"], mode="live"
            )
        # Fetch the data from the last OPX run corresponding to the current slow axis iteration
        I, Q, DC_signal, iteration = results.fetch_all()
        # Convert results into Volts
        S = u.demod2volts(I + 1j * Q, reflectometry_readout_length)
        R = np.abs(S)  # Amplitude
        phase = np.angle(S)  # Phase
        DC_signal = u.demod2volts(DC_signal, readout_len)
        # Progress bar
        progress_counter(iteration, len(B_fields))
        # Plot data
        if len(B_fields) > 1:
            plt.subplot(121)
            plt.cla()
            plt.title(r"$R=\sqrt{I^2 + Q^2}$ [V]")
            plt.pcolor(
                frequencies / u.MHz,
                B_fields[: iteration + 1],
                np.reshape(R, (iteration + 1, len(frequencies))),
            )
            plt.xlabel("Qubit pulse frequency [MHz]")
            plt.ylabel("B [mT]")
            plt.subplot(122)
            plt.cla()
            plt.title("Phase [rad]")
            plt.pcolor(
                frequencies / u.MHz,
                B_fields[: iteration + 1],
                np.reshape(phase, (iteration + 1, len(frequencies))),
            )
            plt.xlabel("Qubit pulse frequency [MHz]")
            plt.ylabel("B [mT]")
            plt.tight_layout()
            plt.pause(0.1)
        else:
            plt.suptitle(f"B = {B_fields[0]} mT")
            plt.subplot(121)
            plt.cla()
            plt.plot(frequencies / u.MHz, np.reshape(R, len(frequencies)))
            plt.xlabel("Qubit pulse frequency [MHz]")
            plt.ylabel(r"$R=\sqrt{I^2 + Q^2}$ [V]")
            plt.subplot(122)
            plt.cla()
            plt.plot(frequencies / u.MHz, np.reshape(phase, len(frequencies)))
            plt.xlabel("Qubit pulse frequency [MHz]")
            plt.ylabel("Phase [rad]")
            plt.tight_layout()
            plt.pause(0.1)
