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
from qualang_tools.voltage_gates import VoltageGateSequence
from scipy import signal

from configuration_with_lffem import *
from macros import RF_reflectometry_macro

matplotlib.use('TkAgg')


###################
# The QUA program #
###################

sd = "Psd1"
sd_sticky = f"{sd}_sticky"
sd_constants = PLUNGER_SD_CONSTANTS[sd]
step_amp = sd_constants["step_amp"]
tank_circuits = ["tank_circuit1", "tank_circuit2"]
num_tank_circuits = len(tank_circuits)

n_avg = 100  # Number of averaging loops
offset_max = +0.2
offset_min = -offset_max
offset_step = 0.02
offsets = np.arange(offset_min, offset_max + offset_step, offset_step)
num_offsets = len(offsets)

save_data_dict = {
    "sensor_dot": sd,
    "tank_circuits": tank_circuits,
    "n_avg": n_avg,
    "offsets": offsets,
    "config": config,
}


with program() as charge_sensor_sweep:
    i = declare(fixed)  # QUA variable for the voltage sweep
    n = declare(int)  # QUA variable for the averaging loop
    n_st = declare_stream()  # Stream for the averaging iteration 'n'
    I = [declare(fixed) for _ in range(num_tank_circuits)]
    Q = [declare(fixed) for _ in range(num_tank_circuits)]
    I_st = [declare_stream() for _ in range(num_tank_circuits)]
    Q_st = [declare_stream() for _ in range(num_tank_circuits)]

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
            # Wait at each iteration in order to ensure that the data will not be transferred faster than 1 sample
            # per µs to the stream processing. Otherwise, the processor will receive the samples faster than it can
            # process them which can cause the OPX to crash.
            wait(1_000 * u.ns)  # in ns
        ramp_to_zero(sd_sticky)
        save(n, n_st)

    with stream_processing():
        n_st.save("iteration")
        for j, tc in enumerate(tank_circuits):
            I_st[j].buffer(len(offsets)).average().save(f"I_{tc}")
            Q_st[j].buffer(len(offsets)).average().save(f"Q_{tc}")


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(
    host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config
)

#######################
# Simulate or execute #
#######################
simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
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
    fetch_names = ["iteration"]
    for tc in tank_circuits:
        fetch_names.append(f"I_{tc}")
        fetch_names.append(f"Q_{tc}")
    results = fetching_tool(job, data_list=fetch_names, mode="live")
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    while results.is_processing():
        # Fetch results
        res = results.fetch_all()
        # Progress bar
        progress_counter(res[0], n_avg, start_time=results.get_start_time())

        plt.suptitle("Charge sensor gate sweep")
        for ind, tc in enumerate(tank_circuits):
            S = res[2 * ind + 1] + 1j * res[2 * ind + 2]
            R = np.abs(S)  # np.unwarp(np.angle(S))
            phase = signal.detrend(np.unwrap(np.angle(S)))

            # Plot results
            plt.suptitle("Charge sensor gate sweep")
            plt.subplot(2, 2, ind + 1)
            plt.cla()
            plt.plot(offsets, R)
            # plt.xlabel("Sensor gate voltage [V]")
            plt.ylabel(r"$R=\sqrt{I^2 + Q^2}$ [V]")
            plt.title(tc)
            plt.subplot(2, 2, ind + 3)
            plt.cla()
            plt.plot(offsets, phase)
            plt.xlabel("Sensor gate voltage [V]")
            plt.ylabel("Phase [rad]")

        plt.tight_layout()
        plt.pause(1)

    # Fetch results
    res = results.fetch_all()
    for ind, tc in enumerate(tank_circuits):
        save_data_dict[f"I_{tc}"] = res[2 * ind + 1]
        save_data_dict[f"Q_{tc}"] = res[2 * ind + 2]

    # Save results
    script_name = Path(__file__).name
    data_handler = DataHandler(root_data_folder=save_dir)
    save_data_dict.update({"fig_live": fig})
    data_handler.additional_files = {
        script_name: script_name,
        **default_additional_files,
    }
    data_handler.save_data(data=save_data_dict, name="05_sensor_gate_sweep_opx")

    qm.close()

# %%
