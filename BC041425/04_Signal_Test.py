"""
A script that mimics a pi/2 - pi pulse sequence but with arbitrary pulse duration.
Helps you check if signal is being generated from your setup
"""

from qm import SimulationConfig
from qm.qua import *
from qm import LoopbackInterface
from qm import QuantumMachinesManager
from configuration import *
import matplotlib.pyplot as plt
from macros import get_c2c_time
from qualang_tools.plot import interrupt_on_close
from qualang_tools.results import fetching_tool, progress_counter
##################
#   Parameters   #
##################
# Parameters Definition
pulse1_len = 400 // 4  # Pi/2 pulse
pulse2_len = pulse1_len * 2  # Pi pulse

cooldown_time = 10 * u.ms // 4  # Resonator or qubit relaxation time
safe_delay = 2 * u.us // 4  # Delay to safely avoid sending pulses during measurement windows

# Center to center time between first and second pulse
pulse_delay = safe_delay - (pulse1_len + pulse2_len) // 2
# Center to center time between the second pulse and the readout pulse
readout_delay = safe_delay - (pulse2_len + readout_len // 4) // 2

n_avg = 100

###################
# The QUA program #
###################
with program() as signal_test:
    n = declare(int)
    n_st = declare_stream()
    echo = declare_stream(adc_trace=True)

    with for_(n, 0, n < n_avg, n + 1):
        # initialization
        #play("cw", "TTL2")
        align()
        # we reset_phase the 'qubit' to be able to collect signals with 'readout_element'
        # with the same phase every run. Thus, when the analog traces are averaged they
        # do not wash out. Furthermore, because the control signal is associated with
        # 'qubit' and demodulated in 'readout_element', we reset the phase of the 'readout_element'
        # as well so that there is no random phase in the demodulation stage
        reset_phase("qubit")
        reset_phase("readout_element")
        reset_frame("qubit")

        # Play 1st pulse (pi/2)
        play("cw", "qubit", duration=pulse1_len)
        # we delay the switches because `duration` for digital pulses is faster than for analog
        # We use the simulator to make the adjustments and find `8`
        wait(8, "TTL1", "TTL2")
        play("signal_1", "TTL1", duration=pulse1_len)
        play("signal_2", "TTL2", duration=pulse1_len)
        # Wait some time corresponding to the echo time which also avoids sending pulses in the measurement window
        wait(pulse_delay, "qubit", "TTL1", "TTL2")

        # Play 2nd pulse (pi) along -X (phaseshift of pi) not sure why though...
        frame_rotation_2pi(-0.5, "qubit")
        play("signal_1", "TTL1", duration=pulse2_len)
        play("signal_2", "TTL2", duration=pulse2_len)
        play("cw", "qubit", duration=pulse2_len)

        align()  # global align
        # Wait the same amount of time as earlier in order to let the spin rephase after the echo
        wait(readout_delay, "readout_element")
        # Readout
        measure("readout", "readout_element", echo)

        save(n, n_st)

    with stream_processing():
        echo.input1().average().save("echo1")
        echo.input2().average().save("echo2")
        n_st.save("iteration")

################################
# Open quantum machine manager #
################################

qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name)

#######################
# Simulate or execute #
#######################

simulate = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulate_config = SimulationConfig(
        duration=2000,
        include_analog_waveforms=True,
        simulation_interface=LoopbackInterface(([("con1", 3, "con1", 1), ("con1", 4, "con1", 2)]), latency=180),
    )
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, signal_test, simulate_config)
    # Get the simulated samples
    samples = job.get_simulated_samples()
    # Plot the simulated samples
    samples.con1.plot()
    # Get the waveform report object
    waveform_report = job.get_simulated_waveform_report()
    # Cast the waveform report to a python dictionary
    waveform_dict = waveform_report.to_dict()
    # Visualize and save the waveform report
    waveform_report.create_plot(samples, plot=True, save_path=str(Path(__file__).resolve()))

    # The lines of code below allow you to retrieve information from the simulated waveform to assert
    # their position in time and manually estimate internal delays.
    # ver_t1: center-to-center time between first two pulses arriving to 'qubit'
    ver_t1 = get_c2c_time(job, ("qubit", 0), ("qubit", 2))
    print(
        f"center to center time between 1st and 2nd pulse is {ver_t1} --> internal delay to add: {ver_t1-4*safe_delay} ns"
    )
    # ver_t2: center-to-center time between the readout window to the second pulse arriving to 'qubit'
    ver_t2 = get_c2c_time(job, ("qubit", 2), ("qubit", 0))
    print(
        f"center to center time between 2nd pulse and readout is {ver_t2} --> internal delay to add: {ver_t2-4*safe_delay} ns"
    )

else:
    # Open quantum machine
    qm = qmm.open_qm(config)
    # Execute QUA program
    job = qm.execute(signal_test)
    # Fetch results
    res_handle = job.result_handles
    echo1_handle = res_handle.get("echo1")
    echo1_handle.wait_for_values(1)
    echo2_handle = res_handle.get("echo2")
    echo2_handle.wait_for_all_values(1)
    iteration_handle = res_handle.get("iteration")
    iteration_handle.wait_for_values(1)
    # results = fetching_tool(job, data_list=["echo1", "echo2", "iteration"], mode="live")

    # Plot results
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    while res_handle.is_processing():
        # echo1, echo2, iteration = results.fetch_all()
        echo1 = u.raw2volts(echo1_handle.fetch_all())
        echo2 = u.raw2volts(echo2_handle.fetch_all())
        iteration = iteration_handle.fetch_all()
        progress_counter(iteration, n_avg)

        plt.plot(echo1)
        plt.plot(echo2)
        plt.xlabel("Time [ns]")
        plt.ylabel("Signal amplitude [V]")
        plt.tight_layout()
        plt.pause(0.2)

    plt.cla()
    echo1 = u.raw2volts(echo1_handle.fetch_all())
    echo2 = u.raw2volts(echo2_handle.fetch_all())

    plt.plot(echo1)
    plt.plot(echo2)
    plt.xlabel("Time [ns]")
    plt.ylabel("Signal amplitude [V]")
    plt.tight_layout()