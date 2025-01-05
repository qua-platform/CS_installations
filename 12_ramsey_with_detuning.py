# %%
"""
        RAMSEY-LIKE CHEVRON - using standard QUA (pulse > 16ns and 4ns granularity)
The goal of the script is to acquire exchange driven coherent oscillations by sweeping the idle time and detuning.
The QUA program is divided into three sections:
    1) step between the initialization, idle and measurement points using sticky elements (long timescale).
    2) apply two delta-g driven pi-half pulses separated by a low detuning pulse to increase J, using non-sticky elements (short timescale).
    3) measure the state of the qubit using either RF reflectometry or dc current sensing via PSB or Elzerman readout.
A compensation pulse can be added to the long timescale sequence in order to ensure 0 DC voltage on the fast line of
the bias-tee. Alternatively one can obtain the same result by changing the offset of the slow line of the bias-tee.

In the current implementation, the qubit pulses are played using the real-time pulse manipulation of the OPX, which is
fast and can be arbitrarily long. However, the minimum pulse length is 16ns and the sweep step must be larger than 4ns.
Also note that the qubit pulses are played at the end of the global "idle" level whose duration is fixed.

Prerequisites:
    - Readout calibration (resonance frequency for RF reflectometry and sensor operating point for DC current sensing).
    - Setting the DC offsets of the external DC voltage source.
    - Connecting the OPX to the fast line of the plunger gates.
    - Having calibrated the initialization and readout point from the charge stability map and updated the configuration.
    - Having calibrated the delta-g driven pi-half parameters (detuning level and duration).

Before proceeding to the next node:
    - Extract the qubit frequency and T2*...
"""


import matplotlib.pyplot as plt
from qm import (CompilerOptionArguments, QuantumMachinesManager,
                SimulationConfig)
from qm.qua import *
from qualang_tools.addons.variables import assign_variables_to_element
from qualang_tools.loops import from_array
from qualang_tools.plot import interrupt_on_close
from qualang_tools.results import fetching_tool, progress_counter
from qualang_tools.results.data_handler import DataHandler
from qualang_tools.voltage_gates import VoltageGateSequence
from scipy import signal

from configuration_with_lffem import *
from macros_initialization_and_readout import *

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
# Pulse frequency sweep in Hz
detuning = 3 * u.MHz
detunings = [-detuning, +detuning]
intermediate_frequency = QUBIT_CONSTANTS[qubit]["IF"]


# duration_init includes the manipulation
delay_ops_start = 16
delay_ops_end = 16
duration_ops = delay_ops_start + 2 * PI_HALF_LEN + delay_ops_end
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
    "detunings": detunings,
    "durations": durations,
    "n_avg": n_avg,
    "config": config,
}


with program() as rabi_chevron:
    t = declare(int)  # QUA variable for the qubit pulse duration
    d = declare(int)
    df = declare(int)  # QUA variable for the qubit drive amplitude
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

        with for_(*from_array(df, detunings)):  # Loop over the qubit pulse amplitude
            update_frequency(qubit, intermediate_frequency + df)

            with for_(*from_array(t, durations)):  # Loop over the qubit pulse duration
                assign(d, tau_max - t)

                with strict_timing_():  # Ensure that the sequence will be played without gap


                    perform_initialization(I, Q, P, I_st, Q_st, P_st, kind=plungers)


                    # Navigate through the charge stability map
                    seq.add_step(voltage_point_name=f"operation_{plungers}", duration=duration_ops)
                    other_elements = get_other_elements(elements_in_use=[qubit] + sweep_gates, all_elements=all_elements)
                    wait(duration_ops >> 2, *other_elements)

                    # Drive the qubit by playing the MW pulse at the end of the manipulation step
                    wait(delay_ops_start * u.ns, qubit) if delay_ops_start >= 16 else None
                    wait(d >> 2, qubit)                    
                    # Play the 1st pi half pulse
                    play("x90_kaiser", qubit)
                    # Wait a varying idle time
                    wait(t >> 2, qubit)
                    # Play the 2nd pi half pulse
                    play("x90_kaiser", qubit)
                    wait(delay_ops_end * u.ns, qubit) if delay_ops_end >= 16 else None


                    perform_readout(I, Q, P, I_st, Q_st, P_st, kind=plungers)


                    seq.add_compensation_pulse(duration=duration_compensation_pulse)

                seq.ramp_to_zero()
                wait(1 * u.us)

    # Stream processing section used to process the dat[0, :]a before saving it.
    with stream_processing():
        n_st.save("iteration")
        for k in range(num_output_streams):
            I_st[k].buffer(len(durations)).buffer(len(detunings)).average().save(f"I{k + 1:d}")
            # Q_st[k].buffer(len(durations)).buffer(len(detunings)).average().save(f"Q{k + 1:d}")
            # P_st[k].boolean_to_int().buffer(len(durations)).buffer(len(detunings)).average().save(f"P{k + 1:d}")



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
    simulation_config = SimulationConfig(duration=1_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, rabi_chevron, simulation_config)
    # Plot the simulated samples
    plt.figure()
    job.get_simulated_samples().con1.plot()
    plt.show()
    # from macros import get_filtered_voltage
    # plt.figure()
    # get_filtered_voltage(
    #     job.get_simulated_samples().con1.analog["1"],
    #     1e-9,
    #     bias_tee_cut_off_frequency,
    #     True,
    # )

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
        iteration, I1, I2 = results.fetch_all()
        # Progress bar
        progress_counter(iteration, n_avg, start_time=results.get_start_time())
        # Plot results
        plt.suptitle(f"Rabi Chevron {tank_circuit}")
        # Plot results
        plt.subplot(2, 1, 1)
        plt.cla()
        plt.plot(durations, I1[0, :])
        plt.plot(durations, I1[1, :])
        plt.legend([f"detuning = {d / u.MHz} MHz"for d in detunings])
        plt.ylabel("I (init) [V]")
        plt.subplot(2, 1, 2)
        plt.cla()
        plt.plot(durations, I2[0, :])
        plt.plot(durations, I2[1, :])
        plt.xlabel("Idle duration [ns]")
        plt.ylabel("I (readout) [V]")
        plt.legend([f"detuning = {d / u.MHz} MHz"for d in detunings])
        plt.tight_layout()
        plt.pause(1)

    # Fetch results
    iteration, I1, I2 = results.fetch_all()
    save_data_dict["I1"] = I1
    save_data_dict["I2"] = I2


    # Fit the data
    try:
        from qualang_tools.plot.fitting import Fit
        fig_analyses = []
        for i, sgn in enumerate([-1, 1]):
            fit = Fit()
            fig_analyses[0] = plt.figure(figsize=(6,6))
            ramsey_fit = fit.ramsey(durations, I2[i, :], plot=True)
            qubit_T2 = np.abs(ramsey_fit["T2"][0])
            qubit_detuning = ramsey_fit["f"][0] * u.GHz - sgn * detuning
            plt.xlabell("Idle duration [ns]")
            plt.ylabel("I (readout) [V]")
            print(f"Qubit detuning to update in the config: qubit_IF += {-qubit_detuning:.0f} Hz")
            print(f"T2* = {qubit_T2:.0f} ns")
            plt.legend((f"detuning = {-qubit_detuning / u.kHz:.3f} kHz", f"T2* = {qubit_T2:.0f} ns"))
            plt.title(f"Ramsey measurement for {qubit}, {tank_circuit}")
            save_data_dict.update({f"fig_analysis{i}": fig_analyses[0]})
    except:
        pass
    finally:
        plt.show()


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
