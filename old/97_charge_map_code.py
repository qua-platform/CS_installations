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
    - Update the config with the lever-arms.pyvisa_py
"""

from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from configuration_with_opxplus import *
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.addons.variables import assign_variables_to_element
from qdac2_driver import QDACII, load_voltage_list
import matplotlib.pyplot as plt
from macros import RF_reflectometry_macro
import matplotlib

matplotlib.use('TkAgg')



###################
# The QUA program #
###################
n_avg = 1 # Number of averages
n_points_right = 1001  # Number of points for the slow axis
n_points_left = 1001  # Number of points for the fast axis
Coulomb_amp = 0.0  # amplitude of the Coulomb pulse
# How many Coulomb pulse periods to last the whole program
N = (
    (int((reflectometry_readout_length + 1_000) / (2 * step_length)) + 1)
    * n_points_left
    * n_points_right
    * n_avg
)

# Voltages in Volt
# voltage_values_right = np.linspace(0.05, 0.25, n_points_right)
# voltage_values_left = np.linspace(0.1, 0.3, n_points_left)

# voltage_values_right = np.linspace(0.2, 0.23, n_points_right)
# voltage_values_right = np.linspace(0.2, 0.21, n_points_right)
# voltage_values_right = np.linspace(0, 0.50, n_points_right)
voltage_values_right = np.linspace(0, 1.500, n_points_right)

# voltage_values_left = np.linspace(0.11, 0.14, n_points_left)
# voltage_values_left = np.linspace(0.115, 0.125, n_points_left)
# voltage_values_left = np.linspace(0, 0.50, n_points_left)
voltage_values_left = np.linspace(0, 1.500, n_points_left)

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
    # # Play the Coulomb pulse continuously for the whole sequence
    # #      ____      ____      ____      ____
    # #     |    |    |    |    |    |    |    |
    # # ____|    |____|    |____|    |____|    |...
    # with for_(counter, 0, counter < N, counter + 1):
    #     # The Coulomb pulse
    #     play("step" * amp(Coulomb_amp / P1_step_amp), "P1")
    #     play("step" * amp(-Coulomb_amp / P1_step_amp), "P1")

    # with for_(n, 0, n < n_avg, n + 1):  # The averaging loop
    #     with for_(i, 0, i < n_points_right, i + 1):
    #         # Trigger the QDAC2 channel to output the next voltage level from the list
    #         play("trigger", "qdac_trigger2")
    #         with for_(j, 0, j < n_points_left, j + 1):
    #             # Trigger the QDAC2 channel to output the next voltage level from the list
    #             play("trigger", "qdac_trigger1")
                
    #             with if_(j == 0):
    #                 wait(100 * u.ms)
    #             # Wait for the voltages to settle (depends on the channel bandwidth)
    #             wait(20 * u.ms)
    #             # RF reflectometry: the voltage measured by the analog input 2 is recorded, demodulated at the readout
    #             # frequency and the integrated quadratures are stored in "I" and "Q"
    #             I, Q, I_st, Q_st = RF_reflectometry_macro(I=I, Q=Q)
    #             # Wait at each iteration in order to ensure that the data will not be transferred faster than 1 sample
    #             # per µs to the stream processing. Otherwise, the processor will receive the samples faster than it can
    #             # process them which can cause the OPX to crash.
    #             # wait(1000 * u.ns)  # in ns
    #         # wait(10 * u.ms)  # in ns
    #     # Save the LO iteration to get the progress bar
    #     save(n, n_st)

    # 20241207
    # reflectometry_readout_long_length = 20 * u.ms
    with for_(n, 0, n < n_avg, n + 1):  # The averaging loop
        with for_(i, 0, i < n_points_right, i + 1):
            # Trigger the QDAC2 channel to output the next voltage level from the list
            play("trigger", "qdac_trigger2")
            
            with for_(j, 0, j < n_points_left, j + 1):
                # Trigger the QDAC2 channel to output the next voltage level from the list
                play("trigger", "qdac_trigger1")
                
                with if_(j == 0):
                    wait(100 * u.ms)
                # Wait for the voltages to settle (depends on the channel bandwidth)
                wait(1 * u.ms)
                # RF reflectometry: the voltage measured by the analog input 2 is recorded, demodulated at the readout
                # frequency and the integrated quadratures are stored in "I" and "Q"
                
                I, Q, I_st, Q_st = RF_reflectometry_macro(operation="long_readout", I=I, Q=Q)

                # Wait at each iteration in order to ensure that the data will not be transferred faster than 1 sample
                # per µs to the stream processing. Otherwise, the processor will receive the samples faster than it can
                # process them which can cause the OPX to crash.
                # wait(1000 * u.ns)  # in ns
            # wait(10 * u.ms)  # in ns
        # Save the LO iteration to get the progress bar
        save(n, n_st)


    # Stream processing section used to process the data before saving it.
    with stream_processing():
        n_st.save("iteration")
        # Cast the data into a 2D matrix and performs a global averaging of the received 2D matrices together.
        # RF reflectometry
        I_st.buffer(n_points_left).buffer(n_points_right).average().save("I")
        Q_st.buffer(n_points_left).buffer(n_points_right).average().save("Q")


# vol_center = np.linspace(0, 0.5, 11)
# vol_center = np.linspace(0.4, 1.0, 13)
vol_center = [0.22]
# vol_center = np.linspace(0.20, 0.28, 5)

# for vol_c in vol_center:
#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(
    host=qop_ip, port=qop_port, cluster_name=cluster_name
)

## QDAC2 section
# Create the qdac instrument
# qdac = QDACII("Ethernet", IP_address="127.0.0.1", port=5025)  # Using Ethernet protocol
import pyvisa
rm = pyvisa.ResourceManager('')
# qdac = rm.open_resource('ASRL7::INSTR')
# qdac = rm.open_resource('ASRL3::INSTR')
qdac = rm.open_resource('ASRL4::INSTR')

# qdac.flush()
# qdac = QDACII("USB", 'ASRL7::INSTR')  # Using USB protocol
# Set up the qdac and load the voltage list

# 15, 21, 24, 7, 19, 3, 1, 5, 2
# left QD
load_voltage_list(
    qdac,
    # channel=11,
    channel=13,
    dwell=2e-6,
    slew_rate=10,
    trigger_port="ext3",
    # trigger_port=None,
    output_range="High",
    output_filter="med",
    voltage_list=voltage_values_left,
    # voltage_list=[vol_c],
)
# right QD
load_voltage_list(
    qdac,
    # channel=8,
    channel=7,
    dwell=2e-6,
    slew_rate=10,
    trigger_port="ext4",
    # trigger_port=None,
    output_range="High",
    output_filter="med",
    voltage_list=voltage_values_right,
    # voltage_list=[vol_c],
)



# # set up other DC voltages
# load_voltage_list(
#     qdac,
#     channel=15,
#     dwell=2e-6,
#     slew_rate=10,
#     trigger_port=None,
#     output_range="High",
#     output_filter="med",
#     voltage_list=[3],
# )
# load_voltage_list(
#     qdac,
#     channel=21,
#     dwell=2e-6,
#     slew_rate=10,
#     trigger_port=None,
#     output_range="High",
#     output_filter="med",
#     voltage_list=[3],
# )
# load_voltage_list(
#     qdac,
#     channel=24,
#     dwell=2e-6,
#     slew_rate=10,
#     trigger_port=None,
#     output_range="High",
#     output_filter="med",
#     voltage_list=[3],
# )
# load_voltage_list(
#     qdac,
#     channel=7,
#     dwell=2e-6,
#     slew_rate=10,
#     trigger_port=None,
#     # trigger_port="ext1",
#     output_range="High",
#     output_filter="med",
#     voltage_list=[0.33],
#     # voltage_list=voltage_values_left,
# )

# # center barrier gate
# load_voltage_list(
#     qdac,
#     channel=3,
#     dwell=2e-6,
#     slew_rate=10,
#     trigger_port=None,
#     output_range="High",
#     output_filter="med",
#     voltage_list=[vol_c],
# )

# load_voltage_list(
#     qdac,
#     channel=5,
#     dwell=2e-6,
#     slew_rate=10,
#     trigger_port=None,
#     # trigger_port="ext2",
#     output_range="High",
#     output_filter="med",
#     voltage_list=[0.30],
#     # voltage_list=voltage_values_right,
# )
# load_voltage_list(
#     qdac,
#     channel=2,
#     dwell=2e-6,
#     slew_rate=10,
#     trigger_port=None,
#     output_range="High",
#     output_filter="med",
#     voltage_list=[3],
# )

###########################
# Run or Simulate Program #
###########################
simulate = False
save_data = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=100_000)  # In clock cycles = 4ns
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
    fig = plt.figure(figsize=(12, 6))
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    while results.is_processing():
        # Fetch the data from the last OPX run corresponding to the current slow axis iteration
        I, Q, iteration = results.fetch_all()
        # Convert results into Volts
        S = u.demod2volts(I + 1j * Q, reflectometry_readout_length)
        R = np.abs(S)  # Amplitude
        phase = np.angle(S)  # Phase
        # Progress bar
        progress_counter(iteration, n_avg, start_time=results.start_time)
        # Plot data
        plt.subplot(121)
        plt.cla()
        plt.title(r"$R=\sqrt{I^2 + Q^2}$ [V]")
        plt.pcolor(voltage_values_left, voltage_values_right, R)
        plt.xlabel("Fast voltage axis [V]")
        plt.ylabel("Slow voltage axis [V]")
        plt.colorbar()
        plt.subplot(122)
        plt.cla()
        plt.title("Phase [rad]")
        plt.pcolor(voltage_values_left, voltage_values_right, phase)
        plt.xlabel("Fast voltage axis [V]")
        plt.ylabel("Slow voltage axis [V]")
        plt.colorbar()
        plt.tight_layout()
        plt.pause(1)

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
            # data=save_data_dict, name=f'charge_stability_map_with_triggered_qdac2_{vol_c}'
        )

    # plt.show()
    qm.close()

# %%
