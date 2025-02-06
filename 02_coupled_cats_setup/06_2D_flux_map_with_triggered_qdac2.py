from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from configuration import *
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.addons.variables import assign_variables_to_element
from external_drivers import QDACII, load_qdac_voltage_list
import matplotlib.pyplot as plt

###################
# The QUA program #
###################
n_avg = 100  # Number of averages
n_points_slow = 101  # Number of points for the slow axis
n_points_fast = 100  # Number of points for the fast axis
element = "ATS1"  # The element used for the readout

# Voltages in Volt
voltage_values_slow = np.linspace(-1.5, 1.5, n_points_slow)
voltage_values_fast = np.linspace(-1.5, 1.5, n_points_fast)

with program() as prog:
    n = declare(int)  # QUA integer used as an index for the averaging loop
    counter = declare(int)  # QUA integer used as an index for the Coulomb pulse
    i = declare(int)  # QUA integer used as an index to loop over the voltage points
    j = declare(int)  # QUA integer used as an index to loop over the voltage points
    n_st = declare_stream()  # Stream for the iteration number (progress bar)
    I = declare(fixed)
    Q = declare(fixed)
    I_st = declare_stream()
    Q_st = declare_stream()

    # Ensure that the result variables are assign to the pulse processor used for readout
    assign_variables_to_element(element, I, Q)

    with for_(n, 0, n < n_avg, n + 1):  # The averaging loop
        with for_(i, 0, i < n_points_slow, i + 1):
            # Trigger the QDAC2 channel to output the next voltage level from the list
            play("qdac_trigger", "QDAC_trigger1")
            with for_(j, 0, j < n_points_fast, j + 1):
                # Trigger the QDAC2 channel to output the next voltage level from the list
                play("qdac_trigger", "QDAC_trigger2")
                align("QDAC_trigger2", element)
                wait(200 * u.ns, element)  # Wait for the QDAC2 to settle
                measure(
                "readout",
                element,
                None,
                demod.full("cos", I),
                demod.full("sin", Q),
                )
                # Wait for the resonator to deplete
                wait(1000 * u.ns)
                # Save the 'I' & 'Q' quadratures to their respective streams
                save(I, I_st)
                save(Q, Q_st)
        save(n, n_st)

    # Stream processing section used to process the data before saving it.

    with stream_processing():
        n_st.save("iteration")
        I_st.buffer(n_points_fast).buffer(n_points_slow).average().save("I")
        Q_st.buffer(n_points_fast).buffer(n_points_slow).average().save("Q")


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name)

# ## QDAC2 section
# # Create the qdac instrument
# qdac = QDACII("Ethernet", IP_address="127.0.0.1", port=5025)  # Using Ethernet protocol
# # qdac = QDACII("USB", USB_device=4)  # Using USB protocol
# # Set up the qdac and load the voltage list
# load_qdac_voltage_list(
#     qdac,
#     channel=1,
#     dwell=2e-6,
#     slew_rate=2e7,
#     trigger_port="ext1",
#     output_range="low",
#     output_filter="med",
#     voltage_list=voltage_values_fast,
# )
# load_qdac_voltage_list(
#     qdac,
#     channel=2,
#     dwell=2e-6,
#     slew_rate=2e7,
#     trigger_port="ext2",
#     output_range="high",
#     output_filter="med",
#     voltage_list=voltage_values_slow,
# )

###########################
# Run or Simulate Program #
###########################
simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, prog, simulation_config)
    job.get_simulated_samples().con1.plot()
    plt.show()

else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(prog)
    # Get results from QUA program and initialize live plotting
    results = fetching_tool(job, data_list=["I", "Q", "iteration"], mode="live")
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    while results.is_processing():
        # Fetch the data from the last OPX run corresponding to the current slow axis iteration
        I, Q, iteration = results.fetch_all()
        # Convert results into Volts
        S = u.demod2volts(I + 1j * Q, readout_len, single_demod=True)
        R = np.abs(S)  # Amplitude
        phase = np.angle(S)  # Phase
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
