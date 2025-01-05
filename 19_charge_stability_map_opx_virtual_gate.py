# %%
"""
        CHARGE STABILITY MAP - fast axis: OPX (AC) & slow axis: external source (DC)
The goal of the script is to acquire the charge stability map.
Here the charge stability diagram is acquired by sweeping the fast axis with the OPX connected to the AC part of the
bias-tee, while the slow axis is handled by an external source connected to the DC part of the bias-tee.

This is done by pausing the QUA program, updating the voltages in Python using the instrument API and resuming the QUA program.
The OPX is simply measuring, either via dc current sensing or RF reflectometry, the charge occupation of the dot.

A single-point averaging is performed and the data is extracted while the program is running to display the results line-by-line.

Prerequisites:
    - Readout calibration (resonance frequency for RF reflectometry and sensor operating point for DC current sensing).
    - Setting the parameters of the external DC source using its driver.
    - Connect one plunger gate (DC line of the bias-tee) to the external dc source and the other plunger gate (AC line of the bias-tee) to tne OPX.

Before proceeding to the next node:
    - Identify the different charge occupation regions
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

, get_filtered_voltage

# matplotlib.use('TkAgg')


###################
# The QUA program #
###################

Px = "P1"
Py = "P2"
tank_circuits = ["tank_circuit1", "tank_circuit2"]
num_tank_circuits = len(tank_circuits)

n_avg = 3
n_voltages_Px = 51
n_voltages_Py = 101

# Voltages in Volt
voltages_Px = np.linspace(-0.1, 0.1, n_voltages_Px)
# Because of the bias-tee, it is important that the voltages swept along the fast axis are centered around 0.
# Also, since the OPX dynamic range is [-0.5, 0.5)V, one may need to add a voltage offset on the DC part of the bias-tee.
voltages_Py = np.linspace(-0.2, 0.2, n_voltages_Py)
# TODO: set DC offset on the external source for the fast gate
# One can check the expected voltage levels after the bias-tee using the following function:
_, _ = get_filtered_voltage(
    voltages_Py, step_duration=1e-6, bias_tee_cut_off_frequency=1e3, plot=True
)

save_data_dict = {
    "Px": Px,
    "Py": Py,
    "tank_circuits": tank_circuits,
    "n_avg": n_avg,
    "voltages_Px": voltages_Px,
    "voltages_Py": voltages_Py,
    "config": config,
}


with program() as charge_stability_prog:
    Vx = declare(fixed)
    Vy = declare(fixed)
    n = declare(int)  # QUA integer used as an index for the averaging loop
    n_st = declare_stream()  # Stream for the iteration number (progress bar)
    I = [declare(fixed) for _ in range(num_tank_circuits)]
    Q = [declare(fixed) for _ in range(num_tank_circuits)]
    I_st = [declare_stream() for _ in range(num_tank_circuits)]
    Q_st = [declare_stream() for _ in range(num_tank_circuits)]

    with for_(n, 0, n < n_avg, n + 1):  # The averaging loop
        with for_(*from_array(Vy, voltages_Py)):
            # Pause the OPX to update the external DC voltages in Python
            set_dc_offset(Py, "single", Vy)
            # Wait for the voltages to settle (depends on the voltage source bandwidth)
            wait(5 * u.ms)
            with for_(*from_array(Vx, voltages_Px)):
                # Update the dc offset of the specified element
                set_dc_offset(Px, "single", Vx)
                wait(1 * u.ms)
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
        # Save the LO iteration to get the progress bar
        save(n, n_st)

    # Stream processing section used to process the data before saving it
    with stream_processing():
        n_st.save("iteration")
        for j, tc in enumerate(tank_circuits):
            I_st[j].buffer(n_voltages_Px).buffer(n_voltages_Py).average().save(f"I_{tc}")
            Q_st[j].buffer(n_voltages_Px).buffer(n_voltages_Py).average().save(f"Q_{tc}")


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
    job = qmm.simulate(config, charge_stability_prog, simulation_config)
    plt.figure()
    job.get_simulated_samples().con1.plot()
    plt.show()

else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(charge_stability_prog)

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
            plt.suptitle("Charge stability diagram")
            plt.subplot(2, 2, ind + 1)
            plt.cla()
            plt.title(r"$\sqrt{I^2 + Q^2}$ [V]" + f" {tc}")
            plt.pcolor(voltages_Px, voltages_Py, R)
            # plt.xlabel(f"{Px} voltage [V]")
            plt.ylabel(f"{Py} voltage [V]")
            plt.subplot(2, 2, ind + 3)
            plt.cla()
            plt.title("Phase [rad]")
            plt.pcolor(voltages_Px, voltages_Py, phase)
            plt.xlabel(f"{Px} voltage [V]")
            plt.ylabel(f"{Py} voltage [V]")

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
    data_handler.save_data(data=save_data_dict, name=Path(__name__).stem)

# %%
