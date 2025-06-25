"""
Stability Map Measurement

Sweeps the qubit plunger and barrier gates with the QDAC-I while measuring source current 
to map charge occupation in the quantum dot.

Prerequisites:
- Calibrated turn-on voltages for B1, P1, B2, P2, and B3.
- Trans-impedance amplifier connected to the source gate.

Outcome:
- 2D current map revealing electron occupation lines on the plunger dot, saved with metadata.
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
plunger_gate = "P1"
barrier_gate = "B2"

# Surrounding voltage gates to be set to their turn-on voltage
surrounding_gates = ["B1", "P2", "B3"]

voltage_span = 0.3
voltage_step = 0.02

plunger_gate_dc_offsets = np.arange(
    qdac_turn_on_voltages[plunger_gate] - voltage_span / 2,
    qdac_turn_on_voltages[plunger_gate] + voltage_span / 2,
    voltage_step
)
barrier_gate_dc_offsets = np.arange(
    qdac_turn_on_voltages[barrier_gate] - voltage_span / 2,
    qdac_turn_on_voltages[barrier_gate] + voltage_span / 2,
    voltage_step
)

simulate = False

with program() as coulomb_peaks_program:
    n = declare(int)  # QUA variable for the averaging loop
    i = declare(int)  # QUA variable for indexing the left barrier gate voltage step
    j = declare(int)  # QUA variable for indexing the right barrier gate voltage step
    n_st = declare_stream()

    with for_(i, 0, i < len(plunger_gate_dc_offsets) + 1, i + 1):
        with for_(j, 0, j < len(barrier_gate_dc_offsets) + 1, j + 1):
            if not simulate:
                # Pause the OPX to update the external DC voltages in Python
                pause()
                # Wait for the voltages to settle (depends on the voltage source bandwidth)
                wait(settle_time)

            with for_(n, 0, n < n_avg, n + 1):  # QUA for_ loop for averaging
                i_source_st = measure_current()

            save(i, n_st)

    with stream_processing():
        i_source_st.buffer(n_avg).map(FUNCTIONS.average()).buffer(len(barrier_gate_dc_offsets)).save_all("i_source")

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
    gate_plunger = qdac.get_channel_from_gate(plunger_gate)
    gate_barrier = qdac.get_channel_from_gate(barrier_gate)

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

    for i in range(len(plunger_gate_dc_offsets)):  # Loop over voltages
        for j in range(len(barrier_gate_dc_offsets)):
            # Set voltage
            gate_plunger.v(plunger_gate_dc_offsets[i])  # set the channel voltage
            gate_barrier.v(barrier_gate_dc_offsets[j])  # set the channel voltage
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
        progress_counter(iteration, len(plunger_gate_dc_offsets))

        # Plot results
        for k, (name, result) in enumerate(measurement_data.items()):
            axis_title = " ".join(name.split("_")[:-1]).capitalize() + f' [{name.split("_")[-1]}]'
            fig.suptitle(f"{plunger_gate}-{barrier_gate} Gate Sweep (Current)")
            ax[k].cla()
            map = ax[k].pcolormesh(barrier_gate_dc_offsets, plunger_gate_dc_offsets[: iteration + 1], result)
            ax[k].set_xlabel(f"{plunger_gate} Gate Voltage [V]")
            ax[k].set_ylabel(f"{barrier_gate} Gate Voltage [V]")
            cbar = plt.colorbar(map)
            cbar.set_label(axis_title)

            fig.tight_layout()
            plt.pause(1)

    data_handler = DataHandler(root_data_folder=save_dir)
    data = {
        **measurement_data,
        "plunger_gate": plunger_gate,
        "barrier_gate": barrier_gate,
        "plunger_gate_dc_offsets": plunger_gate_dc_offsets,
        "barrier_gate_dc_offsets": barrier_gate_dc_offsets,
        "figure": fig
    }
    # Save results
    data_folder = data_handler.save_data(data=data, name=f"{plunger_gate}_{barrier_gate}_coulomb_peaks_current")

    # qdac.close()

plt.show()
