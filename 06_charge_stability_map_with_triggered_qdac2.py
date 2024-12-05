# %%
"""
        CHARGE STABILITY MAP - fast and slow axes: QDAC2 set to trigger mode
The goal of the script is to acquire the charge stability map.
Here two channels of the QDAC2 are parametrized to step though two preloaded voltage lists on the event of two digital
markers provided by the OPX (connected to ext1 and ext2). This method allows the fast acquisition of a 2D voltage map
and the data can be fetched from the OPX in real time to enable live plotting.
The speed can also be further improved by removing the live plotting and increasing the QDAC2 bandwidth.

The QUA program consists in sending the triggers to the QDAC2 to increment the voltages and measure the charge of the dot
AC lines.


A global average is performed (averaging on the most outer loop) and the data is extracted while the program is running
to display the full charge stability map with increasing SNR.

Prerequisites:
      QDAC2 external trigger ports.

    - (optional) Connect the OPX to the fast line of the plunger gates for playing the Coulomb pulse and calibrate the
      lever arm.

Before proceeding to the next node:
    - Identify the different charge occupation regions.
    - Update the config with the lever-arms.
"""

from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from configuration_with_lf_fem import *
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.addons.variables import assign_variables_to_element
from qdac2_driver import QDACII, load_voltage_list
import matplotlib.pyplot as plt
from HI_20241204_JunYoneda._macros import RF_reflectometry_macro, DC_current_sensing_macro

###################
# The QUA program #
###################
n_avg = 3  # Number of averages
n_points_slow = 11  # Number of points for the slow axis
n_points_fast = 10  # Number of points for the fast axis
Coulomb_amp = 0.0  # amplitude of the Coulomb pulse
# How many Coulomb pulse periods to last the whole program
N = (
    (int((reflectometry_readout_length + 1_000) / (2 * step_length)) + 1)
    * n_points_fast
    * n_points_slow
    * n_avg
)

# Voltages in Volt
voltage_values_slow = np.linspace(-1.5, 1.5, n_points_slow)
voltage_values_fast = np.linspace(-1.5, 1.5, n_points_fast)

with program() as charge_stability_prog:
    n = declare(int)  # QUA integer used as an index for the averaging loop
    counter = declare(int)  # QUA integer used as an index for the Coulomb pulse
    i = declare(int)  # QUA integer used as an index to loop over the voltage points
    j = declare(int)  # QUA integer used as an index to loop over the voltage points
    n_st = declare_stream()  # Stream for the iteration number (progress bar)
    I = declare(fixed)
    Q = declare(fixed)

    # Ensure that the result variables are assign to the pulse processor used for readout
    assign_variables_to_element("tank_circuit", I, Q)
    # Play the Coulomb pulse continuously for the whole sequence
    #      ____      ____      ____      ____
    #     |    |    |    |    |    |    |    |
    # ____|    |____|    |____|    |____|    |...
    with for_(counter, 0, counter < N, counter + 1):
        # The Coulomb pulse
        play("step" * amp(Coulomb_amp / P1_step_amp), "P1")
        play("step" * amp(-Coulomb_amp / P1_step_amp), "P1")

    with for_(n, 0, n < n_avg, n + 1):  # The averaging loop
        with for_(i, 0, i < n_points_slow, i + 1):
            # Trigger the QDAC2 channel to output the next voltage level from the list
            play("trigger", "qdac_trigger2")
            with for_(j, 0, j < n_points_fast, j + 1):
                # Trigger the QDAC2 channel to output the next voltage level from the list
                play("trigger", "qdac_trigger1")
                # Wait for the voltages to settle (depends on the channel bandwidth)
                wait(300 * u.us)
                # RF reflectometry: the voltage measured by the analog input 2 is recorded, demodulated at the readout
                # frequency and the integrated quadratures are stored in "I" and "Q"
                I, Q, I_st, Q_st = RF_reflectometry_macro(I=I, Q=Q)
                # Wait at each iteration in order to ensure that the data will not be transferred faster than 1 sample
                # per µs to the stream processing. Otherwise, the processor will receive the samples faster than it can
                # process them which can cause the OPX to crash.
                wait(1_000 * u.ns)  # in ns
        # Save the LO iteration to get the progress bar
        save(n, n_st)

    # Stream processing section used to process the data before saving it.
    with stream_processing():
        n_st.save("iteration")
        # Cast the data into a 2D matrix and performs a global averaging of the received 2D matrices together.
        # RF reflectometry
        I_st.buffer(n_points_fast).buffer(n_points_slow).average().save("I")
        Q_st.buffer(n_points_fast).buffer(n_points_slow).average().save("Q")


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(
    host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config
)

# ## QDAC2 section
# # Create the qdac instrument
# qdac = QDACII("Ethernet", IP_address="127.0.0.1", port=5025)  # Using Ethernet protocol
# # qdac = QDACII("USB", USB_device=4)  # Using USB protocol
# # Set up the qdac and load the voltage list
# load_voltage_list(
#     qdac,
#     channel=1,
#     dwell=2e-6,
#     slew_rate=2e7,
#     trigger_port="ext1",
#     output_range="low",
#     output_filter="med",
#     voltage_list=voltage_values_fast,
# )
# load_voltage_list(
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
save_data = True

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
        S = u.demod2volts(I + 1j * Q, reflectometry_readout_length)
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

    if save_data:
        from qualang_tools.results.data_handler import DataHandler

        # Data to save
        save_data_dict = {}
        # save_data_dict["elapsed_time"] =  np.array([elapsed_time])
        save_data_dict["I"] = I
        save_data_dict["Q"] = Q
        save_data_dict["S"] = S

        # Save results
        script_name = Path(__file__).name
        data_handler = DataHandler(root_data_folder=save_dir)
        save_data_dict.update({"fig_live": fig})
        data_handler.additional_files = {
            script_name: script_name,
            **default_additional_files,
        }
        data_handler.save_data(
            data=save_data_dict, name="charge_stability_map_with_triggered_qdac2"
        )

    plt.show()
    qm.close()

# %%
