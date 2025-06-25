"""
SET Coulomb Peak Measurement via Barrier Gate Sweep

Sweeps two SET barrier gates using the QDAC to measure current through the source and map diagonal Coulomb peaks.

Purpose:
- Reveal charge transitions as a function of tunnel barrier voltages.

Prerequisites:
- Calibrated turn-on voltages for AC0, B20, P20, B21, and AC3.
- Trans-impedance amplifier connected to the source gate.
- Gate mapping defined in `configuration.py`.

Outcome:
- 2D current map showing Coulomb blockade features, saved with figures and metadata.
"""


from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from qualang_tools.plot import interrupt_on_close
from qualang_tools.results import wait_until_job_is_paused, fetching_tool, progress_counter, DataHandler

from configuration import *
import matplotlib.pyplot as plt

from macros import measure_current, fetch_results_current

###################
# The QUA program #
###################
n_avg = 100  # The number of averages
barrier_gate_left = "B20"  # SET Barrier gate to be swept
barrier_gate_right = "B21"  # SET Barrier gate to be swept

# Surrounding voltage gates to be set to their turn-on voltage
surrounding_gates = ["AC0", "P20", "AC3"]

voltage_span = 0.3
voltage_step = 0.02

left_gate_dc_offsets = np.arange(
    qdac_turn_on_voltages[barrier_gate_left] - voltage_span / 2,
    qdac_turn_on_voltages[barrier_gate_left] + voltage_span / 2,
    voltage_step
)
right_gate_dc_offsets = np.arange(
    qdac_turn_on_voltages[barrier_gate_right] - voltage_span / 2,
    qdac_turn_on_voltages[barrier_gate_right] + voltage_span / 2,
    voltage_step
)

simulate = False

with program() as coulomb_peaks_program:
    n = declare(int)  # QUA variable for the averaging loop
    i = declare(int)  # QUA variable for indexing the left barrier gate voltage step
    j = declare(int)  # QUA variable for indexing the right barrier gate voltage step
    n_st = declare_stream()

    with for_(i, 0, i < len(left_gate_dc_offsets) + 1, i + 1):
        with for_(j, 0, j < len(right_gate_dc_offsets) + 1, j + 1):
            if not simulate:
                # Pause the OPX to update the external DC voltages in Python
                pause()
                # Wait for the voltages to settle (depends on the voltage source bandwidth)
                wait(settle_time)

            with for_(n, 0, n < n_avg, n + 1):  # QUA for_ loop for averaging
                i_source_st = measure_current()

            save(i, n_st)

    with stream_processing():
        i_source_st.buffer(n_avg).map(FUNCTIONS.average()).buffer(len(right_gate_dc_offsets)).save_all("i_source")

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
    job = qmm.simulate(config, coulomb_peaks_program, simulation_config)
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
    gate_left = qdac.get_channel_from_gate(barrier_gate_left)
    gate_right = qdac.get_channel_from_gate(barrier_gate_right)

    for surrounding_gate in surrounding_gates:
        qdac.set_to_turn_on_voltage(surrounding_gate)

    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(coulomb_peaks_program)
    # Live plotting
    fig, ax = plt.subplots(1, 1)
    ax = [ax]

    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure

    for i in range(len(left_gate_dc_offsets)):  # Loop over voltages
        for j in range(len(right_gate_dc_offsets)):
            # Set voltage
            gate_left.v(left_gate_dc_offsets[i])  # set the channel voltage
            gate_right.v(right_gate_dc_offsets[j])  # set the channel voltage
            # Resume the QUA program (escape the 'pause' statement)
            job.resume()
            # Wait until the program reaches the 'pause' statement again, indicating that the QUA program is done
            wait_until_job_is_paused(job)

            if i == 0:
                # Get results from QUA program and initialize live plotting
                results = fetching_tool(job, data_list=["i_source", "iteration"], mode="live")

            # Fetch the data from the last OPX run corresponding to the current slow axis iteration
            iteration = results.fetch_all()[-1]
            measurement_data = fetch_results_current(results)

        # Progress bar
        progress_counter(iteration, len(left_gate_dc_offsets))

        # Plot results
        for k, (name, result) in enumerate(measurement_data.items()):
            axis_title = " ".join(name.split("_")[:-1]).capitalize() + f' [{name.split("_")[-1]}]'
            fig.suptitle(f"{barrier_gate_left}-{barrier_gate_right} Gate Sweep (Current)")
            ax[k].cla()
            map = ax[k].pcolormesh(right_gate_dc_offsets, left_gate_dc_offsets[: iteration + 1], result)
            ax[k].set_xlabel(f"{barrier_gate_left} Gate Voltage [V]")
            ax[k].set_ylabel(f"{barrier_gate_right} Gate Voltage [V]")
            cbar = plt.colorbar(map)
            cbar.set_label(axis_title)

            fig.tight_layout()
            plt.pause(1)

    data_handler = DataHandler(root_data_folder=save_dir)
    data = {
        **measurement_data,
        "left_barrier_gate": barrier_gate_left,
        "right_barrier_gate": barrier_gate_right,
        "left_gate_dc_offsets": left_gate_dc_offsets,
        "right_gate_dc_offsets": right_gate_dc_offsets,
        "figure": fig
    }
    # Save results
    data_folder = data_handler.save_data(data=data, name=f"{barrier_gate_left}_{barrier_gate_right}_coulomb_peaks_current")

    qdac.close()

plt.show()
