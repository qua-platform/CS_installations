from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from configuration import *
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.addons.variables import assign_variables_to_element
from external_drivers import set_dc_BILT
import matplotlib.pyplot as plt
from tqdm import tqdm  # Import tqdm for progress bar

###################
# The QUA program #
###################
n_avg = 100  # Number of averages
n_points_slow = 5  # Number of points for the slow axis
n_points_fast = 5  # Number of points for the fast axis
element = "ATS1"  # The element used for the readout

channel1 = 1  # The channel used for the slow axis
channel2 = 2  # The channel used for the fast axis

# Voltages in Volt
voltage_values_slow = np.linspace(-1.5, 1.5, n_points_slow).tolist()
voltage_values_fast = np.linspace(-1.5, 1.5, n_points_fast).tolist()

# Initialize the progress bar
total_iterations = n_points_slow * n_points_fast
progress_bar = tqdm(total=total_iterations, desc="Progress", unit="iteration")

with program() as prog:
    n = declare(int)  # QUA integer used as an index for the averaging loop
    counter = declare(int)  # QUA integer used as an index for the Coulomb pulse
    i = declare(fixed)  # QUA integer used as an index to loop over the voltage points
    j = declare(fixed)  # QUA integer used as an index to loop over the voltage points
    n_st = declare_stream()  # Stream for the iteration number (progress bar)
    I = declare(fixed)
    Q = declare(fixed)
    I_st = declare_stream()
    Q_st = declare_stream()

    # Ensure that the result variables are assign to the pulse processor used for readout
    assign_variables_to_element(element, I, Q)

    with for_each_(i, voltage_values_slow):
        # Set the DC voltage for the BILT channel
        set_dc_BILT(channel1, i, progress_bar)
        with for_each_(j, voltage_values_fast):
            # Trigger the QDAC2 channel to output the next voltage level from the list
            set_dc_BILT(channel2, j, progress_bar)
            with for_(n, 0, n < n_avg, n + 1):  # The averaging loop
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

    # Stream processing section used to process the data before saving it.

    with stream_processing():
        I_st.buffer(n_avg).map(FUNCTIONS.average()).buffer(n_points_fast).buffer(n_points_slow).save("I")
        Q_st.buffer(n_avg).map(FUNCTIONS.average()).buffer(n_points_fast).buffer(n_points_slow).save("Q")


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name)

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
    results = fetching_tool(job, data_list=["I", "Q"], mode="live")
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    while results.is_processing():
        # Fetch the data from the last OPX run corresponding to the current slow axis iteration
        I, Q = results.fetch_all()
        # Convert results into Volts
        S = u.demod2volts(I + 1j * Q, readout_len, single_demod=True)
        R = np.abs(S)  # Amplitude
        phase = np.angle(S)  # Phase
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
        plt.show()

progress_bar.close()  # Close the progress bar when done
