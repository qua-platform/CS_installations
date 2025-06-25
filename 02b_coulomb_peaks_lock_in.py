"""
SET Coulomb Peak Measurement with Lock-in Readout

Sweeps the SET plunger gate using the QDAC and measures the demodulated lock-in signal across a range of readout frequencies.

Purpose:
- Resolve Coulomb peaks by monitoring the frequency-dependent response of the quantum dot.

Prerequisites:
- Calibrated turn-on voltages for AC0, B20, P20, B21, and AC3.
- Trans-impedance amplifier connected to the source gate.
- Lock-in readout path and configuration defined in `configuration.py`.

Outcome:
- 2D map of I/Q lock-in signal vs. gate voltage and readout frequency, saved with metadata and figures.
"""


from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from qualang_tools.plot import interrupt_on_close
from qualang_tools.results import wait_until_job_is_paused, fetching_tool, progress_counter, DataHandler
from qualang_tools.loops import from_array

from configuration import *
import matplotlib.pyplot as plt

from macros import measure_lock_in, fetch_results_lock_in

###################
# The QUA program #
###################
n_avg = 10  # The number of averages
set_gate = "P20"  # SET Plunger gate to be swept

# Surrounding voltage gates to be set to their turn-on voltage
surrounding_gates = ["AC0", "B20", "B21", "AC3"]

set_gate_voltage = qdac_turn_on_voltages[set_gate]
voltage_span = 0.3
voltage_step = 0.02
# Plunger gate voltage sweep
gate_dc_offsets = np.arange(
    set_gate_voltage - voltage_span / 2,
    set_gate_voltage + voltage_span / 2,
    voltage_step
)

# Lock-in readout frequencies
frequencies = np.arange(0, 1 * u.kHz, 50 * u.Hz)

simulate = False

with program() as turn_on_measurements_program:
    n = declare(int)  # QUA variable for the averaging loop
    i = declare(int)  # QUA variable for indexing the QDAC-I voltage step
    f = declare(int)  # QUA variable for sweeping the lock-in frequency
    n_st = declare_stream()

    with for_(i, 0, i < len(gate_dc_offsets) + 1, i + 1):
        if not simulate:
            # Pause the OPX to update the external DC voltages in Python
            pause()
            # Wait for the voltages to settle (depends on the voltage source bandwidth)
            wait(settle_time)

        with for_(*from_array(f, frequencies)):
            update_frequency("source_tia_lock_in", f)

            with for_(n, 0, n < n_avg, n + 1):  # QUA for_ loop for averaging
                I_st, Q_st = measure_lock_in()

        save(i, n_st)

    with stream_processing():
        I_st.buffer(n_avg).map(FUNCTIONS.average()).buffer(len(frequencies)).save_all("I")
        Q_st.buffer(n_avg).map(FUNCTIONS.average()).buffer(len(frequencies)).save_all("Q")

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
    gate = qdac.get_channel_from_gate(set_gate)

    for surrounding_gate in surrounding_gates:
        qdac.set_to_turn_on_voltage(surrounding_gate)

    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(turn_on_measurements_program)
    # Live plotting
    fig, ax = plt.subplots(1, 2)

    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure

    for i in range(len(gate_dc_offsets)):  # Loop over voltages
        # Set voltage
        # gate.v(gate_dc_offsets[i])  # set the channel voltage
        # Resume the QUA program (escape the 'pause' statement)
        job.resume()
        # Wait until the program reaches the 'pause' statement again, indicating that the QUA program is done
        wait_until_job_is_paused(job)

        if i == 0:
            # Get results from QUA program and initialize live plotting
            results = fetching_tool(job, data_list=["I", "Q", "iteration"], mode="live")

        # Fetch the data from the last OPX run corresponding to the current slow axis iteration
        iteration = results.fetch_all()[-1]
        measurement_data = fetch_results_lock_in(results)

        # Progress bar
        progress_counter(iteration, len(gate_dc_offsets))

        # Plot results
        for j, (name, result) in enumerate(measurement_data.items()):
            axis_title = " ".join(name.split("_")[:-1]).capitalize() + f' [{name.split("_")[-1]}]'
            fig.suptitle(f"{set_gate.capitalize()} Gate Sweep (Lock-in)")
            ax[j].cla()
            map = ax[j].pcolormesh(frequencies, gate_dc_offsets[: iteration + 1], result)
            ax[j].set_xlabel("Lock-in Frequency [Hz]")
            ax[j].set_ylabel("Gate Voltage [V]")
            if i == 0:
                cbar = plt.colorbar(map)
                cbar.set_label(axis_title)

        fig.tight_layout()
        plt.pause(1)

    data_handler = DataHandler(root_data_folder=save_dir)
    data = {
        **measurement_data,
        "swept_gate": set_gate,
        "gate_dc_offsets": gate_dc_offsets,
        "figure": fig
    }
    # Save results
    data_folder = data_handler.save_data(data=data, name=f"{set_gate}_coulomb_peaks_current")

    qdac.close()

plt.show()
