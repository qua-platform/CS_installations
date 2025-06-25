"""
GATE SWEEP (TURN-ON MEASUREMENTS)

This script is designed to sweep the source-drain plunger or barrier gate bias using
the QDAC-I to step the voltage.

The transport measurement is conducted through a trans-impedance amplifier connected
to the source gate.

In this experiment, you should see a blockade at low biases and a ramp at
high biases.

Prerequisites:
- Connect the QDAC-I DC channel to the appropriate device port.
- Connect the source_tia to the corresponding input channel (S1 or S3)

"""

from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from qualang_tools.plot import interrupt_on_close
from qualang_tools.results import wait_until_job_is_paused, fetching_tool, progress_counter, DataHandler

from configuration import *
import matplotlib.pyplot as plt


###################
# The QUA program #
###################
n_avg = 100  # The number of averages
gate_dc_offsets = np.arange(-0.5, 0.5, 0.3)
# 'B20', 'P20', 'B21', 'B30', 'P30', 'B31', 'B1', 'P1', 'B2', 'P2', 'B3', 'S1', 'S2', 'S3', 'P3', 'B4', 'P4' or 'B5'
gate_to_sweep = "B20"

with program() as gate_sweep_transport:
    n = declare(int)  # QUA variable for the averaging loop
    i = declare(int)  # QUA variable for indexing the QDAC-II voltage step
    i_source = declare(fixed)
    n_st = declare_stream()
    i_source_st = declare_stream()  # The stream to store the raw ADC trace for the DC line

    with for_(i, 0, i < len(gate_dc_offsets) + 1, i + 1):
        # Pause the OPX to update the external DC voltages in Python
        pause()
        # Wait for the voltages to settle (depends on the voltage source bandwidth)
        wait(1 * u.ms)

        with for_(n, 0, n < n_avg, n + 1):  # QUA for_ loop for averaging
            measure("readout", "source_tia", None, integration.full("constant", i_source, "out1"))
            save(i_source, i_source_st)

        save(i, n_st)

    with stream_processing():
        i_source_st.buffer(n_avg).map(FUNCTIONS.average()).save_all("i_source")
        n_st.save("iteration")


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=None)

qdac = get_qdac()
gate = qdac.get_channel_from_gate(gate_to_sweep)

#######################
# Simulate or execute #
#######################
simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, gate_sweep_transport, simulation_config)
    # Plot the simulated samples
    job.get_simulated_samples().con1.plot()
else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(gate_sweep_transport)
    # Live plotting
    fig, ax = plt.subplots(1, 1)
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    for i in range(len(gate_dc_offsets)):  # Loop over voltages
        # Set voltage
        # todo: do we need to set the output mode?
        gate.v(gate_dc_offsets[i])  # set the channel voltage
        # Resume the QUA program (escape the 'pause' statement)
        job.resume()
        # Wait until the program reaches the 'pause' statement again, indicating that the QUA program is done
        wait_until_job_is_paused(job)
        if i == 0:
            # Get results from QUA program and initialize live plotting
            results = fetching_tool(job, data_list=["i_source", "iteration"], mode="live")
        # Fetch the data from the last OPX run corresponding to the current slow axis iteration
        i_source, iteration = results.fetch_all()
        i_source = u.demod2volts(i_source, readout_len)
        i_source_A = i_source * tia_iv_scale_factor
        # Progress bar
        progress_counter(iteration, len(gate_dc_offsets))
        # Plot results
        fig.suptitle(f"{gate_to_sweep.capitalize()}-Gate Sweep (Transport)")
        ax.cla()
        ax.plot(gate_dc_offsets[: iteration + 1], i_source_A)
        ax.set_xlabel("Gate Voltage [V]")
        ax.set_ylabel(r"Drain Current [pA]")
        plt.yscale('log')  # set the y-axis scaling to be logarithmic
        fig.tight_layout()
        plt.pause(1)

    data_handler = DataHandler(root_data_folder=save_dir)
    data = {
        "swept_gate": gate_to_sweep,
        "gate_dc_offsets": gate_dc_offsets,
        "readout_source_current": i_source,
        "readout_source_current_pA": i_source_A,
        "figure": fig
    }
    # Save results
    data_folder = data_handler.save_data(data=data, name=f"{gate_to_sweep}_turn_on_measurements")

qdac.close()
plt.show()
