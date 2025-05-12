# %%
"""
        CHARGE SENSOR GATE SWEEP with the OPX
Here the voltage biasing the sensor gate is provided and being swept by the OPX connected to the DC line of the bias-tee.
A sticky element is used in order to maintain the voltage level and avoid fast voltage drops. Note that the OPX signal
can be combined with an external dc source to increase the dynamics.
The OPX is also measuring, either via dc current sensing or RF reflectometry, the response of the sensor dot.

A global average is performed (averaging on the most outer loop) and the data is extracted while the program is running
to display the full charge stability map with increasing SNR.
The script can also be easily modified to perform single point averaging instead.

Prerequisites:
    - Connect one the DC line of the bias-tee connected to the sensor dot to one OPX channel.
    - Setting the parameters of the external DC source using its driver if needed.

Before proceeding to the next node:
    - Update the config with the optimal sensing point.
"""

import matplotlib
import matplotlib.pyplot as plt
from qm import QuantumMachinesManager, SimulationConfig
from qm.qua import *
from qualang_tools.loops import from_array
from qualang_tools.plot import interrupt_on_close
from qualang_tools.results import fetching_tool, progress_counter
from qualang_tools.results.data_handler import DataHandler

from configuration_with_lffem_csrack import *
# from configuration_with_lffem import *
from macros_voltage_gate_sequence import VoltageGateSequence

# matplotlib.use('TkAgg')


###################
# The QUA program #
###################

sd_sticky = "Psd1_sticky"
tank_circuit = "tank_circuit1"
step_amp = PLUNGER_SD_CONSTANTS[sd_sticky.replace("_sticky", "")]["step_amp"]


###################
# Sweep Parameters
###################

run_live = False  # True
n_avg = 1000000 if run_live else 100  # Number of averaging loops
offset_max = +0.2
offset_min = -offset_max
offset_step = 0.005
offsets = np.arange(offset_min, offset_max + offset_step, offset_step)
duration_after_step = 1 * u.ms
num_offsets = len(offsets)

assert ((offsets / step_amp) < 2.0).all(), "offsets too high relative to step amp"

save_data_dict = {
    "sensor_dot": sd_sticky,
    "tank_circuit": tank_circuit,
    "n_avg": n_avg,
    "offsets": offsets,
    "config": config,
}


with program() as charge_sensor_sweep:
    i = declare(int)  # QUA variable for the voltage sweep
    n = declare(int)  # QUA variable for the averaging loop
    n_st = declare_stream()  # Stream for the averaging iteration 'n'

    I = declare(fixed)
    Q = declare(fixed)
    I_st = declare_stream()
    Q_st = declare_stream()

    with for_(n, 0, n < n_avg, n + 1):
        # Set the voltage to the 1st point of the sweep
        play("step" * amp(offset_min / step_amp), sd_sticky)
        # Wait for the voltage to settle (depends on the bias-tee cut-off frequency)
        wait(1 * u.ms, sd_sticky)

        with for_(i, 0, i < num_offsets, i + 1):
            # Play only from the second iteration

            with if_(i > 0):
                play("step" * amp(offset_step / step_amp), sd_sticky)
                # Wait for the voltage to settle (depends on the bias-tee cut-off frequency)
                wait(1 * u.ms, sd_sticky)

            align()
            # RF reflectometry: the voltage measured by the analog input 2 is recorded, demodulated at the readout
            # frequency and the integrated quadratures are stored in "I" and "Q"
            measure(
                "readout",
                tank_circuit,
                None,
                demod.full("cos", I, "out1"),
                demod.full("sin", Q, "out1"),
            )
            save(I, I_st)
            save(Q, Q_st)

            # Wait at each iteration in order to ensure that the data will not be transferred faster than 1 sample
            # per µs to the stream processing. Otherwise, the processor will receive the samples faster than it can
            # process them which can cause the OPX to crash.
            wait(1 * u.us)  # in ns

        ramp_to_zero(sd_sticky)
        save(n, n_st)

    with stream_processing():
        n_st.save("iteration")
        if run_live:
            I_st.buffer(len(offsets)).save("I")
            Q_st.buffer(len(offsets)).save("Q")
        else:
            I_st.buffer(len(offsets)).average().save("I")
            Q_st.buffer(len(offsets)).average().save("Q")


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, cluster_name=cluster_name)


#######################
# Simulate or execute #
#######################
simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=2_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, charge_sensor_sweep, simulation_config)
    # Plot the simulated samples
    job.get_simulated_samples().con1.plot()
    plt.show()

else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(charge_sensor_sweep)

    # Get results from QUA program
    fetch_names = ["iteration", "I", "Q"]
    results = fetching_tool(job, data_list=fetch_names, mode="live")
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    while results.is_processing():
        # Fetch results
        iteration, I, Q = results.fetch_all()
        # Progress bar
        progress_counter(iteration, n_avg, start_time=results.get_start_time())

        plt.suptitle(f"Charge sensor gate sweep on {tank_circuit}")
        plt.subplot(2, 1, 1)
        plt.cla()
        plt.plot(offsets, I)
        # plt.xlabel("Sensor gate voltage [V]")
        plt.ylabel("demod reflectometry signal I [V]")
        plt.subplot(2, 1, 2)
        plt.cla()
        plt.plot(offsets, Q)
        plt.xlabel("Sensor gate voltage [V]")
        plt.ylabel("demod reflectometry signal Q [V]")
        plt.tight_layout()
        plt.pause(0.5)

    # Fetch results
    iteration, I, Q = results.fetch_all()
    save_data_dict["I"] = I
    save_data_dict["Q"] = Q

    # Save results
    script_name = Path(__file__).name
    data_handler = DataHandler(root_data_folder=save_dir)
    save_data_dict.update({"fig_live": fig})
    data_handler.additional_files = {script_name: script_name, **default_additional_files}
    data_handler.save_data(data=save_data_dict, name=script_name.replace(".py", ""))

    qm.close()

# %%
