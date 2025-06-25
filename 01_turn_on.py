"""
Turn-On Measurement via Gate Sweep

Sweeps a selected gate (source-drain, plunger, or barrier) using the QDAC to characterize turn-on behavior 
by measuring current or lock-in response through a trans-impedance amplifier.

Purpose:
- Identify the onset of conduction and tunneling regimes by observing current ramp-up or blockade.

Prerequisites:
- QDAC channel connected to the target gate.
- Trans-impedance amplifier connected to source input (e.g., S1 or S3).
- Gate-to-channel mapping and device config defined in `configuration.py`.

Outcome:
- Plots and saves the measured signal vs. gate voltage.
- Supports both direct current and lock-in detection modes.
"""


from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from qualang_tools.plot import interrupt_on_close
from qualang_tools.results import wait_until_job_is_paused, fetching_tool, progress_counter, DataHandler

from configuration import *
import matplotlib.pyplot as plt

from macros import measure_current, measure_lock_in, fetch_results_current, fetch_results_lock_in

###################
# The QUA program #
###################
n_avg = 100  # The number of averages
gate_dc_offsets = np.arange(0, 0.5, 0.05)
gate_to_sweep = "P20"
measurement_type = "lock-in"  # "current" or "lock-in"

simulate = False

with program() as turn_on_measurements_program:
    n = declare(int)  # QUA variable for the averaging loop
    i = declare(int)  # QUA variable for indexing the QDAC-I voltage step
    n_st = declare_stream()

    with for_(i, 0, i < len(gate_dc_offsets) + 1, i + 1):
        if not simulate:
            # Pause the OPX to update the external DC voltages in Python
            pause()
            # Wait for the voltages to settle (depends on the voltage source bandwidth)
            wait(settle_time)

        with for_(n, 0, n < n_avg, n + 1):  # QUA for_ loop for averaging
            if measurement_type == "current":
                i_source_st = measure_current()
            elif measurement_type == "lock-in":
                I_st, Q_st = measure_lock_in()

        save(i, n_st)

    with stream_processing():
        if measurement_type == "current":
            i_source_st.buffer(n_avg).map(FUNCTIONS.average()).save_all("i_source")
        elif measurement_type == "lock-in":
            I_st.buffer(n_avg).map(FUNCTIONS.average()).save_all("I")
            Q_st.buffer(n_avg).map(FUNCTIONS.average()).save_all("Q")

        n_st.save("iteration")


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=None)

#######################
# Simulate or execute #
#######################
if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=1_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, turn_on_measurements_program, simulation_config)
    # Get the simulated samples
    samples = job.get_simulated_samples()
    # Get the waveform report object
    waveform_report = job.get_simulated_waveform_report()
    # Cast the waveform report to a python dictionary
    waveform_dict = waveform_report.to_dict()
    # Visualize and save the waveform report
    waveform_report.create_plot(samples, plot=True, save_path=save_dir / "waveform_report.html")
else:
    # Initialize QDAC
    qdac = get_qdac()
    gate = qdac.get_channel_from_gate(gate_to_sweep)
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(turn_on_measurements_program)
    # Live plotting
    if measurement_type == "current":
        fig, ax = plt.subplots(1, 1)
        ax = [ax]
    else:
        fig, ax = plt.subplots(1, 2)

    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure

    for i in range(len(gate_dc_offsets)):  # Loop over voltages
        # Set voltage
        gate.v(gate_dc_offsets[i])  # set the channel voltage
        # Resume the QUA program (escape the 'pause' statement)
        job.resume()
        # Wait until the program reaches the 'pause' statement again, indicating that the QUA program is done
        wait_until_job_is_paused(job)

        if measurement_type == "current":
            measurement_data_list = ["i_source"]
        else:
            measurement_data_list = ["I", "Q"]

        if i == 0:
            # Get results from QUA program and initialize live plotting
            results = fetching_tool(job, data_list=measurement_data_list + ["iteration"], mode="live")

        # Fetch the data from the last OPX run corresponding to the current slow axis iteration
        iteration = results.fetch_all()[-1]
        if measurement_type == "current":
            measurement_data = fetch_results_current(results)
        else:
            measurement_data = fetch_results_lock_in(results)

        # Progress bar
        progress_counter(iteration, len(gate_dc_offsets))

        # Plot results
        for j, (name, result) in enumerate(measurement_data.items()):
            axis_title = " ".join(name.split("_")[:-1]).capitalize() + f' [{name.split("_")[-1]}]'
            fig.suptitle(f"{gate_to_sweep.capitalize()} Gate Sweep ({measurement_type.capitalize()})")
            ax[j].cla()
            ax[j].plot(gate_dc_offsets[: iteration + 1], result)
            ax[j].set_xlabel("Gate Voltage [V]")
            ax[j].set_ylabel(axis_title)
            plt.yscale('log')  # set the y-axis scaling to be logarithmic

        fig.tight_layout()
        plt.pause(1)

    data_handler = DataHandler(root_data_folder=save_dir)
    data = {
        **measurement_data,
        "swept_gate": gate_to_sweep,
        "gate_dc_offsets": gate_dc_offsets,
        "figure": fig
    }
    # Save results
    data_folder = data_handler.save_data(data=data, name=f"{gate_to_sweep}_turn_on_measurements")

    qdac.close()

plt.show()
