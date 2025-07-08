# %%
"""
        RF REFLECTOMETRY SPECTROSCOPY
The goal of this script is to perform the spectroscopy of the RF-reflectometry readout.
For this, the frequency of the element (pulser) used for reflectometry readout is being swept and the signal reflected
by the tank circuit is being acquired, demodulated and integrated by the OPX.

A global averaging is performed (averaging on the most outer loop) and the data is extracted while the program is running
to display the frequency response of the tank circuit with increasing SNR.

Prerequisites:
    - Connect the tank circuit to the corresponding output and input channels.

Before proceeding to the next node:
    - Update the config with the resonance frequency for reflectometry readout.
"""

from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from configuration_with_lf_fem import *

# from configuration_with_lf_fem import *
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.loops import from_array
import matplotlib.pyplot as plt
from scipy import signal
from qualang_tools.bakery import baking
import matplotlib

from qdac2_driver import load_voltage_list

matplotlib.use('TkAgg')


###################
# The QUA program #
###################
n_avg = 100  # number of averages
ramp_rate = 1e-8 # v/ns
ramp_duration = 50 * u.us  # ramp_rate * ramp_duration will be the voltage applied
flat_duration = 100 * u.us
# ramp_rate = 1e-7 # v/ns
# ramp_duration = 1 * u.us  # ramp_rate * ramp_duration will be the voltage applied
# flat_duration = 5 * u.us
# Set the sliced demod parameters
# division_length = 50  # Size of each demodulation slice in clock cycles -> 50 too short
division_length = 250 # 500*4=2us
number_of_divisions = int(
    (reflectometry_readout_long_length) / (4 * division_length)
)  # Number of slices
print("Integration weights chunk-size length in clock cycles:", division_length)
print(
    "The readout has been sliced in the following number of divisions",
    number_of_divisions,
)
# Time axis for the plots at the end
ts_plot = np.arange(
    division_length * 4, reflectometry_readout_long_length + 1, division_length * 4
)

wait_time_array = [16, 200] # [1, 200] # wait time has to be bigger than 16 ns = 4 clock cycles 
wait_time_in_cycle_array = [wt // 4 for wt in wait_time_array]
wait_time_array_number = np.size(wait_time_in_cycle_array)

with program() as PROG:
    n = declare(int)  # QUA variable for the averaging loop
    m = declare(int)  # QUA variable for the averaging loop
    wait_time_in_cycle = declare(int)
    I = declare(fixed, size=number_of_divisions)  # QUA variable for the measured 'I' quadrature
    Q = declare(fixed, size=number_of_divisions)  # QUA variable for the measured 'Q' quadrature
    # I = declare(fixed)  # QUA variable for the measured 'I' quadrature
    # Q = declare(fixed)  # QUA variable for the measured 'Q' quadrature
    n_st = declare_stream()  # Stream for the averaging iteration 'n'
    I_st = declare_stream()  # Stream for the 'I' quadrature
    Q_st = declare_stream()  # Stream for the 'Q' quadrature

    with for_(n, 0, n < n_avg, n + 1):
        with for_each_(wait_time_in_cycle, wait_time_in_cycle_array):
            wait(100 * u.us, "P1_sticky")
            play(ramp(-ramp_rate), "P1_sticky", duration=ramp_duration * u.ns)  # 1Vpp
            wait(flat_duration * u.ns, "P1_sticky")
            play(ramp(ramp_rate), "P1_sticky", duration=ramp_duration * u.ns)  # 1Vpp
            # wait(flat_duration, "P1_sticky")
            # play(ramp(-ramp_rate), "P1_sticky", duration=ramp_duration)  # 1Vpp

            # RF reflectometry: the voltage measured by the analog input 2 is recorded, demodulated at the readout
            # Please choose the right "out1" or "out2" according to the connectivity
            
            wait(wait_time_in_cycle, "tank_circuit") 
            # wait(49 * u.ms, "tank_circuit")
            measure(
                "long_readout",
                "tank_circuit",
                None,
                demod.sliced("cos", I, division_length, "out1"),
                demod.sliced("sin", Q, division_length, "out1"),
            )
            with for_(m, 0, m < number_of_divisions, m + 1):
                save(I[m], I_st)
                save(Q[m], Q_st)
            # Wait at each iteration in order to ensure that the data will not be transferred faster than 1 sample
            # per µs to the stream processing. Otherwise, the processor will receive the samples faster than it can
            # process them which can cause the OPX to crash.
            wait(1_000 * u.ns)  # in ns
            save(n, n_st)

    with stream_processing():
        n_st.save("iteration")
        # I_st.buffer(number_of_divisions).average().save("I")
        # Q_st.buffer(number_of_divisions).average().save("Q")
        I_st.buffer(number_of_divisions).buffer(wait_time_array_number).average().save("I")
        Q_st.buffer(number_of_divisions).buffer(wait_time_array_number).average().save("Q")

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(
    host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config
)
qmm.close_all_qms()
qmm.clear_all_job_results()
# import pyvisa
# rm = pyvisa.ResourceManager('')
# qdac = rm.open_resource('ASRL7::INSTR')

# # set up other DC voltages
# channel_voltage_pairs = [
#     (15, 3),
#     (21, 3),
#     (24, 3),
#     (7, 0.45), #barrier
#     (19, 0.12),
#     (3, 0.38), #center 
#     (1, 0.2),
#     (5, 0.35), #barrier
#     (2, 3),
# ]
# for ch, vlt in channel_voltage_pairs:
#     load_voltage_list(
#         qdac,
#         channel=ch,
#         dwell=2e-6,
#         slew_rate=10,
#         trigger_port=None,
#         output_range="High",
#         output_filter="med",
#         voltage_list=[vlt],
#     )


#######################
# Simulate or execute #
#######################
simulate = False
save_data = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, PROG, simulation_config)
    # Plot the simulated samples
    job.get_simulated_samples().con1.plot()
    plt.show()
else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(PROG)
    # Get results from QUA program
    results = fetching_tool(job, data_list=["I", "Q", "iteration"], mode="live")
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    while results.is_processing():
        # Fetch results
        I, Q, iteration = results.fetch_all()
        # Convert results into Volts
        S = I + 1j * Q
        R = np.abs(S)  # Amplitude
        phase = np.angle(S)  # Phase
        # Progress bar
        progress_counter(iteration, n_avg, start_time=results.get_start_time())
        # Plot results
        # plt.suptitle("RF-reflectometry spectroscopy")
        # plt.cla()
        # plt.plot(ts_plot, R)
        # plt.xlabel("Readout duration [ns]")
        # plt.ylabel(r"$R=\sqrt{I^2 + Q^2}$ [V]")
        # plt.tight_layout()
        # plt.pause(1)

    from scipy.signal import savgol_filter

    # fig = plt.figure()
    # plt.plot(R)
    # plt.plot(savgol_filter(R, 51, 3))
    # plt.show()

    if save_data:
        from qualang_tools.results.data_handler import DataHandler

        # Data to save
        save_data_dict = {}
        # save_data_dict["elapsed_time"] =  np.array([elapsed_time])
        save_data_dict["I"] = I
        save_data_dict["Q"] = Q

        # Save results
        script_name = Path(__file__).name
        data_handler = DataHandler(root_data_folder=save_dir)
        save_data_dict.update({"fig_live": fig})
        data_handler.additional_files = {
            script_name: script_name,
            **default_additional_files,
        }
        data_handler.save_data(data=save_data_dict, name="pulse_effect_on_sensor_dot")

    # plt.show()
    qm.close()

# %%
