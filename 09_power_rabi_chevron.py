# %%
"""
        RABI CHEVRON - using standard QUA (pulse > 16ns and 4ns granularity)
The goal of the script is to acquire the Rabi oscillations by EDSR pulse frequency and duration.
The QUA program is divided into three sections:
    1) step between the initialization point and the measurement point using sticky elements (long timescale).
    2) send the MW pulse to drive the EDSR transition (short timescale).
    3) measure the state of the qubit using either RF reflectometry or dc current sensing via PSB or Elzerman readout.
A compensation pulse can be added to the long timescale sequence in order to ensure 0 DC voltage on the fast line of
the bias-tee. Alternatively one can obtain the same result by changing the offset of the slow line of the bias-tee.

In the current implementation, the qubit pulse is played using the real-time pulse manipulation of the OPX, which is fast
and can be arbitrarily long. However, the minimum pulse length is 16ns and the sweep step must be larger than 4ns.
Also note that the qubit pulses are played at the end of the "idle" level whose duration is fixed.

Prerequisites:
    - Readout calibration (resonance frequency for RF reflectometry and sensor operating point for DC current sensing).
    - Setting the DC offsets of the external DC voltage source.
    - Connecting the OPX to the fast line of the plunger gates.
    - Having calibrated the initialization and readout point from the charge stability map and updated the configuration.

Before proceeding to the next node:
    - Identify the pi and pi/2 pulse parameters, Rabi frequency...
"""

import matplotlib.pyplot as plt
from qm import CompilerOptionArguments, QuantumMachinesManager, SimulationConfig
from qm.qua import *
from qualang_tools.loops import from_array
from qualang_tools.plot import interrupt_on_close
from qualang_tools.results import fetching_tool, progress_counter
from qualang_tools.results.data_handler import DataHandler
from qualang_tools.addons.variables import assign_variables_to_element
from qualang_tools.voltage_gates import VoltageGateSequence
from scipy import signal

from configuration_with_lffem import *

###################
# The QUA program #
###################

qubit = "qubit3"
tank_circuit = "tank_circuit1"
measure_init = True
sweep_gates = ["P1_sticky", "P2_sticky"]

n_avg = 3
# Pulse duration sweep in ns - must be larger than 4 clock cycles
a_min = 0.05
a_max = 1.95
a_step = 0.05
amp_scalilngs = np.arange(a_min, a_max, a_step)
delay_before_readout = 16
qubit_delay = duration_init - delay_before_readout - PI_LEN
assert qubit_delay >= 16

# Pulse frequency sweep in Hz
frequencies = np.arange(0 * u.MHz, 100 * u.MHz, 100 * u.kHz)

# Add the relevant voltage points describing the "slow" sequence (no qubit pulse)
seq = VoltageGateSequence(config, sweep_gates)
seq.add_points("initialization", level_init, duration_init)
seq.add_points("readout", level_readout, duration_readout)


save_data_dict = {
    "sweep_gates": sweep_gates,
    "qubit": qubit,
    "tank_circuit": tank_circuit,
    "frequencies": frequencies,
    "amp_scalilngs": amp_scalilngs,
    "n_avg": n_avg,
    "config": config,
}


with program() as rabi_chevron:
    a = declare(fixed)  # QUA variable for the qubit pulse duration
    f = declare(int)  # QUA variable for the qubit drive amplitude
    n = declare(int)  # QUA integer used as an index for the averaging loop
    n_st = declare_stream()  # Stream for the iteration number (progress bar)

    I = declare(fixed)
    Q = declare(fixed)
    I_st = declare_stream()
    Q_st = declare_stream()

    assign_variables_to_element(tank_circuit, I, Q)

    with for_(n, 0, n < n_avg, n + 1):  # The averaging loop
        save(n, n_st)
        with for_(*from_array(f, frequencies)):  # Loop over the qubit pulse amplitude
            update_frequency(qubit, f)
            with for_(*from_array(a, amp_scalilngs)):  # Loop over the qubit pulse duration
                with strict_timing_():  # Ensure that the sequence will be played without gap
                    play("square_x180", qubit)
                    wait(PI_LEN * u.us, *sweep_gates)

                    # Navigate through the charge stability map
                    seq.add_step(voltage_point_name="initialization")  # includes manipulation
                    seq.add_step(voltage_point_name="readout")
                    seq.add_compensation_pulse(duration=duration_compensation_pulse)

                    # Drive the qubit by playing the MW pulse at the end of the manipulation step
                    # wait((duration_init - delay_before_readout) // 4 - (t >> 2) - 4, qubit)  # Need -4 cycles to compensate the gap
                    # wait(4, qubit)  # Need 4 additional cycles because of a gap
                    wait(qubit_delay * u.ns, qubit)
                    play("square_x180" * amp(a), qubit)

                    # Measure the dot right after the qubit manipulation
                    wait(duration_init * u.ns, tank_circuit)
                    # Measure the dot right after the qubit manipulation
                    measure("readout", tank_circuit, None, demod.full("cos", I, "out1"), demod.full("sin", Q, "out1"))
                    save(I, I_st)
                    save(Q, Q_st)

                seq.ramp_to_zero()
                wait(1 * u.us)

    # Stream processing section used to process the data before saving it.
    with stream_processing():
        n_st.save("iteration")
        # RF reflectometry
        I_st.buffer(len(amp_scalilngs)).buffer(len(frequencies)).average().save("I")
        Q_st.buffer(len(amp_scalilngs)).buffer(len(frequencies)).average().save("Q")


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
    job = qmm.simulate(config, rabi_chevron, simulation_config)
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
        ["readout", "init", "0", "init", "readout"],
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
    job = qm.execute(
        rabi_chevron,
        compiler_options=CompilerOptionArguments(flags=["not-strict-timing"]),
    )

    # Get results from QUA program
    fetch_names = ["iteration", "I", "Q"]
    results = fetching_tool(job, data_list=fetch_names, mode="live")
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    while results.is_processing():
        # Fetch results
        iterations, I, Q = results.fetch_all()
        # Progress bar
        progress_counter(iterations, n_avg, start_time=results.get_start_time())
        # Plot results
        plt.suptitle(f"Rabi Chevron {tank_circuit}")
        S = I + 1j * Q
        R = np.abs(S)  # np.unwarp(np.angle(S))
        phase = signal.detrend(np.unwrap(np.angle(S)))
        # Plot results
        plt.subplot(2, 1, 1)
        plt.cla()
        plt.title(r"$R=\sqrt{I^2 + Q^2}$ [V]")
        plt.pcolor(amp_scalilngs * PI_AMP, frequencies / u.MHz, R)
        plt.ylabel("Detuning [MHz]")
        plt.subplot(2, 1, 2)
        plt.cla()
        plt.title("Phase [rad]")
        plt.pcolor(amp_scalilngs * PI_AMP, frequencies / u.MHz, phase)
        plt.xlabel("Qubit pulse amplitude [V]")
        plt.ylabel("Detuning [MHz]")
        plt.tight_layout()
        plt.pause(1)

    # Fetch results
    _, I, Q = results.fetch_all()
    save_data_dict["I"] = I
    save_data_dict["Q"] = Q

    # Save results
    script_name = Path(__file__).name
    data_handler = DataHandler(root_data_folder=save_dir)
    save_data_dict.update({"fig_live": fig})
    data_handler.additional_files = {
        script_name: script_name,
        **default_additional_files,
    }
    data_handler.save_data(data=save_data_dict, name=Path(__name__).stem)

    qm.close()

# %%
