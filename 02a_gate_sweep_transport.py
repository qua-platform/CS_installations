"""
GATE SWEEP (TRANSPORT MEASUREMENT)

This script is designed to sweep the source-drain or plunger gate bias using
the QDAC-II to step the voltage of the source/plunger gate.

The transport measurement is conducted through a drain_tia connected to the Drain
gate. In this experiment, you should see a blockade at low biases and a ramp at
high biases.

Prerequisites:
- Connect the QDAC-II DC channel to the appropriate device port.
- Connect the drain_tia to the corresponding input channel.

"""

from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from qualang_tools.plot import interrupt_on_close
from qualang_tools.results import wait_until_job_is_paused, fetching_tool, progress_counter, DataHandler
from qcodes_contrib_drivers.drivers.QDevil import QDAC2

from configuration import *
import matplotlib.pyplot as plt


###################
# The QUA program #
###################
n_avg = 100  # The number of averages
gate_dc_offsets = np.arange(-0.5, 0.5, 0.05)
gate_to_sweep = "source"  # or "plunger"
fixed_gate = "plunger" # or "source"

with program() as gate_sweep_transport:
    n = declare(int)  # QUA variable for the averaging loop
    i = declare(int)  # QUA variable for indexing the QDAC-II voltage step
    i_drain = declare(fixed)
    n_st = declare_stream()
    i_drain_st = declare_stream()  # The stream to store the raw ADC trace for the DC line

    with for_(i, 0, i < len(gate_dc_offsets) + 1, i + 1):
        # Pause the OPX to update the external DC voltages in Python
        pause()
        # Wait for the voltages to settle (depends on the voltage source bandwidth)
        wait(1 * u.ms)

        with for_(n, 0, n < n_avg, n + 1):  # QUA for_ loop for averaging
            measure("readout", "drain_tia", None, integration.full("constant", i_drain, "out1"))
            save(i_drain, i_drain_st)

        save(i, n_st)

    with stream_processing():
        i_drain_st.buffer(n_avg).map(FUNCTIONS.average()).save_all("i_drain")
        n_st.save("iteration")


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=None)
qdac = QDAC2.QDac2('QDAC', visalib='@py', address=f'TCPIP::{qdac_ip}::5025::SOCKET')

if gate_to_sweep == "source":
    gate = qdac.channel(qdac_source_gate_ch)
    fixed_gate_qdac = qdac.channel(qdac_right_plunger_ch)
elif gate_to_sweep == "plunger":
    gate = qdac.channel(qdac_right_plunger_ch)
    fixed_gate_qdac = qdac.channel(qdac_source_gate_ch)
else:
    raise ValueError(f'Expected gate to be "source" or "plunger", got {gate_to_sweep}')

valuet_to_set = 0.2

fixed_gate_qdac.dc_constant_V(valuet_to_set)

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
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    for i in range(len(gate_dc_offsets)):  # Loop over voltages
        # Set voltage
        gate.output_mode(range='low')
        gate.dc_constant_V(gate_dc_offsets[i])
        # gate._set_fixed_voltage_immediately(gate_dc_offsets[i])
        # Resume the QUA program (escape the 'pause' statement)
        job.resume()
        # Wait until the program reaches the 'pause' statement again, indicating that the QUA program is done
        wait_until_job_is_paused(job)
        if i == 0:
            # Get results from QUA program and initialize live plotting
            results = fetching_tool(job, data_list=["i_drain", "iteration"], mode="live")
        # Fetch the data from the last OPX run corresponding to the current slow axis iteration
        i_drain, iteration = results.fetch_all()
        i_drain = u.demod2volts(i_drain, readout_len)
        i_drain_A = i_drain * tia_iv_scale_factor
        # Progress bar
        progress_counter(iteration, len(gate_dc_offsets))
        # Plot results
        plt.suptitle(f"{gate_to_sweep.capitalize()}-Gate Sweep (Transport)")
        plt.cla()
        plt.plot(gate_dc_offsets[: iteration + 1], i_drain_A)
        plt.xlabel("Gate Voltage [V]")
        plt.ylabel(r"Drain Current [pA]")
        plt.yscale('log')  # set the y-axis scaling to be logarithmic
        plt.tight_layout()
        plt.pause(1)

    data_handler = DataHandler(root_data_folder=data_folder_path)
    data = {
        "value_to_set": valuet_to_set,
        "swept_gate": gate_to_sweep,
        "fixed_gate": fixed_gate,
        "gate_dc_offsets": gate_dc_offsets,
        "readout_drain_current": i_drain,
        "readout_drain_current_pA": i_drain_A,
        "figure": fig
    }
    # Save results
    data_folder = data_handler.save_data(data=data, name=f"{gate_to_sweep}_gate_sweep_transport")

qdac.close()
plt.show()