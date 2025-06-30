"""
Elzerman-Readout

Performs a voltage gate sequence which starts by emptying the spin from the quantum dot,
then loads a random spin-state onto the QD, (0,0)->(1,0), then finally pulses to
a voltage which is swept around the charge transition, measuring a time-trace of the
signal.

Purpose:
- Determine the plunger-gate voltage which sets the energy between spin-up and down.
- Visualize the average behaviour of spin-tunneling events.

Output:
- Time-trace as a function of voltage.

Prerequisites:
- Sets the plunger-gate QDAC voltage to the (0,0)->(1,0) charge transition
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
plunger_gate = "P1"

# Add the relevant voltage points describing the "slow" sequence (no qubit pulse)
level_empty = [-0.2]
level_load = [0.2]
level_read = [0.0]

duration_empty = 1000
duration_load = 1000
duration_read = 1000

seq = VoltageGateSequence(config, ["P1_sticky"])
seq.add_points("empty", level_empty, duration_empty)
seq.add_points("load", level_load, duration_load)
seq.add_points("read", level_read, duration_read)

level_reads = np.arange(-0.05, 0.05, 0.01)

simulate = True

with program() as prog:
    t = declare(int, value=16)
    a = declare(fixed, value=0.2)
    i = declare(int)
    with strict_timing_():
        seq.add_step(voltage_point_name="empty")
        seq.add_step(voltage_point_name="load", duration=t)
        seq.add_step(voltage_point_name="read")
        seq.add_compensation_pulse(duration=2_000)

        wait((duration_empty + duration_load) * u.ns, "source_tia_lock_in")
        measure_lock_in()

    seq.ramp_to_zero()

    align()
    play("x180", "qubit_1")


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
    job = qmm.simulate(config, prog, simulation_config)
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
    gate_barrier = qdac.get_channel_from_gate(right_plunger_gate)

    for surrounding_gate in surrounding_gates:
        qdac.set_to_turn_on_voltage(surrounding_gate)

    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(prog)
    # Live plotting
    fig, ax = plt.subplots(1, 1)
    ax = [ax]

    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure

    for i in range(len(read_level)):  # Loop over voltages
        for j in range(len(right_plunger_gate_dc_offsets)):
            # Set voltage
            gate_plunger.v(read_level[i])  # set the channel voltage
            gate_barrier.v(right_plunger_gate_dc_offsets[j])  # set the channel voltage
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
        progress_counter(iteration, len(read_level))

        # Plot results
        for k, (name, result) in enumerate(measurement_data.items()):
            axis_title = " ".join(name.split("_")[:-1]).capitalize() + f' [{name.split("_")[-1]}]'
            fig.suptitle(f"{plunger_gate}-{right_plunger_gate} Stability Map with PAT ({measurement_type.capitalize()})")
            ax[k].cla()
            map = ax[k].pcolormesh(right_plunger_gate_dc_offsets, read_level[: iteration + 1], result, cmap="seismic")
            ax[k].set_xlabel(f"{plunger_gate} Gate Voltage [V]")
            ax[k].set_ylabel(f"{right_plunger_gate} Gate Voltage [V]")
            cbar = plt.colorbar(map)
            cbar.set_label(axis_title)

            fig.tight_layout()
            plt.pause(1)

    data_handler = DataHandler(root_data_folder=save_dir)
    data = {
        **measurement_data,
        "plunger_gate": plunger_gate,
        "barrier_gate": right_plunger_gate,
        "left_plunger_gate_dc_offsets": read_level,
        "right_gate_dc_offsets": right_plunger_gate_dc_offsets,
        "figure": fig
    }
    # Save results
    data_folder = data_handler.save_data(data=data, name=f"{plunger_gate}_{right_plunger_gate}_stability_map_with_pat_{measurement_type}")

    qdac.close()

plt.show()
