"""
        CHARGE STABILITY MAP - fast and slow axes: QDAC2 set to trigger mode
The goal of the script is to acquire the charge stability map.
Here two channels of the QDAC2 are parametrized to step though two preloaded voltage lists on the event of two digital
markers provided by the OPX (connected to ext1 and ext2). This method allows the fast acquisition of a 2D voltage map
and the data can be fetched from the OPX in real time to enable live plotting.
The speed can also be further improved by removing the live plotting and increasing the QDAC2 bandwidth.

The QUA program consists in sending the triggers to the QDAC2 to increment the voltages and measure the charge of the dot
either via dc current sensing or RF reflectometry.
On top of the DC voltage sweeps, the OPX can output a continuous square wave (Coulomb pulse) through the AC line of the
bias-tee. This allows to check the coupling of the fast line to the sample and measure the lever arms between the DC and
AC lines.

A global average is performed (averaging on the most outer loop) and the data is extracted while the program is running
to display the full charge stability map with increasing SNR.

Prerequisites:
    - Readout calibration (resonance frequency for RF reflectometry and sensor operating point for DC current sensing).
    - Setting the parameters of the QDAC2 and preloading the two voltages lists for the slow and fast axes.
    - Connect the two plunger gates (DC line of the bias-tee) to the QDAC2 and two digital markers from the OPX to the
      QDAC2 external trigger ports.
    - (optional) Connect the OPX to the fast line of the plunger gates for playing the Coulomb pulse and calibrate the
      lever arm.

Before proceeding to the next node:
    - Identify the different charge occupation regions.
    - Update the config with the lever-arms.
"""

from qm.qua import *
from qm.QuantumMachinesManager import QuantumMachinesManager
from qm import SimulationConfig
from configuration import *
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.addons.variables import assign_variables_to_element
import matplotlib.pyplot as plt
from macros import lock_in_macro

###################
# The QUA program #
###################
n_avg = 100  # Number of averages

n_points_slow = 101  # Number of points for the slow axis
n_points_fast = 100  # Number of points for the fast axis

# Voltages in Volt
voltage_values_slow = np.linspace(-1.5, 1.5, n_points_slow)
voltage_values_fast = np.linspace(-1.5, 1.5, n_points_fast)

with program() as charge_stability_prog:
    n = declare(int)  # QUA integer used as an index for the averaging loop
    i = declare(int)  # QUA integer used as an index to loop over the voltage points
    j = declare(int)  # QUA integer used as an index to loop over the voltage points
    n_st = declare_stream()  # Stream for the iteration number (progress bar)
    I = declare(fixed)
    I_st = declare_stream()
    Q = declare(fixed)
    Q_st = declare_stream()

    # Ensure that the result variables are assign to the pulse processor used for readout
    assign_variables_to_element("QDS", I, Q)

    align()

    with for_(n, 0, n < n_avg, n + 1):  # The averaging loop
        save(n, n_st)

        with for_(i, 0, i < n_points_slow, i + 1):
            # Trigger the QDAC2 channel to output the next voltage level from the list
            play("trigger", "qdac_trigger2")
            
            with for_(j, 0, j < n_points_fast, j + 1):
                # Trigger the QDAC2 channel to output the next voltage level from the list
                play("trigger", "qdac_trigger1")
                # Wait for the voltages to settle (depends on the channel bandwidth)
                wait(500 * u.us)

                align()

                lock_in_macro(I=I, Q=Q, I_st=I_st, Q_st=Q_st)

    # Stream processing section used to process the data before saving it.
    with stream_processing():
        n_st.save("iteration")
        # Cast the data into a 2D matrix and performs a global averaging of the received 2D matrices together.
        I_st.buffer(n_points_fast).buffer(n_points_slow).average().save("I")
        Q_st.buffer(n_points_fast).buffer(n_points_slow).average().save("Q")


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config)

## QDAC2 section
# Create the qdac instrument
qdac = QDACII("Ethernet", IP_address=qdac_ip, port=qdac_port)  # Using Ethernet protocol
# qdac = QDACII("USB", USB_device=4)  # Using USB protocol
# Set up the qdac and load the voltage list
load_voltage_list(
    qdac,
    channel=1,
    dwell=2e-6,
    slew_rate=2e7,
    trigger_port="ext1",
    output_range="low",
    output_filter="med",
    voltage_list=voltage_values_fast,
)
load_voltage_list(
    qdac,
    channel=2,
    dwell=2e-6,
    slew_rate=2e7,
    trigger_port="ext2",
    output_range="low",
    output_filter="med",
    voltage_list=voltage_values_slow,
)

###########################
# Run or Simulate Program #
###########################
simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, charge_stability_prog, simulation_config)
    job.get_simulated_samples().con1.plot()

else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(charge_stability_prog)
    # Get results from QUA program and initialize live plotting
    results = fetching_tool(job, data_list=["I", "Q", "iteration"], mode="live")
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure

    while results.is_processing():
        # Fetch the data from the last OPX run corresponding to the current slow axis iteration
        I, Q, iteration = results.fetch_all()
        # Convert results into Volts
        S = u.demod2volts(I + 1j * Q, lock_in_readout_length)
        R = np.abs(S)  # Amplitude
        phase = np.unwrap(np.angle(S))  # Phase
        # Progress bar
        progress_counter(iteration, n_points_slow, start_time=results.start_time)
        # Plot data
        plt.subplot(121)
        plt.cla()
        plt.title(r"$R=\sqrt{I^2 + Q^2}$ [V]")
        plt.pcolor(voltage_values_fast, voltage_values_slow, R)
        plt.xlabel("Fast voltage axis [V]")
        plt.ylabel("Slow voltage axis [V]")
        plt.subplot(122)
        plt.cla()
        plt.title("Phase [rad]")
        plt.pcolor(voltage_values_fast, voltage_values_slow, phase)
        plt.xlabel("Fast voltage axis [V]")
        plt.ylabel("Slow voltage axis [V]")
        plt.tight_layout()
        plt.pause(0.1)

    qm.close()