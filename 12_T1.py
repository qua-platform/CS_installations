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

from macros_initialization_and_readout import *
from configuration_with_lffem import *

###################
# The QUA program #
###################

qubit = "qubit1"
plungers = "P1-P2"
tank_circuit = "tank_circuit1"
do_feedback = False # False for test. True for actual.
full_read_init = False
num_output_streams = 6 if full_read_init else 2
do_simulate = True
all_elements = adjust_all_elements(removes=["qubit3", "qubit4", "qubit5"])


n_avg = 3
# Pulse duration sweep in ns - must be larger than 4 clock cycles
tau_min = 16
tau_max = 200
tau_step = 4
durations = np.arange(tau_min, tau_max, tau_step)


# duration_init includes the manipulation
delay_ops_start = 16
delay_ops_end = 16
duration_ops = delay_ops_start + tau_max + delay_ops_end
assert delay_ops_start == 0 or delay_ops_start >= 16
assert delay_ops_end == 0 or delay_ops_end >= 16


duration_compensation_pulse_ops = duration_ops
duration_compensation_pulse = int(0.7 * duration_compensation_pulse_full_initialization + duration_compensation_pulse_ops + duration_compensation_pulse_full_readout)
duration_compensation_pulse = 100 * (duration_compensation_pulse // 100)


seq.add_points("operation_P1-P2", level_ops["P1-P2"], duration_ops)
seq.add_points("operation_P4-P5", level_ops["P4-P5"], duration_ops)
seq.add_points("operation_P3", level_ops["P3"], duration_ops)


save_data_dict = {
    "sweep_gates": sweep_gates,
    "qubit": qubit,
    "plungers": plungers,
    "durations": durations,
    "n_avg": n_avg,
    "config": config,
}


with program() as rabi_chevron:
    t = declare(int)  # QUA variable for the qubit pulse duration
    d = declare(int)
    n = declare(int)  # QUA integer used as an index for the averaging loop
    n_st = declare_stream()  # Stream for the iteration number (progress bar)

    I = [declare(fixed) for _ in range(2)]  # QUA variable for the 'I' quadrature
    Q = [declare(fixed) for _ in range(2)]  # QUA variable for the 'Q' quadrature
    P = [declare(bool) for _ in range(2)]  # QUA variable for state discrimination
    I_st = [declare_stream() for _ in range(num_output_streams)]
    Q_st = [declare_stream() for _ in range(num_output_streams)]
    P_st = [declare_stream() for _ in range(num_output_streams)]

    assign_variables_to_element(tank_circuits[0], I[0], Q[0])
    assign_variables_to_element(tank_circuits[1], I[1], Q[1])

    with for_(n, 0, n < n_avg, n + 1):  # The averaging loop
        save(n, n_st)
        with for_(*from_array(t, durations)):  # Loop over the qubit pulse duration
            assign(d, tau_max - t)
 
            with strict_timing_():  # Ensure that the sequence will be played without gap

                if full_read_init:
                    # RI12 -> 2 x (R3 -> R12) -> RI45
                    perform_initialization(I, Q, P, I_st[0], I_st[1], I_st[2])
                else:
                    # RI12
                    read_init12(I[0], Q[0], P[0], None, I_st[0], do_save=[False, True])

                # Navigate through the charge stability map
                seq.add_step(voltage_point_name=f"operation_{plungers}", duration=duration_ops)
                other_elements = get_other_elements(elements_in_use=[qubit] + sweep_gates, all_elements=all_elements)
                wait(duration_ops >> 2, *other_elements)

                # Drive the qubit by playing the MW pulse at the end of the manipulation step
                wait(delay_ops_start * u.ns, qubit) if delay_ops_start >= 16 else None
                wait(d >> 2, qubit)
                play("x180_kaiser", qubit)
                wait(t >> 2, qubit)
                wait(delay_ops_end * u.ns, qubit) if delay_ops_end >= 16 else None

                if full_read_init:
                    # RI12 -> R3 -> RI45
                    perform_readout(I, Q, P, I_st[3], I_st[4], I_st[5])
                else:
                    # RI12
                    read_init12(I[0], Q[0], P[0], I_st[1], None, do_save=[True, False])

                seq.add_compensation_pulse(duration=duration_compensation_pulse)

            seq.ramp_to_zero()
            wait(1 * u.us)

    # Stream processing section used to process the data before saving it.
    with stream_processing():
        n_st.save("iteration")
        for k in range(num_output_streams):
            I_st[k].buffer(len(durations)).average().save(f"I{k + 1:d}")
            # Q_st[k].buffer(len(durations)).average().save(f"Q{k + 1:d}")
            # P_st[k].buffer(len(durations)).average().save(f"P{k + 1:d}")


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
    fetch_names = ["iteration"]
    fetch_names.extend([f"I{k + 1:d}" for k in range(num_output_streams)])
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
        plt.suptitle(f"T1 {tank_circuit}")
        # Plot results
        plt.subplot(2, 1, 1)
        plt.cla()
        plt.plot(durations, I)
        plt.ylabel("I [V]")
        plt.subplot(2, 1, 2)
        plt.cla()
        plt.plot(durations, Q)
        plt.xlabel("Idle duration [ns]")
        plt.ylabel("Q [V]")
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
