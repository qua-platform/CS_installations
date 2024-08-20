"""
GATE SWEEP (REFLECTOMETRY MEASUREMENT)

This script is designed to sweep the source-drain bias using the QDAC-II to
step the voltage of the source/plunger gate.

The reflectometry measurement is performed using a fast-line to an LC
circuit on the relevant gate. In this experiment, you should see a blockade
at low biases and a ramp at high biases.

Prerequisites:
- Connect the LC circuit between the bias-tee and the relevant gate.
- Connect the OPX analog output/input to the coupler before the bias-tee.

Note:
- Need to remove `pause` and `wait` to see simulation output.
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
n_points = 101
gate_dc_offsets = np.linspace(-0.5, 0.5, n_points)
gate_to_sweep = "source"  # or "plunger"
gate_to_measure = "source"  # or "plunger"

with program() as gate_sweep_reflectometry:
    n = declare(int)  # QUA variable for the averaging loop
    i = declare(int)  # QUA variable for indexing the QDAC-II voltage step
    I = declare(fixed)
    Q = declare(fixed)
    n_st = declare_stream()
    I_st = declare_stream()
    Q_st = declare_stream()

    with for_(i, 0, i < n_points + 1, i + 1):
        # Pause the OPX to update the external DC voltages in Python
        pause()
        # Wait for the voltages to settle (depends on the voltage source bandwidth)
        wait(1 * u.ms)

        with for_(n, 0, n < n_avg, n + 1):  # QUA for_ loop for averaging
            measure(
                "readout",
                f"{gate_to_measure}_resonator",
                None,
                demod.full("cos", I, "out1"),
                demod.full("sin", Q, "out1")
            )
            save(I, I_st)
            save(Q, Q_st)

        save(i, n_st)

    with stream_processing():
        I_st.buffer(n_avg).map(FUNCTIONS.average()).save_all("I")
        Q_st.buffer(n_avg).map(FUNCTIONS.average()).save_all("Q")
        n_st.save("iteration")


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=None)
qdac = QDAC2.QDac2('QDAC', visalib='@py', address=f'TCPIP::{qdac_ip}::5025::SOCKET')

if gate_to_sweep == "source":
    gate = qdac.channel(qdac_source_gate_ch)
elif gate_to_sweep == "plunger":
    gate = qdac.channel(qdac_right_plunger_ch)
else:
    raise ValueError(f'Expected gate to be "source" or "plunger", got {gate_to_sweep}')

#######################
# Simulate or execute #
#######################
simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, gate_sweep_reflectometry, simulation_config)
    # Plot the simulated samples
    job.get_simulated_samples().con1.plot()

else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(gate_sweep_reflectometry)
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    for i in range(n_points):  # Loop over voltages
        # Set voltage
        gate.output_mode(range='low')
        gate.dc_constant_V(gate_dc_offsets[i])
        # Resume the QUA program (escape the 'pause' statement)
        job.resume()
        # Wait until the program reaches the 'pause' statement again, indicating that the QUA program is done
        wait_until_job_is_paused(job)
        if i == 0:
            # Get results from QUA program and initialize live plotting
            results = fetching_tool(job, data_list=["I", "Q", "iteration"], mode="live")
    # Fetch the data from the last OPX run corresponding to the current slow axis iteration
    I, Q, iteration = results.fetch_all()
    # Convert results into Volts
    S = u.demod2volts(I + 1j * Q, rf_readout_length)
    R = np.abs(S)  # Amplitude
    phase = np.angle(S)  # Phase
    # Progress bar
    progress_counter(iteration, n_points)
    # Plot results
    plt.suptitle(f"{gate_to_sweep.capitalize()} Gate Sweep "
                 f"{gate_to_measure.capitalize()} Reflectometry")
    plt.subplot(211)
    plt.cla()
    plt.plot(gate_dc_offsets[: iteration + 1], R)
    plt.xlabel(f"{gate_to_sweep.capitalize()} Gate Voltage [V]")
    plt.ylabel(r"$R=\sqrt{I^2 + Q^2}$ [V]")
    plt.subplot(212)
    plt.cla()
    plt.plot(gate_dc_offsets[: iteration + 1], phase)
    plt.xlabel(f"{gate_to_sweep.capitalize()} Gate Voltage [V]")
    plt.ylabel("Phase [rad]")
    plt.tight_layout()
    plt.pause(0.1)

    data_handler = DataHandler(root_data_folder=data_folder_path)
    data = {
        "swept_gate": gate_to_sweep,
        "measured_gate": gate_to_measure,
        "gate_dc_offsets": gate_dc_offsets,
        "measured_amplitude": S,
        "measured_phase": R,
        "figure": fig
    }
    # Save results
    data_folder = data_handler.save_data(
        data=data,
        name=f"{gate_to_sweep}_gate_sweep_{gate_to_measure}_reflectometry"
    )

qdac.close()
plt.show()